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
    Prepárate para sumergirte en un viaje lleno de color, poderes increíbles y mucha, mucha diversión.
    ¡El universo Marvel te espera! 🚀🦸‍♂️🦸‍♀️✨
    """

    col2.markdown(
        f"<div style='text-align: justify; font-size: 15px;'>{texto}</div>",
        unsafe_allow_html=True
    )

    st.markdown("---")
    st.subheader("¿Qué vas a encontrar en esta página?")

    # Aquí añadiré una descripción de lo que ofrezco en la app
    st.markdown("""
💥 **¡Bienvenido al Universo Marvel!** 💥  

🧠 **¡Descubre tu héroe interior!**  
Responde nuestro quiz interactivo y averigua qué superhéroe o antihéroe del universo Marvel se parece más a ti.  

📊 **Explora la base de datos Marvel**  
Conoce poderes, habilidades, equipos e historia de tus personajes favoritos.  

🎬 **Guías rápidas de películas, series y cómics**  
Encuentra apariciones de tus héroes en el universo audiovisual de Marvel.
    """)

    st.subheader("Por último, nuestros creadores")

    # Aquí mostraré a los creadores con sus fotos
    col3, col4 = st.columns(2)
    col3.image("pablo.jpg", caption='Pablo Vera, estudiante de Comunicación audiovisual', width=300)
    col4.image("mateo.jpg", caption='Mateo Angeles, estudiante de Comunicación para el desarrollo', width=300)


# ================== PÁGINA: QUIZ ==================
elif pagina_seleccionada == 'Quiz: ¿Qué superhéroe eres?':

    st.markdown("<h1 style='text-align: center;'>Descubre tu héroe de Marvel</h1>", unsafe_allow_html=True)

    texto_2 = """
    ¿Alguna vez te has preguntado qué superhéroe de Marvel sería tu versión ideal?  
    Tal vez siempre has querido saber si tu personalidad encaja mejor con un genio tecnológico como Iron Man,
    un líder noble como el Capitán América, un aventurero cósmico como Thor o un héroe espontáneo y divertido como Spider-Man. Este quiz fue creado para ayudarte a descubrir el personaje que más conecta contigo, basado en tus gustos,
    tus decisiones y la forma en que ves el mundo. ¡Responde honestamente y deja que el multiverso haga su magia!"""

    # Aquí añadiré el texto introductorio del quiz
    st.markdown(
        f"<div style='text-align: justify; font-size: 18px;'>{texto_2}</div>",
        unsafe_allow_html=True
    )

    st.markdown("<h2 style='text-align: center;'>Responde las preguntas con calma</h2>", unsafe_allow_html=True)

    # Aquí definiré las preguntas del quiz
    preguntas = [
        {
            "pregunta": "1. Si pudieras tener un superpoder, ¿cuál elegirías?",
            "columna": "Tipo de poder",
            "opciones": {
                "a": "Físico / Sobrehumano",
                "b": "Tecnológico",
                "c": "Mágico / Sobrenatural",
                "d": "Mutante"
            }
        },
        {
            "pregunta": "2. ¿Cómo te describes mejor?",
            "columna": "Actitud",
            "opciones": {
                "a": "Héroe Inspirador",
                "b": "Rebelde Caótico",
                "c": "Guerrero Oscuro",
                "d": "Cerebro Estratégico"
            }
        },
        {
            "pregunta": "3. Si fueras parte de un equipo, ¿con quién irías?",
            "columna": "Grupo",
            "opciones": {
                "a": "Independiente",
                "b": "Avengers",
                "c": "X-Men",
                "d": "Guardians of the Galaxy"
            }
        },
        {
            "pregunta": "4. ¿Qué rol crees que tendrías en el universo Marvel?",
            "columna": "Rol",
            "opciones": {
                "a": "Héroe",
                "b": "Villano",
                "c": "Antihéroe",
                "d": "Líder"
            }
        },
        {
            "pregunta": "5. ¿Cómo te ven los demás?",
            "columna": "Actitud",
            "opciones": {
                "a": "Héroe Inspirador",
                "b": "Rebelde Caótico",
                "c": "Guerrero Oscuro",
                "d": "Cerebro Estratégico"
            }
        },
        {
            "pregunta": "6. ¿Con qué tipo de habilidad conectas más?",
            "columna": "Tipo de poder",
            "opciones": {
                "a": "Físico / Sobrehumano",
                "b": "Tecnológico",
                "c": "Mágico / Sobrenatural",
                "d": "Mutante"
            }
        }
    ]

    # Aquí iré guardando las respuestas del usuario
    respuestas_usuario = {}

    # Aquí mostraré cada pregunta con sus opciones
    for i, pregunta in enumerate(preguntas):
        st.markdown(f"### {pregunta['pregunta']}")
        opciones_texto = list(pregunta["opciones"].values())

        seleccion = st.radio(
            "Elige una opción:",
            opciones_texto,
            key=f"pregunta_{i}"
        )

        respuestas_usuario[i] = seleccion

    # Aquí calcularé el resultado del quiz cuando el usuario presione el botón
    if st.button("Descubrir mi superhéroe"):

        df["Puntaje"] = 0

        for i, pregunta in enumerate(preguntas):
            columna = pregunta["columna"]
            valor_elegido = respuestas_usuario[i]

            df.loc[
                df[columna].astype(str).str.contains(valor_elegido, case=False, na=False),
                "Puntaje"
            ] += 1

        max_puntaje = df["Puntaje"].max()
        candidatos = df[df["Puntaje"] == max_puntaje]

        elegido = candidatos.sample(1).iloc[0]

        st.success(f"¡Tu personaje de Marvel es **{elegido['Nombre héroe/villano']}**! 🦸‍♂️🦸‍♀️")

        st.markdown("### Información de tu personaje")

        st.write(f"**Nombre real:** {elegido['Nombre real']}")
        st.write(f"**Tipo de poder:** {elegido['Tipo de poder']}")
        st.write(f"**Actitud:** {elegido['Actitud']}")
        st.write(f"**Grupo:** {elegido['Grupo']}")
        st.write(f"**Rol:** {elegido['Rol']}")
        st.write(f"**Lugar de nacimiento:** {elegido['Lugar de nacimiento']}")

        if 'Imagen' in elegido.index and pd.notna(elegido['Imagen']):
            st.image(elegido['Imagen'], caption=elegido['Nombre héroe/villano'], width=300)


# ================== PÁGINA: PERSONAJES MARVEL ==================
elif pagina_seleccionada == 'Personajes Marvel':

    st.markdown("<h1 style='text-align: center;'>Más información de tu personaje</h1>", unsafe_allow_html=True)

    # Aquí cargaré la base fusionada con lore, pelis y coordenadas
    info_df = pd.read_excel("marvel_database_2.xlsx")

    personajes_disponibles = sorted(info_df["Character"].unique())

    st.markdown("### Elige tu personaje favorito")
    personaje_elegido = st.selectbox(
        "Escribe o selecciona un personaje:",
        personajes_disponibles
    )

    # Aquí filtraré la fila del personaje elegido
    fila = info_df[info_df["Character"] == personaje_elegido].iloc[0]

    # Aquí organizaré la vista en dos columnas
    col1, col2 = st.columns([1, 2])

    # ---------- COLUMNA 1: IMAGEN + MAPA ----------
    with col1:
        img_path = None

        if "Imagen" in df.columns:
            fila_img = None

            if "Character" in df.columns and personaje_elegido in df["Character"].values:
                fila_img = df[df["Character"] == personaje_elegido].iloc[0]
            elif "Nombre héroe/villano" in df.columns:
                mask_img = df["Nombre héroe/villano"].astype(str).str.contains(
                    personaje_elegido, case=False, na=False
                )
                if mask_img.any():
                    fila_img = df[mask_img].iloc[0]

            if fila_img is not None:
                nombre_archivo = str(fila_img["Imagen"]).strip()
                img_path = f"foto/{nombre_archivo}"

        if img_path:
            st.image(img_path, caption=personaje_elegido, use_container_width=True)

        st.markdown("#### Ubicación en el mapa (origen / referencia)")
        map_df = pd.DataFrame({
            "lat": [fila["Latitud"]],
            "lon": [fila["Longitud"]]
        })
        st.map(map_df, zoom=2)

    # ---------- COLUMNA 2: LORE + CONTENIDO AUDIOVISUAL ----------
    with col2:
        st.markdown(f"## {fila['Character']}")
        st.markdown("### Lore del personaje")
        st.markdown(
            f"<div style='text-align: justify;'>{fila['Lore']}</div>",
            unsafe_allow_html=True
        )

        st.markdown("### Contenido audiovisual")
        if "Contenido audiovisual" in fila.index:
            st.write(fila["Contenido audiovisual"])
        else:
            st.write(fila.get("Movies", "Sin información audiovisual registrada."))


# ================== PÁGINA: ¡QUE LA SUERTE DECIDA! ==================
elif pagina_seleccionada == '¡Que la suerte decida!':

    st.title("¡Personaje Marvel Aleatorio!")

    # Aquí pondré una breve explicación de esta sección
    st.markdown("""
    🔹 ¡Que el multiverso te sorprenda!  
    Aquí no hay preguntas ni tests, solo caos y pura aleatoriedad.  
    Presiona el botón y deja que el destino elija un personaje para ti.
    """)

    if st.button("¡Dame un personaje!"):
        personaje = df.sample(1).iloc[0]

        nombre_visible = personaje.get("Nombre héroe/villano", personaje.get("Character", "Personaje"))

        st.subheader(nombre_visible)

        if "Tipo de poder" in personaje.index:
            st.write(f"*Tipo de poder:* {personaje['Tipo de poder']}")
        if "Actitud" in personaje.index:
            st.write(f"*Actitud:* {personaje['Actitud']}")
        if "Grupo" in personaje.index:
            st.write(f"*Grupo:* {personaje['Grupo']}")
        if "Rol" in personaje.index:
            st.write(f"*Rol:* {personaje['Rol']}")
        if "Lugar de nacimiento" in personaje.index:
            st.write(f"*Lugar de nacimiento:* {personaje['Lugar de nacimiento']}")

        if "Imagen" in personaje.index and pd.notna(personaje["Imagen"]):
            nombre_archivo = str(personaje["Imagen"]).strip()
            img_path = f"foto/{nombre_archivo}"
            st.image(img_path, caption=nombre_visible, use_container_width=True)
