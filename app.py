# sheet para app
import streamlit as st
import pandas as pd
import plotly_express as px
import matplotlib.pyplot as plt


ve_us = pd.read_csv(
    "C:\\Users\\USER\OneDrive\\Documentos\\Triple Ten proyects\\modulo_2\\sprint_7\\sprint7\\vehicles_us.csv")

st.header("US Vehicles Data")
st.write('Esta pagina web esta diseñada para mostrar los datos de los autos en Estados Unidos segun el año seleccionado')

st.subheader('Boton')
selected_year = st.slider(
    'selecciona un año',
    min_value=int(ve_us['model_year'].min()),
    max_value=int(ve_us['model_year'].max())
)
start_button = st.button('Buscar')
if start_button:
    data_selected_year = ve_us[ve_us['model_year'] >= selected_year]
    st.write(f'Buscando autos con modelo desde el año {selected_year}')
    st.write(data_selected_year)
    # grafico de dispersión
    st.subheader('Grafico de dispersión')
    fig, ax = plt.subplots()
    valid_colors = data_selected_year['paint_color'].apply(
        lambda x: isinstance(x, str))
    data_clean = data_selected_year[valid_colors]
    unique_colors, color_map = data_clean['paint_color'].factorize()
    ax.scatter(
        x=data_clean['days_listed'],
        y=data_clean['price'],
        c=unique_colors
    )
    ax.set_xlabel('Dias en venta')
    ax.set_ylabel('Precio')
    ax.set_title(
        f'Grafico de dispersion de disponibilidad de autos desde {selected_year}')
    st.pyplot(fig)
    # historiograma
    st.subheader(f'Histograma de odometro de los coches desde {selected_year}')
    hist_fig = px.histogram(data_selected_year, x='odometer', y='price')
    st.plotly_chart(hist_fig)
