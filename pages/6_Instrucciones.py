import streamlit as st
from estilos import cargar_estilos_y_navbar

st.set_page_config(page_title="Instrucciones", page_icon="📖", layout="wide")
cargar_estilos_y_navbar()

st.markdown("<h1 style='font-weight: 800;'>📖 Instrucciones de Uso</h1>", unsafe_allow_html=True)
st.write("Sigue esta guía rápida para escribir funciones y matrices correctamente dentro de la plataforma:")

col1, col2 = st.columns(2, gap="large")

with col1:
    st.info("### 1. Cómo escribir ecuaciones $f(x)$")
    st.markdown("""
    Para los métodos de **Ecuaciones No Lineales**, utiliza sintaxis matemática estándar de Python:
    * **Potencias:** Usa doble asterisco `**` (Ejemplo: $x^3$ se escribe `x**3`).
    * **Multiplicación:** Usa siempre `*` (Ejemplo: $2x$ se escribe `2*x`).
    * **Funciones especiales:** Puedes usar `sin(x)`, `cos(x)`, `tan(x)`, `exp(x)` para $e^x$, y `log(x)` para logaritmo natural.
    * **Tolerancia:** Escribe el margen de error deseado en decimal (Ejemplo: `0.0001`).
    """)

with col2:
    st.success("### 2. Cómo ingresar matrices $Ax = b$")
    st.markdown("""
    Para **Sistemas Lineales** y **Valores Propios**:
    * **Tamaño de la matriz:** Selecciona primero la dimensión $n \\times n$ deseada.
    * **Valores:** Escribe los coeficientes numéricos directamente en cada celda de la tabla interactiva.
    * **Recomendación para métodos iterativos:** Para que **Jacobi** y **Gauss-Seidel** converjan rápido, procura que la matriz sea diagonalmente dominante.
    """)
