import streamlit as st
from estilos import cargar_estilos_y_navbar

st.set_page_config(page_title="Nosotros", page_icon="👩‍💻", layout="wide")
cargar_estilos_y_navbar()

st.markdown("<h1 style='font-weight: 800;'>👩‍💻 Sobre el Proyecto y Equipo</h1>", unsafe_allow_html=True)

st.markdown("""
<div style="background-color: white; padding: 30px; border-radius: 14px; box-shadow: 0 6px 18px rgba(0,0,0,0.05); margin-top: 15px;">
    <h3 style="color: #E082B4; margin-top: 0;">Proyecto Final de Métodos Numéricos</h3>
    <p style="color: #444; font-size: 15px; line-height: 1.6;">
        Esta aplicación fue desarrollada con el objetivo de facilitar la comprensión visual y el cálculo iterativo 
        de los principales algoritmos del análisis numérico estudiados durante el curso.
    </p>
    <hr style="border: none; border-top: 1px solid #FCEEF5; margin: 20px 0;">
    <p><b>🏫 Institución:</b> Nombre de tu Universidad / Escuela</p>
    <p><b>📚 Materia:</b> Métodos Numéricos</p>
    <p><b>👨‍🏫 Profesor(a):</b> Nombre de tu Profesor(a)</p>
    <p><b>✨ Integrantes:</b></p>
    <ul>
        <li>Tu Nombre Completo</li>
        <li>Integrante 2 (si aplica)</li>
    </ul>
</div>
""", unsafe_allow_html=True)
