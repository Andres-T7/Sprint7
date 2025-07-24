import streamlit as st
import pandas as pd
import plotly.express as px

st.header('Análisis Exploratorio de Vehículos')

car_data = pd.read_csv("vehicles_us.csv")  # leer los datos
hist_button = st.button('Generar Histograma')  # crear un botón

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write('Permite visualizar cómo están distribuidos los precios de los vehículos')

    # crear un histograma
    fig = px.histogram(car_data, x="price", nbins=50,
                       title="Distribución de precios",
                       labels={
                           "price": "Precio del vehículo (USD)",
                           "count": "Cantidad de vehículos"})

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


hist_button_2 = st.button('Diagrama de Dispersion')  # crear un botón

if hist_button_2:  # al hacer clic en el botón
    # escribir un mensaje
    st.write('Muestra la relación entre el año del modelo y el precio del vehículo.')

    # crear un diagrama de Dispersion
    fig = px.scatter(car_data, x="model_year", y="price",
                     title="Precio vs Año del modelo", opacity=0.6, labels={
                         "price": "Precio del vehículo (USD)",
                         "model_year": "Año del modelo"})

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

hist_button_3 = st.button('Boxplot')  # crear un botón

if hist_button_3:  # al hacer clic en el botón
    # escribir un mensaje
    st.write('Compara las distribuciones de precio según el tipo de combustible')

# Boxplot por tipo de combustible
fig = px.box(car_data, x="fuel", y="price",
             title="Precio por tipo de combustible", labels={
                         "price": "Precio del Combustible(USD)",
                         "fuel": "Tipo de Combustible"})

# mostrar un gráfico Plotly interactivo
st.plotly_chart(fig, use_container_width=True)

hist_button_4 = st.button('Construir grafico de barras')  # crear un botón

if hist_button_4:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Es útil para entender la composición del inventario y qué categorías dominan el dataset.')

# Gráfico de barras: número de vehículos por tipo
df_counts = car_data['type'].value_counts().reset_index()
# Renombrar columnas para mayor claridad
df_counts.columns = ['Tipo de vehículo', 'Cantidad']

fig = px.bar(df_counts, x='Tipo de vehículo', y='Cantidad',
             title='Número de vehículos por tipo')

# mostrar un gráfico Plotly interactivo
st.plotly_chart(fig, use_container_width=True)
