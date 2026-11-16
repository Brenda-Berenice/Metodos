import streamlit as st
from estilos import cargar_estilos_y_navbar, imagen_a_base64

st.set_page_config(page_title="Métodos Numéricos", page_icon="🧮", layout="wide")
cargar_estilos_y_navbar()

# Cargar imágenes locales
img_banner = imagen_a_base64("imagenes/banner.jpg")
img_u2 = imagen_a_base64("imagenes/u2.jpg")
img_u3 = imagen_a_base64("imagenes/u3.jpg")
img_u4 = imagen_a_base64("imagenes/u4.jpg")
img_u5 = imagen_a_base64("imagenes/u5.jpg")

# Banner panorámico
st.markdown(f"""
<div class="hero-banner">
    <img src="{img_banner}" alt="Banner Matemáticas">
</div>
""", unsafe_allow_html=True)

# Sección inferior: Columna izquierda (Texto) + 4 Tarjetas de Unidades a la derecha
col_texto, col_u2, col_u3, col_u4, col_u5 = st.columns([1.35, 1, 1, 1, 1], gap="small")

with col_texto:
    st.markdown("<h1 style='font-size: 32px; line-height: 1.15; font-weight: 800; color: #1A1A1A; margin-top: 0px;'>Explora los Métodos Numéricos</h1>", unsafe_allow_html=True)
    st.markdown("""
    <p style='color: #555555; font-size: 13.5px; line-height: 1.55; margin-top: 10px; margin-bottom: 18px;'>
    Sistema interactivo organizado por unidades del temario para resolver ecuaciones no lineales, sistemas lineales, factorización LU y valores propios.
    </p>
    <a href="/Introduccion" target="_self" class="btn-comenzar">Comenzar ahora</a>
    <p style='font-size: 12px; color: #777777; margin-top: 18px; line-height: 1.45;'>
        <b>Integrantes:</b> Brindis Gamboa María Fernanda | González Hernández Eric Noel | Leyva Chávez Brenda Berenice | Reyes García Evelyn Yesenia<br>
        <b>Materia:</b> Métodos Numéricos
    </p>
    """, unsafe_allow_html=True)

with col_u2:
    st.markdown(f"""
    <a href="/Unidad_2" target="_self" class="card-link">
        <div class="photo-card">
            <img src="{img_u2}">
            <div class="card-title">Unidad 2</div>
            <div class="card-sub">Bisección • Newton • Secante</div>
        </div>
    </a>
    """, unsafe_allow_html=True)

with col_u3:
    st.markdown(f"""
    <a href="/Unidad_3" target="_self" class="card-link">
        <div class="photo-card">
            <img src="{img_u3}">
            <div class="card-title">Unidad 3</div>
            <div class="card-sub">Gauss-Jordan • Seidel • Jacobi</div>
        </div>
    </a>
    """, unsafe_allow_html=True)

with col_u4:
    st.markdown(f"""
    <a href="/Unidad_4" target="_self" class="card-link">
        <div class="photo-card">
            <img src="{img_u4}">
            <div class="card-title">Unidad 4</div>
            <div class="card-sub">Doolittle • Crout</div>
        </div>
    </a>
    """, unsafe_allow_html=True)

with col_u5:
    st.markdown(f"""
    <a href="/Unidad_5" target="_self" class="card-link">
        <div class="photo-card">
            <img src="{img_u5}">
            <div class="card-title">Unidad 5</div>
            <div class="card-sub">Potencia • Potencia Inversa</div>
        </div>
    </a>
    """, unsafe_allow_html=True)
