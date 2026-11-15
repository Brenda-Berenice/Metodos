import streamlit as st
from estilos import cargar_estilos_y_navbar, imagen_a_base64

st.set_page_config(page_title="Introducción", page_icon="📘", layout="wide")
cargar_estilos_y_navbar()

# Cargar imagen local de introducción
img_intro = imagen_a_base64("imagenes/intro.jpg")

st.markdown("""
<style>
    /* Contenedor de imagen con cuadro decorativo malva detrás */
    .intro-img-wrapper {
        position: relative;
        padding-left: 24px;
        padding-bottom: 24px;
        margin-top: 10px;
    }
    .intro-bg-shape {
        position: absolute;
        bottom: 0;
        left: 0;
        width: 72%;
        height: 78%;
        background-color: #B4949D;
        border-radius: 6px;
        z-index: 1;
    }
    .intro-img-wrapper img {
        position: relative;
        width: 100%;
        height: 360px;
        object-fit: cover;
        border-radius: 8px;
        box-shadow: 0 8px 22px rgba(0,0,0,0.08);
        z-index: 2;
    }
    /* Tarjeta blanca de texto */
    .intro-text-card {
        background-color: #FFFFFF;
        padding: 26px 30px;
        border-radius: 16px;
        box-shadow: 0 6px 18px rgba(0,0,0,0.04);
        margin-top: 12px;
        margin-bottom: 22px;
    }
    /* Cuadritos clicables del temario */
    a.temario-link {
        text-decoration: none !important;
        display: block;
    }
    .temario-box {
        padding: 18px 20px;
        border-radius: 12px;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        box-shadow: 0 4px 12px rgba(0,0,0,0.04);
        height: 115px;
    }
    .temario-box:hover {
        transform: translateY(-4px);
        box-shadow: 0 8px 20px rgba(224, 130, 180, 0.25);
    }
    .temario-title {
        font-weight: 800;
        font-size: 15px;
        margin-bottom: 8px;
    }
    .temario-desc {
        font-size: 13.5px;
        line-height: 1.4;
    }
</style>
""", unsafe_allow_html=True)

# Sección superior: Imagen a la izquierda + Texto a la derecha
col_izq, col_der = st.columns([1, 1.35], gap="large")

with col_izq:
    st.markdown(f"""
    <div class="intro-img-wrapper">
        <div class="intro-bg-shape"></div>
        <img src="{img_intro}" alt="Introducción Métodos Numéricos">
    </div>
    """, unsafe_allow_html=True)

with col_der:
    st.markdown("<h1 style='font-size: 36px; font-weight: 800; color: #1A1A1A; margin-bottom: 0px;'>Introducción</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div class="intro-text-card">
        <h3 style="color: #E082B4; font-size: 20px; font-weight: 800; margin-top: 0; margin-bottom: 12px;">
            ¿Qué son los métodos numéricos?
        </h3>
        <p style="color: #555555; font-size: 14px; line-height: 1.65; margin-bottom: 0; text-align: justify;">
            "Los métodos numéricos son técnicas para resolver una gran variedad de problemas matemáticos. 
            Este tipo de métodos solamente emplean operaciones aritméticas y lógicas, de tal manera que los cálculos 
            pueden hacerse directamente o utilizando una computadora digital. La combinación de métodos numéricos y 
            las computadoras digitales han creado una herramienta de inmenso poder en el análisis numérico. Los métodos 
            numéricos son capaces de manejar la no linealidad, la geometría compleja y sistemas grandes de ecuaciones 
            simultáneas que nos necesarios para la simulación perfecta de muchas situaciones físicas reales."
        </p>
    </div>
    <a href="/Unidad_2" target="_self" class="btn-comenzar">Ir a la unidad 2</a>
    """, unsafe_allow_html=True)

st.write("")
st.markdown("<h2 style='font-size: 24px; font-weight: 800; color: #1A1A1A; margin-top: 15px; margin-bottom: 15px;'>Contenido del temario</h2>", unsafe_allow_html=True)

# 4 Cuadritos clicables del temario con contraste mejorado en Unidad 5
c1, c2, c3, c4 = st.columns(4, gap="medium")

with c1:
    st.markdown("""
    <a href="/Unidad_2" target="_self" class="temario-link">
        <div class="temario-box" style="background-color: #E3F0FC; border-left: 5px solid #4A90E2;">
            <div class="temario-title" style="color: #1D4E89;">Unidad 2: Ecuaciones No Lineales</div>
            <div class="temario-desc" style="color: #2B5B84;">Bisección, Newton y Secante.</div>
        </div>
    </a>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <a href="/Unidad_3" target="_self" class="temario-link">
        <div class="temario-box" style="background-color: #E3F6EC; border-left: 5px solid #38A169;">
            <div class="temario-title" style="color: #1E5631;">Unidad 3: Sistemas Lineales</div>
            <div class="temario-desc" style="color: #276749;">Gauss-Jordan, Gauss-Seidel y Jacobi.</div>
        </div>
    </a>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <a href="/Unidad_4" target="_self" class="temario-link">
        <div class="temario-box" style="background-color: #FDF3D7; border-left: 5px solid #D69E2E;">
            <div class="temario-title" style="color: #744210;">Unidad 4: Factorización LU</div>
            <div class="temario-desc" style="color: #744210;">Métodos de Doolittle y Crout.</div>
        </div>
    </a>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
    <a href="/Unidad_5" target="_self" class="temario-link">
        <div class="temario-box" style="background-color: #ECE6FA; border-left: 5px solid #7C4DFF;">
            <div class="temario-title" style="color: #442788;">Unidad 5: Valores Propios</div>
            <div class="temario-desc" style="color: #553C9A;">Potencia y Potencia Inversa.</div>
        </div>
    </a>
    """, unsafe_allow_html=True)
