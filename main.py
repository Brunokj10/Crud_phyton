# main.py
import streamlit as st
import mysql.connector
import pandas as pd
from models.Controllers import ClienteController
import Pages.Clientes.Create as PageIncluirCliente
import Pages.Clientes.List as PageListClientes
import Pages.Clientes.Edit as PageEditarCliente  # Importa a página de edição de cliente

# Definindo a função para inserir um novo cliente no banco de dados
def inserir_cliente(nome, idade, profissao):
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='crud_python'
        )

        # Criar um cursor para executar as consultas SQL
        cursor = conn.cursor()

        sql = "INSERT INTO clientes (nome, idade, profissao) VALUES (%s, %s, %s)"
        val = (nome, idade, profissao)
        cursor.execute(sql, val)
        conn.commit()
        cursor.close()
        conn.close()

        st.success("Cliente inserido com sucesso!")

    except mysql.connector.Error as e:
        st.error(f"Erro ao inserir cliente no banco de dados: {e}")

# Interface do Streamlit
st.sidebar.title("Menu")
Page_Cliente = st.sidebar.selectbox('Cliente', ['Incluir', 'Consultar/Excluir', 'Editar'])  # Alterado para 'Consultar/Excluir'

if Page_Cliente == 'Incluir':
    PageIncluirCliente.create()
elif Page_Cliente == 'Consultar/Excluir':  # Alterado para 'Consultar/Excluir'
    PageListClientes.list()
elif Page_Cliente == 'Editar':
    cliente_id = st.sidebar.number_input('ID do Cliente a Editar', step=1, value=1)  # Campo para inserir o ID do cliente a editar
    PageEditarCliente.editar(cliente_id)  # Chama a função de edição de cliente passando o ID
