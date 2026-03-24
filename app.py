import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('data/vehicles.csv')

st.title('Análise de Veículos')

hist_button = st.button('Criar histograma')

if hist_button:
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)