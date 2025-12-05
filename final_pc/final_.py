# Ejecutaré la app con: python -m streamlit run final_.py

# ================== LIBRERÍAS QUE UTILIZARÉ ==================
import streamlit as st
import pandas as pd
import random

# ================== BASES DE DATOS QUE VOY A USAR ==================
# Aquí cargaré la base de datos principal de personajes Marvel
df = pd.read_excel("marvel_database_final.xlsx")


# ================== ESTILOS (COLORES + FUENTES) QUE APLICARÉ ==================
st.markdown("""
    <style>
        .stApp {
            background-color: #1B1B1B;
        }

        section[data-testid="stSidebar"] {
            background-color: #ED0547;
        }

        header[data-testid="stHeader"] {
            background-color: #1B1B1B;
        }

        div[data-testid="stToolbar"] {
            background-color: #1B1B1B;
        }

        div[data-testid="stSidebarHeader"] {
            background-color: #ED0547;
        }

        h1 {
            color: #F5F5F5;
        }

        h2 {
            color: #CCCCCC;
        }

        p, div, span {
            color: #E0E0E0;
        }
    </style>
""", unsafe_allow_html=True)

# Aquí configuraré las fuentes y tamaños de letra que quiero usar
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Permanent+Marker&family=Comic+Neue:wght@300;400;700&display=swap" rel="stylesheet"> 

<style>

    html, body, [class*="css"]  {
        font-family: "Comic Neue", sans-serif !important;
        font-size: 18px !important;
    }

    h1 {
        font-family: "Permanent Marker", sans-serif !important;
        font-size: 64px !important;
    }

    h2 {
        font-family: "Comic Neue", sans-serif !important;
        font-size: 32px !important;
    }

    h3 {
        font-family: "Comic Neue", sans-serif !important;
        font-size: 26px !important;
    }

    h4 {
        font-family: "Comic Neue", sans-serif !important;
        font-size: 22px !important;
    }

    section[data-testid="stSidebar"] * {
        font-family: "Comic Neue", sans-serif !important;
        font-size: 20px !important;
    }

    p, div, span, label {
        font-size: 18px !important;
    }

</style>
""", unsafe_allow_html=True)

# Aquí ajustaré el estilo del selectbox del sidebar
st.markdown("""
<style>
    div[data-baseweb="select"] input {
        background-color: #14140F !important;
        color: #F5F5F5 !important;
    }

    div[data-baseweb="select"] > div {
        border-color: #14140F !important;
    }
</style>
""", unsafe_allow_html=True)


# ================== BARRA DE NAVEGACIÓN QUE VOY A MOSTRAR ==================
st.sidebar.image("barra_imagen.png", use_container_width=True)

paginas = [
    'Inicio',
    'Quiz: ¿Qué superhéroe eres?',
    'Personajes Marvel',
    "¡Que la suerte decida!"
]
pagina_seleccionada = st.sidebar.selectbox('Echa un vistazo aquí', paginas)


# ================== PÁGINA: INICIO ==================
if pagina_seleccionada == 'Inicio':

    st.markdown("<h1 style='text-align: center;'>Tu héroe Marvel</h1>", unsafe_allow_html=True)

    # Aquí organizaré el contenido inicial en dos columnas
    col1, col2 = st.columns(2)

    col1.image("fotoinicio.jpg", caption='Héroes', width=300)

    texto = """
    ¡Hola! Si has llegado hasta aquí, es porque amas el universo Marvel tanto como nosotros.
    En este espacio encontrarás un recorrido divertido y ordenado por el inmenso mundo de héroes,
    heroínas, villanos y seres sorprendentes que han dado forma a décadas de historias épicas.
    Este proyecto nace con una idea sencilla: reunir una base de datos clara, visual y fácil de usar 
    con los personajes más representativos de Marvel, acompañados de sus imágenes oficiales. 
    Ya no tendrás que buscar uno por uno: ¡aquí todo está listo para explorar, aprender y disfrutar!
    Nuestro objetivo es crear una herramienta accesible para fans, estudiantes, desarrolladores y curiosos
    que quieran conocer más sobre el enorme catálogo de personajes del multiverso. Cada entrada combina datos esenciales
    y una imagen confiable, para que puedas navegar como si estuvieras hojeando tu propia enciclopedia digital de Marvel.
    Prepárate para sumergirte en un viaje lleno de color, poderes increíbles y mucha, mucha
