# Pages/Clientes/Edit.py

import streamlit as st
from models.Controllers import ClienteController

def editar(cliente_id):
    st.title(f"Editando Cliente ID: {cliente_id}")

    # Obter todos os clientes
    clientes = ClienteController.selecionar_todos_clientes()

    # Procurar o cliente pelo ID
    cliente = None
    for c in clientes:
        if c[0] == cliente_id:
            cliente = c
            break

    if cliente:
        nome = cliente[1]
        idade = cliente[2]
        profissao = cliente[3]

        # Formulário para editar as informações do cliente
        novo_nome = st.text_input("Nome", value=nome)
        nova_idade = st.number_input("Idade", value=idade, format="%d", step=1)
        nova_profissao = st.selectbox("Profissão", ["Desenvolvedor", "Dentista", "Médico", "Padeiro", "Motorista"], index=0)

        # Botão para salvar as alterações
        if st.button("Salvar Alterações"):
            # Função para atualizar as informações do cliente no banco de dados
            ClienteController.atualizar_cliente(cliente_id, novo_nome, nova_idade, nova_profissao)
            st.success("Informações do cliente atualizadas com sucesso!")
    else:
        st.warning("Cliente não encontrado")
