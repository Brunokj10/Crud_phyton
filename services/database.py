import mysql.connector

# Defina os detalhes da conexão com o banco de dados MySQL
HOST = 'localhost'
DATABASE = 'crud_python'
USERNAME = 'root'
PASSWORD = ''

# Crie uma conexão com o banco de dados MySQL
try:
    conn = mysql.connector.connect(
        host=HOST,
        user=USERNAME,
        password=PASSWORD,
        database=DATABASE
    )
    
    if conn.is_connected():
        print("Conexão bem-sucedida!")

except mysql.connector.Error as e:
    print("Erro ao conectar ao banco de dados MySQL:", e)

# Agora você pode usar 'conn' para realizar operações no banco de dados
