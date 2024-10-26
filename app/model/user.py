from app.config import connection

# Buscar todos os usuários
def getUser(user_id: int = None, email: str = None):
    try:
        conn = connection.getConnection()
        with conn:
            with conn.cursor() as cursor:
                if user_id is None and email is None:
                    query = "SELECT * FROM users WHERE status = 1"
                    cursor.execute(query)
                    result = cursor.fetchall()
                    return result
                
                if user_id is not None and email is not None:
                    print("Erro ao buscar o usuário. Por favor, informe apenas um parâmetro.")
                    return None 

                query = "SELECT * FROM users WHERE "
                data = None
                if user_id is not None:
                    query += "user_id = %s AND status = 1"
                    data = (user_id,)
                elif email is not None:
                    query += "email = %s AND status = 1"
                    data = (email,)
                
                cursor.execute(query, data)
                result = cursor.fetchone()
                return result            

    except Exception as E:
        print(f"Erro ao buscar o usuário: {E}")
        return None 


# Criar um usuário
def createUser(name: str, email: str, password: str):
    try:
        conn = connection.getConnection()
        with conn:
            conn.begin()
            with conn.cursor() as cursor:
                query = """
                    INSERT INTO users (
                        name, email, password
                    )
                    VALUES (
                        %s, %s, %s
                    )
                """

                data = (name, email, password)
                cursor.execute(query, data)
                if cursor.rowcount > 0:
                    conn.commit()
                    return True
                else:
                    conn.rollback()
                    return False



    except Exception as E:
        print(f"Erro ao criar o usuário: {E}")
        conn.rollback()
        return False
    

def getUsename(email: str) -> str:
    try:
        conn = connection.getConnection()
        with conn:
            with conn.cursor() as cursor:
                query = '''
                    SELECT name FROM users WHERE email = %s
                '''

                data = (email,)
                cursor.execute(query, data)
                
                result = cursor.fetchone()[0]
                return result

    except Exception as E:  
        print(f"Erro ao buscar o nome do usuário: {E}")
        return None
