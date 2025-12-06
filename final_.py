
# python -m streamlit run final_.py (para probar)

# librerias que voy a usar
import streamlit as st
import pandas as pd
import random

# aca cargo la base de datos principal de marvel
df = pd.read_excel("marvel_database_final.xlsx")

# ------------------ BARRA DE NAVEGACION ------------------
# muestro una imagen en la barra lateral para que se vea cool
st.sidebar.image("barra_imagen.png", use_container_width=True)
# defino las paginas que voy a mostrar en el selectbox de la barra lateral
paginas = ['Inicio', 'Quiz: ¿Qué superhéroe eres?', 'Personajes Marvel',"¡Que la suerte decida!"]
# aqui dejo que el usuario elija la pagina, yo leo lo que elige en pagina_seleccionada
pagina_seleccionada = st.sidebar.selectbox('Echa un vistazo aquí', paginas)

# ========================================= Estilo y colores ====================================
# aca cambio colores de fondo, cabeceras y texto, para que la pagina tenga una estetica oscura/rosa
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

# -------------------------------- Decoracion (fuentes y tamaños) --------------------------------
# aqui enlazo las fuentes desde google fonts y seteo tamaños globales
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Permanent+Marker&family=Comic+Neue:wght@300;400;700&display=swap" rel="stylesheet"> 

<style>
    html, body, [class*="css"] {
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


# ------------------ PÁGINA INICIO ------------------
if pagina_seleccionada == 'Inicio':
    # muestro el titulo principal centrado
    st.markdown("<h1 style='text-align: center;'>Tu héroe Marvel</h1>", unsafe_allow_html=True)

    # divido la pantalla en dos columnas para imagen y texto
    col1, col2 = st.columns(2)

    # en la primera columna muestro la imagen de inicio
    col1.image("fotoinicio.jpg", caption='héroes', width=300)

    # aqui defino el texto introductorio que voy a mostrar en la segunda columna
    texto =  """ 
    ¡Hola! Si has llegado hasta aquí, es porque amas el universo Marvel tanto como nosotros.
    En este espacio encontrarás un recorrido divertido y ordenado por el inmenso mundo de héroes,
    heroínas, villanos y seres sorprendentes que han dado forma a décadas de historias épicas. Este proyecto nace con una idea sencilla: reunir una base de datos clara, visual y fácil de usar 
    con los personajes más representativos de Marvel, acompañados de sus imágenes oficiales. 
    Ya no tendrás que buscar uno por uno: ¡aquí todo está listo para explorar, aprender y disfrutar! Nuestro objetivo es crear una herramienta accesible para fans, estudiantes, desarrolladores y curiosos
    que quieran conocer más sobre el enorme catálogo de personajes del multiverso. Cada entrada combina datos esenciales
    y una imagen confiable, para que puedas navegar como si estuvieras hojeando tu propia enciclopedia digital de Marvel. Prepárate para sumergirte en un viaje lleno de color, poderes increíbles y mucha, mucha diversión.
    ¡El universo Marvel te espera! 🚀🦸‍♂️🦸‍♀️✨"""

    # muestro el texto en la columna 2 con justificado
    col2.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto}</div>", unsafe_allow_html=True)

    # separador visual
    st.markdown("---")
    # subtitulo sobre lo que encontrara el usuario
    st.subheader("¿Qué vas a encontrar en esta pagina?")

    # aqui muestro una lista explicativa con emojis para que quede mas amigable
    st.markdown("""
    💥 ¡Bienvenido al Universo Marvel! 💥

🧠 ¡Descubre tu héroe interior!
Responde nuestro quiz interactivo y averigua qué superhéroe o antihéroe del universo Marvel se parece más a ti. ¡Demuestra tu personalidad y comparte tu resultado con tus amigos!

📊 Explora la base de datos Marvel
Conoce todos los secretos de tus personajes favoritos: poderes, habilidades, equipos y su historia completa. Desde los icónicos Avengers hasta los villanos más temibles, ¡toda la información al alcance de un clic!

🎬 Guías rápidas de películas, series y cómics
Nunca te pierdas una aventura. Encuentra resúmenes y apariciones de tus héroes en películas, series y cómics. Planifica maratones, revive tus escenas favoritas y descubre nuevas historias del universo Marvel
    """)

    # presento a los creadores en dos columnas
    st.subheader("Por ultimo, nuestros creadores")
    col3, col4 = st.columns(2)
    col3.image("pablo.jpg", caption='Pablo Vera, estudiante de Comunicacion audiovisual', width=300)
    col4.image("mateo.jpg", caption='Mateo Angeles, estudiante de Comunicacion para el desarrollo', width=300)


# ------------------ PÁGINA 2 QUIZ ------------------
elif pagina_seleccionada == 'Quiz: ¿Qué superhéroe eres?':
    # muestro el titulo de la pagina del quiz
    st.markdown("<h1 style='text-align: center;'>Descubre aqui tu heroe de Marvel</h1>", unsafe_allow_html=True)

    # texto introductorio corto sobre el proposito del quiz
    texto_2 = """
    ¿Alguna vez te has preguntado qué superhéroe de Marvel sería tu versión ideal?  
    Tal vez siempre has querido saber si tu personalidad encaja mejor con un genio tecnológico como Iron Man,
    un líder noble como el Capitán América, un aventurero cósmico como Thor o un héroe espontáneo y divertido como Spider-Man. Este quiz fue creado para ayudarte a descubrir el personaje que más conecta contigo, basado en tus gustos,
    tus decisiones y la forma en que ves el mundo. ¡Responde honestamente y deja que el multiverso haga su magia!"""

    # defino las preguntas del quiz en una lista de diccionarios
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

    # muestro el texto introductorio en pantalla
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_2}</div>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>Responde las preguntas con calma</h2>", unsafe_allow_html=True)

    # diccionario donde voy guardando las respuestas del usuario
    respuestas_usuario = {}

    # aca recorro la lista de preguntas y muestro cada una con sus opciones como radio buttons
    for i, pregunta in enumerate(preguntas):
        st.markdown(f"### {pregunta['pregunta']}")
        opciones_texto = list(pregunta["opciones"].values())

        seleccion = st.radio(
            "Elige una opción:",
            opciones_texto,
            key=f"pregunta_{i}"
        )

        # guardo la respuesta seleccionada en el diccionario
        respuestas_usuario[i] = seleccion

    # cuando el usuario hace click en el boton, calculo el resultado
    if st.button("Descubrir mi superhéroe"):
        # reseteo la columna puntaje del df para empezar a contar de nuevo
        df["Puntaje"] = 0

        # por cada pregunta busco coincidencias en la columna correspondiente y sumo puntos
        for i, pregunta in enumerate(preguntas):
            columna = pregunta["columna"]
            valor_elegido = respuestas_usuario[i]

            df.loc[
                df[columna].astype(str).str.contains(valor_elegido, case=False, na=False),
                "Puntaje"
            ] += 1

        # determino el maximo puntaje y elijo aleatoriamente entre los empates
        max_puntaje = df["Puntaje"].max()
        candidatos = df[df["Puntaje"] == max_puntaje]
        elegido = candidatos.sample(1).iloc[0]

        # muestro el resultado final y datos basicos del personaje elegido
        st.success(f"¡Tu personaje de Marvel es **{elegido['Nombre héroe/villano']}**! 🦸‍♂️🦸‍♀️")
        st.markdown("### Información de tu personaje")
        st.write(f"**Nombre real:** {elegido['Nombre real']}")
        st.write(f"**Tipo de poder:** {elegido['Tipo de poder']}")
        st.write(f"**Actitud:** {elegido['Actitud']}")
        st.write(f"**Grupo:** {elegido['Grupo']}")
        st.write(f"**Rol:** {elegido['Rol']}")
        st.write(f"**Lugar de nacimiento:** {elegido['Lugar de nacimiento']}")


# ------------------ PÁGINA PERSONAJES MARVEL ------------------
elif pagina_seleccionada == 'Personajes Marvel':
    # muestro titulo y luego cargo el excel que tiene lore y coordenadas
    st.markdown("<h1 style='text-align: center;'>Más información de tu personaje</h1>", unsafe_allow_html=True)
    info_df = pd.read_excel("marvel_database_2.xlsx")

    # genero la lista de personajes disponibles para el selectbox
    personajes_disponibles = sorted(info_df["Character"].unique())
    st.markdown("### Elige tu personaje favorito")
    personaje_elegido = st.selectbox(
        "Escribe o selecciona un personaje:",
        personajes_disponibles
    )

    # filtrado: obtengo la fila del personaje seleccionado
    fila = info_df[info_df["Character"] == personaje_elegido].iloc[0]

    # layout con dos columnas: izquierda mapa, derecha lore
    col1, col2 = st.columns([1, 2])

    # ---------- COLUMNA 1: MAPA ----------
    with col1:
        # muestro el subtitulo del mapa y creo el dataframe con lat/lon para st.map
        st.markdown("#### Ubicación en el mapa (origen / referencia)")
        map_df = pd.DataFrame({
            "lat": [fila["Latitud"]],
            "lon": [fila["Longitud"]]
        })
        st.map(map_df, zoom=2)

    # ---------- COLUMNA 2: LORE + CONTENIDO AUDIOVISUAL ----------
    with col2:
        # muestro nombre del personaje y su lore, uso html para justificar el texto
        st.markdown(f"## {fila['Character']}")
        st.markdown("### Lore del personaje")
        st.markdown(f"<div style='text-align: justify;'>{fila['Lore']}</div>", unsafe_allow_html=True)

        # muestro contenido audiovisual si existe, si no muestro fallback
        st.markdown("### Contenido audiovisual")
        if "Contenido audiovisual" in fila.index:
            st.write(fila["Contenido audiovisual"])
        else:
            st.write(fila.get("Movies", "Sin informacion audiovisual registrada."))


# ------------------ PAGINA: ¡QUE LA SUERTE DECIDA! ------------------
elif pagina_seleccionada == '¡Que la suerte decida!':
    # muestro titulo y explicacion corta
    st.title("¡Personaje Marvel Aleatorio!")
    st.markdown("""
    - ¡Que el multiverso te sorprenda!  
    Aqui no hay preguntas ni tests, solo caos y pura aleatoriedad. Presiona el boton y deja que el destino elija un personaje para ti.
    """)

    # si el usuario pulsa el boton, selecciono un personaje aleatorio del df cargado al inicio
    if st.button("¡Dame un personaje!"):
        personaje = df.sample(1).iloc[0]

        # defino el nombre que voy a mostrar (fallback si cambian nombres de columna)
        nombre_visible = personaje.get("Nombre héroe/villano", personaje.get("Character", "Personaje"))
        st.subheader(nombre_visible)

        # muestro algunos datos basicos si estan presentes en la fila
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

     

# fin 
