from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token
from datetime import timedelta

from app.utils import validate, auth, logger
from app.model import user as modelUser

user_routes = Blueprint("user_routes", __name__)

@user_routes.route("/register", methods=["POST"])
def register():
    try:
        data = request.get_json()
        if not data:
            return jsonify(
                {
                    "success": False,
                    "message": "Nenhum dado enviado ao servidor!"
                }
            )
        
        name = data["name"]
        email = data["email"]
        password = data["password"]

        errors = validate.validateSignupData(
            {
                "name": name,
                "email": email,
                "password": password
            }
        )
        if errors:
            return jsonify(errors), 400
        
        hashPassword = auth.hashPassword(password)

        result = modelUser.createUser(name=name, email=email, password=hashPassword)
        if result:
            logger.logCreateUser(name=name, email=email)

            return jsonify(
                {
                    "success": True,
                    "message": "Usuário criado com sucesso!",
                    "user": {
                        "name": name,
                        "email": email
                    }
                }
            ), 201
        else:
            return jsonify(
                {
                    "success": False,
                    "message": "Erro ao registrar novo usuário!"
                }
            ), 400


    except Exception as E:
        print(f"Erro ao registrar novo usuário! [Erro: {E}]")


@user_routes.route("/login", methods=["POST"])
def login():
    try:
        data = request.get_json()
        if not data:
            return jsonify(
                {
                    "success": False,
                    "message": "Nenhum dado enviado ao servidor!"
                }
            )
        
        email = data["name"]
        password = data["password"]

        errors = validate.validateLoginData(
            {
                "email": email,
                "password": password
            }
        )
        if errors:
            return jsonify(errors), 400
        
        data_user = modelUser.getUser(email=email)

        if not data_user:
            return jsonify(
                {
                    "success": False,
                    "message": "Email e/ou senha incorreto(s)!"
                }
            ), 400

        user = {
            "user_id": data_user[0],
            "name": data_user[1],
            "email": data_user[2],
            "password": data_user[3]
        }

        if not auth.checkPassword(password, user["password"]):
            return jsonify(
                {
                    "success": False,
                    "message": "Email e/ou senha incorreto(s)!"
                }
            ), 400
        
        #Estabelecer sessão aqui

        logger.logLogin(name=user["name"], email=user["email"])

        return jsonify(
            {
                "success": True,
                "message": "Usuário logado com sucesso!",
                "user": {
                    "email": email,
                    "password": password
                }
            }
        ), 200

    except Exception as E:
        print(f"Erro ao efetuar login de usuário! [Erro: {E}]")