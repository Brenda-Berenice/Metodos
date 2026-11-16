import streamlit as st
from estilos import cargar_estilos_y_navbar, imagen_a_base64

st.set_page_config(page_title="Nosotros - Métodos Numéricos", layout="wide")
cargar_estilos_y_navbar()
st.session_state.portada_vista = True

escudo1 = imagen_a_base64("imagenes/escudo1.png")
escudo2 = imagen_a_base64("imagenes/escudo2.png")

try:
    fondo_hojas = imagen_a_base64("imagenes/fondo_nosotros.jpg")
    bg_hero = f"linear-gradient(rgba(168, 102, 138, 0.84), rgba(154, 90, 125, 0.88)), url('{fondo_hojas}')"
except Exception:
    bg_hero = "linear-gradient(135deg, #BD7B9E 0%, #9E5E80 100%)"

st.markdown(f"""
<style>
@import url('https://googleapis.com');

.nosotros-wrapper {{
    border-radius: 16px;
    overflow: hidden;
    box-shadow: 0 10px 28px rgba(0, 0, 0, 0.07);
    margin-top: 10px;
    margin-bottom: 24px;
    font-family: 'Poppins', sans-serif !important;
}}
.header-uni {{
    background-color: #F7C6DF;
    padding: 26px 44px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 20px;
}}
.escudo-box {{
    width: 110px;
    height: 110px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
}}
.escudo-box img {{
    max-width: 100%;
    max-height: 100%;
    object-fit: contain;
}}
.uni-textos {{
    text-align: center;
    color: #2B2428;
}}
.uni-nombre {{
    font-family: 'Poppins', sans-serif !important;
    font-size: 14.5px;
    font-weight: 500;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin: 0 0 4px 0;
}}
.facultad-nombre {{
    font-family: 'Poppins', sans-serif !important;
    font-size: 22px;
    font-weight: 300;
    letter-spacing: 1px;
    margin: 0;
}}
.hero-nosotros {{
    background: {bg_hero};
    background-size: cover;
    background-position: center;
    padding: 58px 30px;
    text-align: center;
    color: #FFFFFF;
}}
.hero-titulo {{
    font-family: 'Poppins', sans-serif !important;
    font-size: 44px;
    font-weight: 500;
    letter-spacing: 3px;
    margin: 0 0 4px 0;
    text-transform: uppercase;
    color: #FFFFFF !important;
}}
.hero-subtitulo {{
    font-family: 'Poppins', sans-serif !important;
    font-size: 20px;
    font-weight: 400;
    font-style: italic;
    letter-spacing: 0.8px;
    color: #FCEEF5;
    margin: 0 0 44px 0;
}}
.integrantes-container {{
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 26px;
    max-width: 780px;
    margin: 0 auto;
}}
.integrantes-label {{
    font-family: 'Poppins', sans-serif !important;
    font-size: 16px;
    font-weight: 600;
    letter-spacing: 2px;
    text-transform: uppercase;
    text-align: right;
    padding-right: 26px;
    border-right: 1.5px solid rgba(255, 255, 255, 0.85);
    color: #FFFFFF;
}}
.integrantes-lista {{
    text-align: left;
    font-family: 'Poppins', sans-serif !important;
    font-size: 16px;
    line-height: 1.65;
    font-weight: 300;
    color: #FFFFFF;
}}
.integrantes-lista p {{
    margin: 0;
    letter-spacing: 0.3px;
}}
.footer-nosotros {{
    background-color: #F7C6DF;
    padding: 16px 40px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    color: #2B2428;
    font-family: 'Poppins', sans-serif !important;
    font-size: 15px;
    font-weight: 400;
}}
.footer-nosotros strong {{
    font-weight: 600;
}}
@media (max-width: 768px) {{
    .header-uni {{ flex-direction: column; text-align: center; }}
    .hero-titulo {{ font-size: 30px; }}
    .integrantes-container {{ flex-direction: column; text-align: center; }}
    .integrantes-label {{ border-right: none; border-bottom: 1.5px solid rgba(255,255,255,0.85); padding-right: 0; padding-bottom: 10px; text-align: center; }}
    .integrantes-lista {{ text-align: center; }}
    .footer-nosotros {{ flex-direction: column; gap: 8px; }}
}}
</style>

<div class="nosotros-wrapper">
<div class="header-uni">
<div class="escudo-box">
<img src="{escudo1}" alt="Escudo 1">
</div>
<div class="uni-textos">
<p class="uni-nombre">UNIVERSIDAD NACIONAL AUTÓNOMA DE MÉXICO</p>
<p class="facultad-nombre">Facultad de Estudios Superiores Acatlán</p>
</div>
<div class="escudo-box">
<img src="{escudo2}" alt="Escudo 2">
</div>
</div>
<div class="hero-nosotros">
<h1 class="hero-titulo">MÉTODOS NUMÉRICOS</h1>
<p class="hero-subtitulo">Proyecto final</p>
<div class="integrantes-container">
<div class="integrantes-label">INTEGRANTES</div>
<div class="integrantes-lista">
<p>Brindis Gamboa María Fernanda</p>
<p>González Hernández Eric Noel</p>
<p>Leyva Chávez Brenda Berenice</p>
<p>Reyes García Evelyn Yesenia</p>
</div>
</div>
</div>
<div class="footer-nosotros">
<div><strong>Profesor:</strong> Curiel García Carlos Pedro</div>
<div><strong>Grupo:</strong> 1354</div>
</div>
</div>
""", unsafe_allow_html=True)
