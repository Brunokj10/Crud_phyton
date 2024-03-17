import streamlit as st
from models.Controllers import ClienteController

def list():
    with st.container():
        colms = st.columns((1, 2, 1, 2, 2)) 
        campos = ['Nº', 'Nome', 'Idade', 'Profissão', 'Ações']
        for col, campos_nome in zip(colms, campos):
            col.write(campos_nome)
        
        for item in ClienteController.selecionar_todos_clientes():
            with st.container():
                col1, col2, col3, col4, col5 = st.columns((1, 2, 1, 2, 2))
                col1.write(item[0])  
                col2.write(item[1])  
                col3.write(item[2])  
                col4.write(item[3])  

                # Botão de Excluir
                if col5.button(f'Excluir {item[0]}'):
                    ClienteController.deletar_cliente(item[0])  
                    st.success("Cliente excluído com sucesso!")  # Mensagem de sucesso
                    st.experimental_rerun()  # Recarregar a página para refletir a exclusão
