import streamlit as st
import pandas as pd
import plotly.express as px

st.header('Visualizador de Datos Mercado de Vehiculos')

car_data = pd.read_csv("vehicles_us.csv")  # leer los datos
hist_button = st.button('Construir histograma')  # crear un botón

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para Distribución de precios de los Vehiculos')

    # crear un histograma
    fig = px.histogram(car_data, x="price", nbins=50,
                       title="Distribución de precios")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


hist_button_2 = st.button('Construir Diagrama de Dispersion')  # crear un botón

if hist_button_2:  # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un Diagrama de Dispersion para ver Precio vs Año del modelo')

    # crear un diagrama de Dispersion
    fig = px.scatter(car_data, x="model_year", y="price",
                     title="Precio vs Año del modelo", opacity=0.6)

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
