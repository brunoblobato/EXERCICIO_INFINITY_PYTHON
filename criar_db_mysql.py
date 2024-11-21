import mysql.connector

# Configurações de conexão
host = 'localhost'
user = 'root'
password = '123456' # Senha que criei para o bando de dados

# Conectar ao MySQL
try:
    conn = mysql.connector.connect(host=host, user=user, password=password)
    cursor = conn.cursor()

    # SQL para criar o banco de dados
    create_db_sql = "CREATE DATABASE IF NOT EXISTS Infinity_School;"

    # Salvar o script SQL em um arquivo
    with open("create_infinity_school.sql", "w") as file:
        file.write(create_db_sql)

    print("Script SQL criado e salvo como 'create_infinity_school.sql'.")

    # Executar o script SQL
    cursor.execute(create_db_sql)
    print("Banco de dados 'Infinity_School' criado com sucesso.")

except mysql.connector.Error as err:
    print(f"Erro: {err}")
finally:
    # Fechar a conexão
    if conn.is_connected():
        cursor.close()
        conn.close()
