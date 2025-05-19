# sheet para app
import streamlit as st
import pandas as pd
import plotly_express as px


ve_us = pd.read_csv(
    "C:\\Users\\USER\OneDrive\\Documentos\\Triple Ten proyects\\modulo_2\\sprint_7\\sprint7\\vehicles_us.csv")


# se tienen que sustituir por 0 los valores nulos
ve_us['model_year'] = ve_us['model_year'].fillna(0)
# Se convierten a enteros, el año no puede ser decimal
ve_us['model_year'] = ve_us['model_year'].astype(int)
# No se van a hacer operaciones con el año, por lo que se convierte a string
ve_us['model_year'] = ve_us['model_year'].astype(str)
ve_us['model_year'] = ve_us['model_year'].replace(
    '0', 'NaN')  # Se tiene que saber que el año no puede ser 0


# Se tiene que convertir el cilindraje en 0 los valores nulos
ve_us['cylinders'] = ve_us['cylinders'].fillna(0)
# Se convierten a enteros, el cilindraje no puede ser decimal
ve_us['cylinders'] = ve_us['cylinders'].astype(int)
# No se van a hacer operaciones con el cilindraje, por lo que se convierte a string
ve_us['cylinders'] = ve_us['cylinders'].astype(str)
# No se puede asumir el cilindraje con la media, se tomara como NaN
ve_us['cylinders'] = ve_us['cylinders'].replace('0', 'NaN')


# Se tienen que sustituir por 0 los valores nulos
ve_us['is_4wd'] = ve_us['is_4wd'].fillna(0)
# Se convierten a enteros, el 4wd no puede ser decimal
ve_us['is_4wd'] = ve_us['is_4wd'].astype(int)
# No se van a hacer operaciones con el 4wd, por lo que se convierte a string
ve_us['is_4wd'] = ve_us['is_4wd'].astype(str)


# Damos un valor a los nulos para trabajar
ve_us['odometer'] = ve_us['odometer'].fillna(-1)
# convertimos a enteros, no se puede ser flotante
ve_us['odometer'] = ve_us['odometer'].astype(int)
# Sustituimos el -1 por NaN, y los datos conservan estructura
ve_us['odometer'] = ve_us['odometer'].replace(-1, 'NaN')

# Para no perder datos los valores nulos son Nan
ve_us['paint_color'] = ve_us['paint_color'].fillna('Nan')

st.header("US Vehicles Data")
st.write('Esta pagina web esta diseñada para mostrar los datos de los autos en Estados Unidos segun el año seleccionado')

st.subheader('Boton')
selected_year = st.slider('selecciona un año', min_value=int(
    ve_us['model_year'].min()), max_value=int(ve_us['model_year'].max()))
start_button = st.button('Buscar')
if start_button:
    data_selected_year = ve_us[ve_us['model_year'] >= selected_year]
    st.write('Buscando autos desde el año {selected_year}')
    st.write(data_selected_year)
    # grafico de dispersión
    st.subheader('Grafico de dispersión')
    fig, ax = plt.subplots()
    ax.scatter(data_selected_year, x='days_listed',
               y='price', color='paint_color')
    ax.set_xlabel('Dias en venta')
    ax.set_ylabel('Precio')
    ax.set_title(
        'Grafico de dispersion de disponibilidad de autos desde {selected_year}')
    # historiograma
    st.subheader('Histograma')
    fig = px.histogram(data_selected_year, x='odometer', y='price')
