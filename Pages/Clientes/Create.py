import streamlit as st
import pandas as pd
from models.Controllers import ClienteController
st.title("Incluir Cliente")
    # Formulário para inserir informações do cliente
def create():
    with st.form(key="include_cliente"):
        input_name = st.text_input(label="Insira seu nome")
        input_age = st.number_input(label="Insira sua idade", format="%d", step=1)
        input_occupation = st.selectbox("Selecione sua profissão", ["Desenvolvedor", "Dentista", "Médico", "Padeiro", "Motorista",])
        input_button_submit = st.form_submit_button("Enviar")
        
   
    if input_button_submit:
       
        ClienteController.inserir_cliente(input_name, input_age, input_occupation) 