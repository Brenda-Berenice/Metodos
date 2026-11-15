import streamlit as st
import numpy as np
import pandas as pd
import sympy as sp
import matplotlib.pyplot as plt
from estilos import cargar_estilos_y_navbar
from nucleo_matematico import ECUACIONES_CLASE, biseccion, ECUACIONES_CLASE_NEWTON, newton_raphson, ECUACIONES_CLASE_SECANTE, secante


st.set_page_config(page_title="Unidad 2: Ecuaciones de una sola variable", layout="wide")
cargar_estilos_y_navbar()

st.markdown("""
<style>
    /* Encabezado estilo editorial de Canva */
    .unidad-tag {
        color: #B484A0;
        font-size: 20px;
        font-weight: 800;
        margin-bottom: 2px;
    }
    .unidad-titulo {
        color: #1A1A1A;
        font-size: 32px;
        font-weight: 800;
        margin-top: 0px;
        margin-bottom: 18px;
        line-height: 1.2;
    }
    .unidad-intro {
        color: #333333;
        font-size: 14.5px;
        line-height: 1.65;
        text-align: justify;
        margin-bottom: 14px;
    }
    /* Tarjeta blanca para cada método */
    .unit-card {
        background-color: #FFFFFF;
        padding: 26px 30px;
        border-radius: 16px;
        box-shadow: 0 6px 18px rgba(0,0,0,0.04);
        margin-top: 10px;
        margin-bottom: 20px;
    }
    .theory-text {
        color: #444444;
        font-size: 14.5px;
        line-height: 1.65;
        text-align: justify;
        margin-bottom: 0;
    }
    /* Colores personalizados para las pestañas */
    button[data-baseweb="tab"]:nth-child(1) p {
        color: #2B6CB0 !important;
        font-weight: 700 !important;
        font-size: 15px !important;
    }
    button[data-baseweb="tab"]:nth-child(2) p {
        color: #D97706 !important;
        font-weight: 700 !important;
        font-size: 15px !important;
    }
    button[data-baseweb="tab"]:nth-child(3) p {
        color: #9B2C2C !important;
        font-weight: 700 !important;
        font-size: 15px !important;
    }
    /* Cajas reservadas combinadas con el color de cada método */
    .placeholder-bis {
        background-color: #EBF8FF;
        border: 2px dashed #3182CE;
        border-radius: 12px;
        padding: 32px 20px;
        text-align: center;
        color: #2B6CB0;
        margin-top: 12px;
    }
    .placeholder-new {
        background-color: #FFFBEB;
        border: 2px dashed #D97706;
        border-radius: 12px;
        padding: 32px 20px;
        text-align: center;
        color: #B45309;
        margin-top: 12px;
    }
    .placeholder-sec {
        background-color: #FFF5F5;
        border: 2px dashed #9B2C2C;
        border-radius: 12px;
        padding: 32px 20px;
        text-align: center;
        color: #9B2C2C;
        margin-top: 12px;
    }
        /* Botón Azul Bisección */
    .st-key-btn_calc_bis div.stButton > button {
        background-color: #2B6CB0 !important;
        box-shadow: 0 4px 10px rgba(43, 108, 176, 0.3) !important;
    }
    .st-key-btn_calc_bis div.stButton > button:hover {
        background-color: #2C5282 !important;
    }

    /* Botón Ámbar Newton */
    .st-key-btn_calc_new div.stButton > button {
        background-color: #D97706 !important;
        box-shadow: 0 4px 10px rgba(217, 119, 6, 0.3) !important;
    }
    .st-key-btn_calc_new div.stButton > button:hover {
        background-color: #B45309 !important;
    }

    /* Botón Vino Secante */
    .st-key-btn_calc_sec div.stButton > button {
        background-color: #9B2C2C !important;
        box-shadow: 0 4px 10px rgba(155, 44, 44, 0.3) !important;
    }
    .st-key-btn_calc_sec div.stButton > button:hover {
        background-color: #742A2A !important;
    }

</style>
""", unsafe_allow_html=True)

# 1. TÍTULO E INTRODUCCIÓN DE LA UNIDAD 2 (Exacto a tu plantilla)
st.markdown("""
<div class="unidad-tag">Unidad 2.</div>
<div class="unidad-titulo">Solución numérica de ecuaciones de una sola variable</div>

<p class="unidad-intro">
    La solución numérica de ecuaciones se obtiene mediante un método numérico. Un método numérico se utiliza para resolver un 
    problema de valor inicial consistiendo en un procedimiento que conduce a soluciones aproximadas en puntos especiales, usando 
    solamente las operaciones de adición, sustracción, multiplicación, división y cálculo de funciones.
</p>
<p class="unidad-intro" style="margin-bottom: 28px;">
    Los métodos que se presentan reciben el nombre genérico de aproximaciones sucesivas, los cuales desarrollan su convergencia 
    mediante la aplicación de una fórmula de recurrencia. Se les da ese nombre pues a partir de una primer aproximación, se obtiene 
    otra aproximación mejor, en general más cercana a la solución.
</p>
""", unsafe_allow_html=True)

# 2. SELECTOR VISUAL DE LOS 3 MÉTODOS (Sin emojis y con color propio)
st.markdown("<h3 style='font-size: 18px; font-weight: 800; color: #1A1A1A; margin-bottom: 10px;'>Selecciona un método para ver su fundamento:</h3>", unsafe_allow_html=True)

tab_bis, tab_new, tab_sec = st.tabs(["🔹 Método de Bisección", "🔸 Método de Newton", "🔺 Método de la Secante"])

# ==================== TAB 1: BISECCIÓN (AZUL) ====================
with tab_bis:
    st.markdown("""
    <div class="unit-card" style="border-left: 5px solid #3182CE;">
        <h3 style="color: #2B6CB0; font-size: 21px; font-weight: 800; margin-top: 0; margin-bottom: 12px;">
            Método de Bisección
        </h3>
        <p class="theory-text" style="margin-bottom: 12px;">
            Se basa en el teorema de cambio de signo. Se proponen dos valores <i>a</i> y <i>b</i> para el intervalo 
            cerrado <i>[a, b]</i>. Si se cumple que <i>f(a)</i> y <i>f(b)</i> tienen signos diferentes, sin importar 
            cuál de ambos es positivo o negativo, entonces dentro de ese intervalo existe al menos una raíz real.
        </p>
        <p class="theory-text" style="margin-bottom: 14px;">
            El método consiste en evaluar la función en el punto medio del intervalo <i>f(x)</i>. Si la función en 
            el valor intermedio <i>f(x)</i> es del mismo signo que la función evaluada en <i>f(a)</i> o <i>f(b)</i>, 
            entonces se sustituye por el valor con el mismo signo, de tal manera que el intervalo se reduce a 
            <i>[x, b]</i> o <i>[a, x]</i> dependiendo cuál fue el valor que se reemplazó. Y se repite el proceso a 
            partir del nuevo intervalo, esto hasta que la función <i>f(x)</i> sea cero o casi nula.
        </p>
        <span style="background-color: #EBF8FF; color: #2B6CB0; padding: 5px 12px; border-radius: 6px; font-size: 13px; font-weight: 700;">
            Convergencia lineal
        </span>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<h4 style='color: #2B6CB0; font-weight: 800; margin-top: 10px;'>Calculadora Interactiva — Bisección</h4>", unsafe_allow_html=True)
    
    opciones_eq = [f"{eq} = 0" for eq, _, _ in ECUACIONES_CLASE] + ["Escribir ecuación personalizada..."]
    seleccion = st.selectbox("Ecuaciones vistas en clase:", opciones_eq, key="bis_select")

    if seleccion == "Escribir ecuación personalizada...":
        eq_default, a_default, b_default = "x^3 - 2*x - 5", 2.0, 3.0
    else:
        idx = opciones_eq.index(seleccion)
        eq_default, a_default, b_default = ECUACIONES_CLASE[idx]

    c1, c2, c3, c4, c5 = st.columns([1.8, 1, 1, 1, 1])
    expr_input = c1.text_input("Función f(x):", value=eq_default, key="bis_fx")
    a_input = c2.number_input("Valor inicial a:", value=float(a_default), format="%.4f", key="bis_a")
    b_input = c3.number_input("Extremo b:", value=float(b_default), format="%.4f", key="bis_b")
    tol_input = c4.number_input("Tolerancia (%):", value=0.001, format="%.5f", key="bis_tol")
    max_input = c5.number_input("Máx. Iteraciones:", value=50, step=1, key="bis_max")

    if st.button("Calcular Raíz por Bisección", key="btn_calc_bis"):
        try:
            iteraciones, resumen = biseccion(expr_input, a_input, b_input, tol_input, int(max_input))
            
            m1, m2, m3, m4 = st.columns(4)
            m1.metric("Raíz Aproximada (xr)", f"{resumen['raiz']:.6f}")
            m2.metric("f(xr)", f"{resumen['f_raiz']:.2e}")
            m3.metric("Iteraciones", f"{resumen['iteraciones_totales']}")
            m4.metric("Error Final (%)", f"{resumen['error_final']:.5f}%")

            col_tabla, col_graf = st.columns([1.4, 1], gap="medium")

            with col_tabla:
                st.markdown("**Tabla de Iteraciones**")
                df_res = pd.DataFrame(iteraciones)
                df_res.columns = ["Iter", "a", "b", "xr", "f(a)", "f(b)", "f(xr)", "Error (%)"]
                st.dataframe(df_res, use_container_width=True, height=320)

            with col_graf:
                st.markdown("**Gráfica de la Función**")
                x_sym = sp.Symbol('x')
                f_num = sp.lambdify(x_sym, sp.sympify(expr_input.replace("^", "**")), "numpy")
                margen = max(abs(resumen['b_usado'] - resumen['a_usado']) * 0.5, 1.0)
                x_vals = np.linspace(resumen['a_usado'] - margen, resumen['b_usado'] + margen, 300)
                y_vals = f_num(x_vals)

                fig, ax = plt.subplots(figsize=(5, 3.6))
                fig.patch.set_facecolor('#FFFFFF')
                ax.plot(x_vals, y_vals, color="#2B6CB0", linewidth=2, label=f"f(x) = {expr_input}")
                ax.axhline(0, color="#888888", linestyle="--", linewidth=1)
                ax.scatter([resumen['raiz']], [resumen['f_raiz']], color="#E082B4", s=90, zorder=5, label=f"Raíz ≈ {resumen['raiz']:.5f}")
                ax.grid(True, linestyle=":", alpha=0.6)
                ax.legend(fontsize=9)
                st.pyplot(fig)

        except Exception as e:
            st.error(f"Error en el cálculo: {e}")


# ==================== TAB 2: NEWTON (NARANJA) ====================
with tab_new:
    st.markdown("""
    <div class="unit-card" style="border-left: 5px solid #D97706;">
        <h3 style="color: #D97706; font-size: 21px; font-weight: 800; margin-top: 0; margin-bottom: 12px;">
            Método de Newton
        </h3>
        <p class="theory-text" style="margin-bottom: 14px;">
            Dado un punto <i>x</i> propuesto, se puede trazar una recta tangente desde el punto <i>[x, f(x)]</i> de la curva. 
            Por lo común, el punto donde esta tangente cruza al eje <i>x</i> representa una aproximación mejorada de la raíz.
        </p>
        <span style="background-color: #FFFBEB; color: #B45309; padding: 5px 12px; border-radius: 6px; font-size: 13px; font-weight: 700;">
            Convergencia cuadrática
        </span>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<h4 style='color: #D97706; font-weight: 800; margin-top: 10px;'>Calculadora Interactiva — Newton-Raphson</h4>", unsafe_allow_html=True)

    opciones_new = [f"{eq} = 0" for eq, _, _ in ECUACIONES_CLASE_NEWTON] + ["Escribir ecuación personalizada..."]
    sel_new = st.selectbox("Ecuaciones vistas en clase:", opciones_new, key="new_select")

    if sel_new == "Escribir ecuación personalizada...":
        eq_new_def, df_new_def, x0_new_def = "x^3 - 2*x - 5", "3*x^2 - 2", 2.0
    else:
        idx_n = opciones_new.index(sel_new)
        eq_new_def, df_new_def, x0_new_def = ECUACIONES_CLASE_NEWTON[idx_n]

    c1, c2, c3, c4, c5 = st.columns([1.5, 1.5, 1, 1, 1])
    expr_new_in = c1.text_input("Función f(x):", value=eq_new_def, key="new_fx")
    df_new_in = c2.text_input("Derivada f'(x) (opcional):", value=df_new_def, key="new_dfx")
    x0_new_in = c3.number_input("Valor inicial x0:", value=float(x0_new_def), format="%.4f", key="new_x0")
    tol_new_in = c4.number_input("Tolerancia (%):", value=0.0001, format="%.5f", key="new_tol")
    max_new_in = c5.number_input("Máx. Iteraciones:", value=50, step=1, key="new_max")

    if st.button("Calcular Raíz por Newton", key="btn_calc_new"):
        try:
            iteraciones, resumen = newton_raphson(expr_new_in, x0_new_in, df_new_in, tol_new_in, int(max_new_in))

            m1, m2, m3, m4 = st.columns(4)
            m1.metric("Raíz Aproximada (x)", f"{resumen['raiz']:.6f}")
            m2.metric("f(x)", f"{resumen['f_raiz']:.2e}")
            m3.metric("Iteraciones", f"{resumen['iteraciones_totales']}")
            m4.metric("Error Final (%)", f"{resumen['error_final']:.5f}%")

            col_tabla, col_graf = st.columns([1.4, 1], gap="medium")

            with col_tabla:
                st.markdown("**Tabla de Iteraciones**")
                df_res = pd.DataFrame(iteraciones)
                df_res.columns = ["Iter", "xi", "f(xi)", "f'(xi)", "x_{i+1}", "Error (%)"]
                st.dataframe(df_res, use_container_width=True, height=320)

            with col_graf:
                st.markdown("**Gráfica de la Función**")
                x_sym = sp.Symbol('x')
                f_num = sp.lambdify(x_sym, sp.sympify(expr_new_in.replace("^", "**")), "numpy")
                raiz = resumen['raiz']
                x_vals = np.linspace(raiz - 2.5, raiz + 2.5, 300)
                y_vals = f_num(x_vals)

                fig, ax = plt.subplots(figsize=(5, 3.6))
                fig.patch.set_facecolor('#FFFFFF')
                ax.plot(x_vals, y_vals, color="#D97706", linewidth=2, label=f"f(x) = {expr_new_in}")
                ax.axhline(0, color="#888888", linestyle="--", linewidth=1)
                ax.scatter([raiz], [resumen['f_raiz']], color="#E082B4", s=90, zorder=5, label=f"Raíz ≈ {raiz:.5f}")
                ax.grid(True, linestyle=":", alpha=0.6)
                ax.legend(fontsize=9)
                st.pyplot(fig)

        except Exception as e:
            st.error(f"Error en el cálculo: {e}")


# ==================== TAB 3: SECANTE (VINO / ROJO OSCURO) ====================
with tab_sec:
    st.markdown("""
    <div class="unit-card" style="border-left: 5px solid #9B2C2C;">
        <h3 style="color: #9B2C2C; font-size: 21px; font-weight: 800; margin-top: 0; margin-bottom: 12px;">
            Método de la Secante
        </h3>
        <p class="theory-text" style="margin-bottom: 12px;">
            El método de la secante es, esencialmente, una modificación del método convencional de Newton con la derivada 
            reemplazada por una expresión diferente. Esto es ventajoso si la función es difícil de derivar.
        </p>
        <p class="theory-text" style="margin-bottom: 12px;">
            Reemplazando la derivada por el concepto elemental de la tangente.
        </p>
        <p class="theory-text" style="margin-bottom: 14;">
            Dados dos valores <i>x<sub>1</sub></i> y <i>x<sub>2</sub></i>, entonces se calcula <i>f(x<sub>1</sub>)</i> y 
            <i>f(x<sub>2</sub>)</i>, de tal manera que las iteraciones siguientes se calculen con la ecuación elemental de tangente.
        </p>
        <span style="background-color: #FFF5F5; color: #9B2C2C; padding: 5px 12px; border-radius: 6px; font-size: 13px; font-weight: 700;">
            Convergencia superlineal
        </span>
    </div>
    """, unsafe_allow_html=True)

    
    st.markdown("<h4 style='color: #9B2C2C; font-weight: 800; margin-top: 10px;'>Calculadora Interactiva — Método de la Secante</h4>", unsafe_allow_html=True)

    opciones_sec = [f"{eq} = 0" for eq, _, _ in ECUACIONES_CLASE_SECANTE] + ["Escribir ecuación personalizada..."]
    sel_sec = st.selectbox("Ecuaciones vistas en clase:", opciones_sec, key="sec_select")

    if sel_sec == "Escribir ecuación personalizada...":
        eq_sec_def, x0_sec_def, x1_sec_def = "exp(-x^2) - x", 0.0, 1.0
    else:
        idx_s = opciones_sec.index(sel_sec)
        eq_sec_def, x0_sec_def, x1_sec_def = ECUACIONES_CLASE_SECANTE[idx_s]

    c1, c2, c3, c4, c5 = st.columns([1.8, 1, 1, 1, 1])
    expr_sec_in = c1.text_input("Función f(x):", value=eq_sec_def, key="sec_fx")
    x0_sec_in = c2.number_input("Primer valor x0:", value=float(x0_sec_def), format="%.4f", key="sec_x0")
    x1_sec_in = c3.number_input("Segundo valor x1:", value=float(x1_sec_def), format="%.4f", key="sec_x1")
    tol_sec_in = c4.number_input("Tolerancia (%):", value=0.0001, format="%.5f", key="sec_tol")
    max_sec_in = c5.number_input("Máx. Iteraciones:", value=50, step=1, key="sec_max")

    if st.button("Calcular Raíz por Secante", key="btn_calc_sec"):
        try:
            iteraciones, resumen = secante(expr_sec_in, x0_sec_in, x1_sec_in, tol_sec_in, int(max_sec_in))

            m1, m2, m3, m4 = st.columns(4)
            m1.metric("Raíz Aproximada (x)", f"{resumen['raiz']:.6f}")
            m2.metric("f(x)", f"{resumen['f_raiz']:.2e}")
            m3.metric("Iteraciones", f"{resumen['iteraciones_totales']}")
            m4.metric("Error Final (%)", f"{resumen['error_final']:.5f}%")

            col_tabla, col_graf = st.columns([1.4, 1], gap="medium")

            with col_tabla:
                st.markdown("**Tabla de Iteraciones**")
                df_res = pd.DataFrame(iteraciones)
                df_res.columns = ["Iter", "x_{i-1}", "x_i", "f(x_{i-1})", "f(x_i)", "x_{i+1}", "Error (%)"]
                st.dataframe(df_res, use_container_width=True, height=320)

            with col_graf:
                st.markdown("**Gráfica de la Función**")
                x_sym = sp.Symbol('x')
                f_num = sp.lambdify(x_sym, sp.sympify(expr_sec_in.replace("^", "**")), "numpy")
                raiz = resumen['raiz']
                x_vals = np.linspace(raiz - 2.5, raiz + 2.5, 300)
                y_vals = f_num(x_vals)

                fig, ax = plt.subplots(figsize=(5, 3.6))
                fig.patch.set_facecolor('#FFFFFF')
                ax.plot(x_vals, y_vals, color="#9B2C2C", linewidth=2, label=f"f(x) = {expr_sec_in}")
                ax.axhline(0, color="#888888", linestyle="--", linewidth=1)
                ax.scatter([raiz], [resumen['f_raiz']], color="#E082B4", s=90, zorder=5, label=f"Raíz ≈ {raiz:.5f}")
                ax.grid(True, linestyle=":", alpha=0.6)
                ax.legend(fontsize=9)
                st.pyplot(fig)

        except Exception as e:
            st.error(f"Error en el cálculo: {e}")


# 3. BOTONES DE NAVEGACIÓN ENTRE UNIDADES
st.write("")
col_prev, col_space, col_next = st.columns([1, 2, 1])
with col_prev:
    st.markdown('<a href="/Introduccion" target="_self" class="btn-comenzar">Volver a Introducción</a>', unsafe_allow_html=True)
with col_next:
    st.markdown('<div style="text-align: right;"><a href="/Unidad_3" target="_self" class="btn-comenzar">Ir a Unidad 3</a></div>', unsafe_allow_html=True)
