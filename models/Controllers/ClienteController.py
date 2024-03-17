import mysql.connector
from mysql.connector import Error
import streamlit as st

def inserir_cliente(nome, idade, profissao):
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='crud_python'
        )

        cursor = conn.cursor()

        sql = "INSERT INTO clientes (nome, idade, profissao) VALUES (%s, %s, %s)"
        val = (nome, idade, profissao)
        cursor.execute(sql, val)

        conn.commit()

        cursor.close()
        conn.close()

        st.success("Cliente inserido com sucesso!")

    except Error as e:
        st.error(f"Erro ao inserir cliente no banco de dados: {e}")

def selecionar_todos_clientes():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='crud_python'
        )

        cursor = conn.cursor()

        sql = "SELECT * FROM clientes"
        cursor.execute(sql)

        resultados = cursor.fetchall()

        cursor.close()
        conn.close()

        return resultados

    except Error as e:
        st.error(f"Erro ao selecionar clientes do banco de dados: {e}")
        return None

def deletar_cliente(id_cliente):
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='crud_python'
        )

        cursor = conn.cursor()

        sql = "DELETE FROM clientes WHERE id = %s"
        val = (id_cliente,)
        cursor.execute(sql, val)

        conn.commit()

        cursor.close()
        conn.close()

        st.success("Cliente deletado com sucesso!")

    except Error as e:
        st.error(f"Erro ao deletar cliente do banco de dados: {e}")
        
def atualizar_cliente(id_cliente, novo_nome, nova_idade, nova_profissao):
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='crud_python'
        )

        cursor = conn.cursor()

        sql = "UPDATE clientes SET nome = %s, idade = %s, profissao = %s WHERE id = %s"
        val = (novo_nome, nova_idade, nova_profissao, id_cliente)
        cursor.execute(sql, val)

        conn.commit()

        cursor.close()
        conn.close()

        st.success("Cliente atualizado com sucesso!")

    except Error as e:
        st.error(f"Erro ao atualizar cliente no banco de dados: {e}")

