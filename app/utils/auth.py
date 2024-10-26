from bcrypt import (
    hashpw,
    gensalt,
    checkpw
)

def hashPassword(password):
    return hashpw(password.encode('utf-8'), gensalt())

def checkPassword(password, hash):
    return checkpw(password.encode('utf-8'), hash.encode('utf-8'))