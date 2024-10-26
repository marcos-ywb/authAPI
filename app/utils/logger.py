import logging
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
log_dir = os.path.join(current_dir, '..', 'logs')

logger = logging.getLogger('AuthAPI')
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(f"{log_dir}/logs.txt")
file_handler.setLevel(logging.INFO)

formatter = logging.Formatter(
    '[Data/Hora]: %(asctime)s \n'
    '[Nível]: %(levelname)s \n'
    '[Mensagem]: %(message)s \n'
    '[Nome do Usuário]: %(username)s \n'
    '[Email]: %(email)s \n'
    '\n',
    datefmt='%d/%m/%Y - %H:%M:%S'
)

file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def logEvent(level, message, user=None, **kwargs):
    extra_info = {
        'username': user if user else 'Desconhecido',
        'email': kwargs.get('email', 'Não informado')
    }
    
    full_message = f"{message}"

    if level == "info":
        logger.info(full_message, extra=extra_info)
    elif level == "warning":
        logger.warning(full_message, extra=extra_info)
    elif level == "error":
        logger.error(full_message, extra=extra_info)

def logCreateUser(name, email):
    logEvent("info", "Registro realizado com sucesso!", user=name, email=email)

def logLogin(name, email, sucess=True):
    if sucess:
        logEvent("info", "Login realizado com sucesso!", user=name, email=email)
    else:
        logEvent("warning", "Email ou senha inválidos!", user=name, email=email)

def logLogout(name, email):
    logEvent("info", "Logout realizado com sucesso!", user=name, email=email)

def logProtectedRoute(name, email, sucess=True):
    if sucess:
        logEvent("info", "Rota protegida acessada com sucesso!", user=name, email=email)
    else:
        logEvent("warning", "Rota protegida acessada sem autenticação!", user=name, email=email)
