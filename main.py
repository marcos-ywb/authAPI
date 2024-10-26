from flask import Flask, request, session, jsonify
from flask_session import Session
from app.cfg import Config
from app.utils import validate, auth, logger
from app.model import database

from app.model import user as modelUser

app = Flask(__name__)

app.config["SECRET_KEY"] = Config.SECRET_KEY
app.config["SESSION_TYPE"] = Config.SESSION_TYPE

Session(app)

# Rota de registro
@app.route("/api/signup", methods=["POST"])
def signup():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    errors = validate.validateSignupData({"name": name, "email": email, "password": password})
    if errors:
        return jsonify(errors), 400
    
    hashPassword = auth.hashPassword(password)

    result = modelUser.createUser(name=name, email=email, password=hashPassword)
    if result:

        logger.logCreateUser(name=name, email=email)

        return jsonify(
            {
                "message": "Usário criado com sucesso!",
                "user": {
                    "name": name,
                    "email": email
                }
            }
        ), 201
    
    else:
        return jsonify(
            {
                "message": "Erro ao criar o usuário!"
            }
        ), 400


# Rota de login
@app.route("/api/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    errors = validate.validateLoginData({"email": email, "password": password})
    if errors:
        return jsonify(errors), 400

    data_user = modelUser.getUser(email=email)

    if not data_user:
        return jsonify(
            {
                "message": "Email ou senha inválidos!"
            }
        ), 400

    user = {
        "user_id": data_user[0],
        "name": data_user[1],
        "email": data_user[2],
        "password": data_user[3]
    }

    if not auth.checkPassword(password, user["password"]):
        return jsonify({"message": "Email ou senha inválidos!"}), 400
    
    session["user_session"] = email

    logger.logLogin(name=user["name"], email=user["email"])

    return jsonify(
        {
            "message": "Usuário logado com sucesso!",
            "user": {
                "email": email,
                "password": password
            }
        }
    ), 200


# Rota de rota protegida
@app.route("/api/protected", methods=["GET"])
def protected():
    if "user_session" in session:

        logger.logProtectedRoute(name=modelUser.getUsename(email=session.get("user_session")), email=session.get("user_session"), sucess=True)

        return jsonify(
            {
                "message": "Usário autenticado com sucesso!"
            }
        ), 200
    else:

        logger.logProtectedRoute(name='Desconhecido', email='Não informado', sucess=False)

        return jsonify(
            {
                "message": "Usário não autenticado!"
            }
        ), 401


# Rota de logout
@app.route("/api/logout", methods=["POST"])
def logout():
    email = session.get("user_session")
    logger.logLogout(name=modelUser.getUsename(email=email), email=email)

    session.pop("user_session", None)
    return jsonify(
        {
            "message": "Usuário deslogado com sucesso!"
        }
    ), 200



# Iniciar servidor
if __name__ == "__main__":
    database.verifyUserTable()
    app.run(
        host=Config.API_HOST,
        port=Config.API_PORT,
        debug=True
    )