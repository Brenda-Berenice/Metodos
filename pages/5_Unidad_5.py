import streamlit as st
import pandas as pd
from estilos import cargar_estilos_y_navbar
from nucleo5 import EJEMPLO_POT_A, metodo_potencia_maximo, metodo_potencia_inversa

st.set_page_config(page_title="Unidad 5: Cálculo de valores y vectores propios", layout="wide")
cargar_estilos_y_navbar()

st.markdown("""
<style>
    /* Encabezado estilo editorial */
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
    /* Etiqueta recordatorio con tipografía monoespaciada */
    .pendiente-tag {
        display: inline-block;
        background-color: #FCEEF5;
        color: #C96B9D;
        border: 1.5px dashed #E082B4;
        font-family: 'Courier New', Courier, monospace;
        font-size: 12px;
        font-weight: 800;
        letter-spacing: 1px;
        padding: 4px 10px;
        border-radius: 6px;
        margin-bottom: 10px;
        text-transform: uppercase;
    }
    .unidad-intro {
        color: #555555;
        font-size: 14.5px;
        font-style: italic;
        line-height: 1.65;
        text-align: justify;
        margin-bottom: 24px;
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
        color: #777777;
        font-size: 14.5px;
        font-style: italic;
        line-height: 1.65;
        text-align: justify;
        margin-bottom: 14px;
    }
    /* Colores personalizados para las 2 pestañas (Potencia: Azul, Potencia Inversa: Ámbar) */
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
    /* Cajas reservadas para calculadoras */
    .placeholder-pot {
        background-color: #EBF8FF;
        border: 2px dashed #3182CE;
        border-radius: 12px;
        padding: 32px 20px;
        text-align: center;
        color: #2B6CB0;
        margin-top: 12px;
    }
    .placeholder-potinv {
        background-color: #FFFBEB;
        border: 2px dashed #D97706;
        border-radius: 12px;
        padding: 32px 20px;
        text-align: center;
        color: #B45309;
        margin-top: 12px;
    }
    /* Botones futuros con el color de cada método */
    .st-key-btn_calc_pot div.stButton > button {
        background-color: #2B6CB0 !important;
        box-shadow: 0 4px 10px rgba(43, 108, 176, 0.3) !important;
    }
    .st-key-btn_calc_pot div.stButton > button:hover {
        background-color: #2C5282 !important;
    }
    .st-key-btn_calc_potinv div.stButton > button {
        background-color: #D97706 !important;
        box-shadow: 0 4px 10px rgba(217, 119, 6, 0.3) !important;
    }
    .st-key-btn_calc_potinv div.stButton > button:hover {
        background-color: #B45309 !important;
    }
</style>
""", unsafe_allow_html=True)

# 1. TÍTULO E INTRODUCCIÓN DE LA UNIDAD 5
st.markdown("""
<div class="unidad-tag">Unidad 5.</div>
<div class="unidad-titulo">Cálculo de valores y vectores propios</div>

<div class="pendiente-tag">[ PENDIENTE: INFORMACIÓN INTRODUCTORIA DE LA UNIDAD 5 ]</div>
<p class="unidad-intro">
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
    Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
</p>
""", unsafe_allow_html=True)

# 2. SELECTOR VISUAL DE LOS 2 MÉTODOS DE LA UNIDAD 5
st.markdown("<h3 style='font-size: 18px; font-weight: 800; color: #1A1A1A; margin-bottom: 10px;'>Selecciona un método para ver su fundamento:</h3>", unsafe_allow_html=True)

tab_pot, tab_potinv = st.tabs(["🔹 Método de la Potencia", "🔸 Método de la Potencia Inversa"])

# ==================== TAB 1: MÉTODO DE LA POTENCIA (AZUL) ====================
with tab_pot:
    st.markdown("""
    <div class="unit-card" style="border-left: 5px solid #3182CE;">
        <h3 style="color: #2B6CB0; font-size: 21px; font-weight: 800; margin-top: 0; margin-bottom: 10px;">
            Método de la Potencia
        </h3>
        <div class="pendiente-tag">[ PENDIENTE: AGREGAR EXPLICACIÓN DE CLASE ]</div>
        <p class="theory-text">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore 
            magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
        </p>
        <span style="background-color: #EBF8FF; color: #2B6CB0; padding: 5px 12px; border-radius: 6px; font-size: 13px; font-weight: 700;">
            Valor propio dominante (máximo en magnitud)
        </span>
    </div>
    """, unsafe_allow_html=True)

    st.latex(r"A \cdot \mathbf{v} = \lambda_{\max} \cdot \mathbf{v}")

    st.markdown("<h4 style='color: #2B6CB0; font-weight: 800; margin-top: 10px;'>Calculadora Interactiva — Método de la Potencia</h4>", unsafe_allow_html=True)

    c_dim, c_tol, c_max = st.columns(3)
    n_pot = c_dim.number_input("Tamaño de la matriz (n × n):", min_value=2, max_value=8, value=3, step=1, key="pot_n")
    tol_pot = c_tol.number_input("Tolerancia (%):", value=0.001, format="%.5f", key="pot_tol")
    max_pot = c_max.number_input("Máx. Iteraciones:", value=50, step=1, key="pot_max")

    if n_pot == 3:
        datos_pot = EJEMPLO_POT_A
    else:
        datos_pot = [[4.0 if i == j else 1.0 for j in range(n_pot)] for i in range(n_pot)]

    df_pot = st.data_editor(
        pd.DataFrame(datos_pot, columns=[f"c{j+1}" for j in range(n_pot)], index=[f"f{i+1}" for i in range(n_pot)]),
        use_container_width=True,
        key="editor_pot"
    )

    if st.button("Calcular Valor Propio Máximo", key="btn_calc_pot"):
        try:
            A_in = df_pot.to_numpy(dtype=float).tolist()
            lam, vec, iters, _ = metodo_potencia_maximo(A_in, tol=tol_pot, max_iter=int(max_pot))

            m1, m2 = st.columns(2)
            m1.metric("Valor Propio Máximo (λ_máx)", f"{lam:.6f}")
            m2.metric("Iteraciones Totales", f"{len(iters)}")

            v_str = "[ " + ",  ".join(f"{v:.6f}" for v in vec) + " ]"
            st.success(f"**Vector Propio Correspondiente v:** `{v_str}`")

            filas_tabla = []
            for it in iters:
                y_str = "[ " + ", ".join(f"{v:.4f}" for v in it['y']) + " ]"
                vec_str = "[ " + ", ".join(f"{v:.5f}" for v in it['vector']) + " ]"
                filas_tabla.append([str(it['k']), y_str, f"{it['lambda']:.6f}", vec_str, f"{it['error']:.4f}%"])

            df_res_pot = pd.DataFrame(
                filas_tabla,
                columns=["Iter", "Producto y^(k) = A·x^(k-1)", "Valor Propio Máx (λ)", "Vector Normalizado x^(k)", "Error (%)"]
            )
            st.dataframe(df_res_pot, use_container_width=True, height=300)

        except Exception as e:
            st.error(f"Error en Método de la Potencia: {e}")


# ==================== TAB 2: MÉTODO DE LA POTENCIA INVERSA (ÁMBAR) ====================
with tab_potinv:
    st.markdown("""
    <div class="unit-card" style="border-left: 5px solid #D97706;">
        <h3 style="color: #D97706; font-size: 21px; font-weight: 800; margin-top: 0; margin-bottom: 10px;">
            Método de la Potencia Inversa
        </h3>
        <div class="pendiente-tag">[ PENDIENTE: AGREGAR EXPLICACIÓN DE CLASE ]</div>
        <p class="theory-text">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis aute irure dolor in reprehenderit in voluptate 
            velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident.
        </p>
        <span style="background-color: #FFFBEB; color: #B45309; padding: 5px 12px; border-radius: 6px; font-size: 13px; font-weight: 700;">
            Valor propio mínimo en magnitud
        </span>
    </div>
    """, unsafe_allow_html=True)

    st.latex(r"A^{-1} \cdot \mathbf{v} = \frac{1}{\lambda_{\min}} \cdot \mathbf{v}")

    st.markdown("<h4 style='color: #D97706; font-weight: 800; margin-top: 10px;'>Calculadora Interactiva — Potencia Inversa</h4>", unsafe_allow_html=True)

    c_dim, c_tol, c_max = st.columns(3)
    n_potinv = c_dim.number_input("Tamaño de la matriz (n × n):", min_value=2, max_value=8, value=3, step=1, key="potinv_n")
    tol_potinv = c_tol.number_input("Tolerancia (%):", value=0.001, format="%.5f", key="potinv_tol")
    max_potinv = c_max.number_input("Máx. Iteraciones:", value=50, step=1, key="potinv_max")

    if n_potinv == 3:
        datos_potinv = EJEMPLO_POT_A
    else:
        datos_potinv = [[4.0 if i == j else 1.0 for j in range(n_potinv)] for i in range(n_potinv)]

    df_potinv = st.data_editor(
        pd.DataFrame(datos_potinv, columns=[f"c{j+1}" for j in range(n_potinv)], index=[f"f{i+1}" for i in range(n_potinv)]),
        use_container_width=True,
        key="editor_potinv"
    )

    if st.button("Calcular Valor Propio Mínimo", key="btn_calc_potinv"):
        try:
            A_in = df_potinv.to_numpy(dtype=float).tolist()
            lam, vec, iters, _ = metodo_potencia_inversa(A_in, tol=tol_potinv, max_iter=int(max_potinv))

            m1, m2 = st.columns(2)
            m1.metric("Valor Propio Mínimo (λ_mín)", f"{lam:.6f}")
            m2.metric("Iteraciones Totales", f"{len(iters)}")

            v_str = "[ " + ",  ".join(f"{v:.6f}" for v in vec) + " ]"
            st.success(f"**Vector Propio Correspondiente v:** `{v_str}`")

            filas_tabla = []
            for it in iters:
                vec_str = "[ " + ", ".join(f"{v:.5f}" for v in it['vector']) + " ]"
                filas_tabla.append([str(it['k']), f"{it['mu']:.6f}", f"{it['lambda']:.6f}", vec_str, f"{it['error']:.4f}%"])

            df_res_potinv = pd.DataFrame(
                filas_tabla,
                columns=["Iter", "Factor μ (de A^-1·x)", "Valor Propio Mín (λ = 1/μ)", "Vector Normalizado x^(k)", "Error (%)"]
            )
            st.dataframe(df_res_potinv, use_container_width=True, height=300)

        except Exception as e:
            st.error(f"Error en Potencia Inversa: {e}")


#  3. BOTÓN DE NAVEGACIÓN INFERIOR
st.write("")
st.markdown('<a href="/Unidad_4" target="_self" class="btn-comenzar">Volver a Unidad 4</a>', unsafe_allow_html=True)
