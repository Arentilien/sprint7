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


# Para no perder datos los valores nulos son Nan
ve_us['paint_color'] = ve_us['paint_color'].fillna('Nan')

st.header("US Vehicles Data")

st.subheader('Historiograma')

st.subheader('grafico de dispersion')

st.subheader('Boton')
