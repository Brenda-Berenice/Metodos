import streamlit as st
import base64
import os
import time

def imagen_a_base64(ruta):
    if os.path.exists(ruta):
        with open(ruta, "rb") as f:
            data = base64.b64encode(f.read()).decode("utf-8")
        ext = ruta.split(".")[-1].lower()
        if ext == "jpg":
            ext = "jpeg"
        return f"data:image/{ext};base64,{data}"
    return ""

def cargar_estilos_y_navbar():
    # Pantalla final de cierre con referencias bibliográficas (sin menú ni navegación)
    if st.query_params.get("salir") == "1":
        st.markdown("""
        <style>
            .stApp { background-color: #FCEEF5; }
            /* Ocultar menú lateral, barra superior y cualquier botón de regreso */
            header[data-testid="stHeader"], section[data-testid="stSidebar"], div[data-testid="stToolbar"] {
                display: none !important;
            }
            .exit-card {
                background-color: #FFFFFF;
                padding: 45px;
                border-radius: 16px;
                max-width: 720px;
                margin: 40px auto;
                box-shadow: 0 10px 30px rgba(224, 130, 180, 0.2);
                border-top: 6px solid #E082B4;
            }
            .exit-title {
                color: #1A1A1A;
                font-size: 30px;
                font-weight: 800;
                text-align: center;
                margin-bottom: 8px;
            }
            .exit-subtitle {
                color: #E082B4;
                font-size: 16px;
                font-weight: 700;
                text-align: center;
                margin-bottom: 25px;
            }
            .ref-box {
                background-color: #FCEEF5;
                padding: 20px 25px;
                border-radius: 10px;
                margin-top: 20px;
                color: #333333;
                font-size: 14px;
                line-height: 1.7;
            }
        </style>
        <div class="exit-card">
            <div class="exit-title">🎓 Sesión Finalizada</div>
            <div class="exit-subtitle">Proyecto Final • Métodos Numéricos</div>
            <p style="text-align: center; color: #555555; font-size: 15px;">
                Gracias por utilizar <b>Numérika Lab</b>. El sistema ha cerrado todos los módulos correctamente.
            </p>
            <div class="ref-box">
                <b style="color: #1A1A1A; font-size: 15px;">📚 Referencias Bibliográficas:</b>
                <ul style="margin-top: 10px; margin-bottom: 0;">
                    <li>Chapra, S. C., & Canale, R. P. (2015). <i>Métodos numéricos para ingenieros</i> (7.ª ed.). McGraw-Hill Education.</li>
                    <li>Burden, R. L., & Faires, J. D. (2017). <i>Análisis numérico</i> (10.ª ed.). Cengage Learning.</li>
                    <li>Nieves Hurtado, A., & Domínguez Sánchez, F. C. (2014). <i>Métodos numéricos aplicados a la ingeniería</i>. Grupo Editorial Patria.</li>
                </ul>
            </div>
            <p style="text-align: center; color: #888888; font-size: 13px; margin-top: 25px; margin-bottom: 0;">
                🔒 Aplicación detenida. Ya puedes cerrar esta ventana del navegador.
            </p>
        </div>
        """, unsafe_allow_html=True)
        time.sleep(1.5)
        os._exit(0)

    st.markdown("""
    <style>
        /* Fondo rosa pastel de toda la app */
        .stApp {
            background-color: #FCEEF5;
        }
        /* Hacer transparente la barra superior de Streamlit y ocultar botón Deploy */
        header[data-testid="stHeader"] {
            background-color: transparent !important;
        }
        
        /* Espaciado superior para que no se corte el menú */
        .block-container {
            padding-top: 3.2rem;
            padding-bottom: 3rem;
            max-width: 1150px;
        }
        /* Barra superior fija */
        .navbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px 0px 25px 0px;
        }
        .brand {
            display: flex;
            align-items: center;
            gap: 12px;
            font-size: 22px;
            font-weight: 800;
            color: #1A1A1A !important;
            text-decoration: none !important;
        }
        .brand-icon {
            background-color: #E082B4;
            color: white;
            padding: 6px 11px;
            border-radius: 8px;
            font-size: 18px;
        }
        .nav-links {
            display: flex;
            align-items: center;
            gap: 28px;
        }
        .nav-item {
            font-size: 13px;
            font-weight: 700;
            letter-spacing: 2.2px;
            color: #1A1A1A !important;
            text-decoration: none !important;
            transition: color 0.2s;
        }
        .nav-item:hover {
            color: #E082B4 !important;
        }
        .nav-btn-salir {
            background-color: #E082B4;
            color: white !important;
            padding: 9px 24px;
            border-radius: 7px;
            font-size: 14px;
            font-weight: 700;
            text-decoration: none !important;
            box-shadow: 0 4px 10px rgba(224, 130, 180, 0.35);
            transition: background-color 0.2s, transform 0.2s;
        }
        .nav-btn-salir:hover {
            background-color: #C96B9D;
            transform: translateY(-1px);
        }
        /* Banner panorámico */
        .hero-banner img {
            width: 100%;
            height: 270px;
            object-fit: cover;
            border-radius: 14px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.06);
            margin-bottom: 28px;
        }
        /* Tarjetas con imagen 100% clicables */
        a.card-link {
            text-decoration: none !important;
            color: inherit !important;
            display: block;
        }
        .photo-card {
            background-color: #FFFFFF;
            padding: 12px;
            border-radius: 10px;
            box-shadow: 0 6px 18px rgba(0,0,0,0.05);
            text-align: center;
            transition: transform 0.22s ease, box-shadow 0.22s ease;
            cursor: pointer;
        }
        .photo-card:hover {
            transform: translateY(-6px);
            box-shadow: 0 12px 24px rgba(224, 130, 180, 0.25);
        }
        .photo-card img {
            width: 100%;
            height: 205px;
            object-fit: cover;
            border-radius: 6px;
            margin-bottom: 10px;
        }
        .card-title {
            font-weight: 800;
            font-size: 15px;
            color: #1A1A1A;
            margin-bottom: 3px;
        }
        .card-sub {
            font-size: 12px;
            color: #666666;
        }
        /* Botón principal "Comenzar ahora" */
        a.btn-comenzar {
            display: inline-block;
            background-color: #E082B4;
            color: white !important;
            padding: 10px 26px;
            border-radius: 8px;
            font-weight: 700;
            font-size: 14px;
            text-decoration: none !important;
            box-shadow: 0 4px 12px rgba(224, 130, 180, 0.35);
            transition: background-color 0.2s ease, transform 0.2s ease;
        }
        a.btn-comenzar:hover {
            background-color: #C96B9D;
            transform: translateY(-2px);
        }
        /* Botones de cálculo dentro de los métodos */
        div.stButton > button {
            background-color: #E082B4 !important;
            color: white !important;
            border-radius: 8px !important;
            border: none !important;
            padding: 8px 22px !important;
            font-weight: 700 !important;
            box-shadow: 0 4px 10px rgba(224, 130, 180, 0.3);
        }
        div.stButton > button:hover {
            background-color: #C96B9D !important;
            color: white !important;
        }
        
    </style>

    <div class="navbar">
        <a href="/" target="_self" class="brand">
            <div class="brand-icon">∑</div>
            <span>Numérika Lab</span>
        </a>
        <div class="nav-links">
            <a href="/" target="_self" class="nav-item">INICIO</a>
            <a href="/Instrucciones" target="_self" class="nav-item">INSTRUCCIONES</a>
            <a href="/Nosotros" target="_self" class="nav-item">NOSOTROS</a>
            <a href="/?salir=1" target="_self" class="nav-btn-salir">Salir</a>
        </div>
    </div>
    """, unsafe_allow_html=True)
