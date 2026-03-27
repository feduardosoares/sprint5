import os
import pandas as pd
import plotly.express as px
import streamlit as st

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, 'data', 'vehicles.csv')

car_data = pd.read_csv(file_path)

st.title('Análise de Veículos')

hist_button = st.button('Criar histograma')

if hist_button:
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Criar gráfico de dispersão')

if scatter_button: # se o botão for clicado
    st.write('Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')
    
    # criar um gráfico de dispersão
    fig = px.scatter(car_data, x="odometer", y="price")
    
    # exibir o gráfico
    st.plotly_chart(fig, use_container_width=True)