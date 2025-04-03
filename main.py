from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from app.cfg import Config
from app.model import database


from app.routes import user_routes

app = Flask(__name__)
CORS(app)

app.config["JWT_SECRET_KEY"] = Config.JWT_SECRET_KEY
jwt = JWTManager(app)

app.register_blueprint(user_routes.user_routes, url_prefix="/api/user")

# Iniciar servidor
if __name__ == "__main__":
    database.verifyUserTable()
    app.run(
        host=Config.API_HOST,
        port=Config.API_PORT,
        debug=True
    )