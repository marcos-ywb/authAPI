from app.config import connection

# Verificar se a tabela 'users' já existe
def verifyUserTable():
    try:
        conn = connection.getConnection()
        with conn:
            with conn.cursor() as cursor:
                query = """
                    SHOW TABLES LIKE 'users'
                """
                cursor.execute(query)
                result = cursor.fetchone()
                if result:
                    print("Tabela 'users' já existe!")
                else:
                    print("Tabela 'users' ainda não existe! Criando...")
                    migrateUserTables()

    except Exception as E:
        print(f"Erro ao verificar a tabela 'users' {E}")

# Migrar o banco de dados caso a tabela 'users' não exista
def migrateUserTables():
    try:
        conn = connection.getConnection()
        with conn:
            conn.begin()
            with conn.cursor() as cursor:
                query = """
                    CREATE TABLE IF NOT EXISTS users (
                        user_id INT NOT NULL AUTO_INCREMENT,
                        name VARCHAR(255) NOT NULL,
                        email VARCHAR(255) NOT NULL,
                        password VARCHAR(255) NOT NULL,
                        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                        status TINYINT(1) DEFAULT 1,
                        PRIMARY KEY (user_id)
                    )
                """
                cursor.execute(query)
                
                cursor.execute("SHOW TABLES LIKE 'users'")
                result = cursor.fetchone()
                if result:
                    print("Tabela 'users' criada com sucesso!")
                    conn.commit()
                else:
                    print("Erro ao criar a tabela 'users'")
                    conn.rollback()

    except Exception as E:
        print(f"Erro ao migrar o banco de dados {E}")
        conn.rollback()