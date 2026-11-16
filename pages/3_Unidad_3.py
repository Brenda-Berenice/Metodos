import streamlit as st
import pandas as pd
from estilos import cargar_estilos_y_navbar, imagen_a_base64
from nucleo3 import (
    EJEMPLO_GJ_CLASE_A,
    EJEMPLO_GJ_CLASE_B,
    EJEMPLO_GJ_A,
    EJEMPLO_GJ_B,
    gauss_jordan,
    EJEMPLO_CLASE_3_A,
    EJEMPLO_CLASE_3_B,
    EJEMPLO_ITER_A,
    EJEMPLO_ITER_B,
    reordenar_diagonal_dominante,
    metodo_gauss_seidel,
    EJEMPLO_JAC_A,
    EJEMPLO_JAC_B,
    metodo_jacobi
)

st.set_page_config(page_title="Unidad 3: Sistemas de Ecuaciones Lineales", layout="wide")
cargar_estilos_y_navbar()

# Cargar la imagen PNG del sistema de ecuaciones
img_sistema = imagen_a_base64("imagenes/sistema_u3.png")

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
    .unidad-intro {
        color: #333333;
        font-size: 14.5px;
        line-height: 1.65;
        text-align: justify;
        margin-bottom: 14px;
    }
    .sistema-img-box {
        text-align: center;
        margin: 18px 0px;
    }
    .sistema-img-box img {
        max-width: 480px;
        width: 100%;
        border-radius: 10px;
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
    /* Colores personalizados para las 3 pestañas */
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
    /* Botones con el color de cada método */
    .st-key-btn_calc_gj div.stButton > button {
        background-color: #2B6CB0 !important;
        box-shadow: 0 4px 10px rgba(43, 108, 176, 0.3) !important;
    }
    .st-key-btn_calc_gj div.stButton > button:hover {
        background-color: #2C5282 !important;
    }
    .st-key-btn_calc_gs div.stButton > button {
        background-color: #D97706 !important;
        box-shadow: 0 4px 10px rgba(217, 119, 6, 0.3) !important;
    }
    .st-key-btn_calc_gs div.stButton > button:hover {
        background-color: #B45309 !important;
    }
    .st-key-btn_calc_jac div.stButton > button {
        background-color: #9B2C2C !important;
        box-shadow: 0 4px 10px rgba(155, 44, 44, 0.3) !important;
    }
    .st-key-btn_calc_jac div.stButton > button:hover {
        background-color: #742A2A !important;
    }

    /* PENDIENTE */
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
</style>
""", unsafe_allow_html=True)

# 1. TÍTULO E INTRODUCCIÓN DE LA UNIDAD 3 (Con tu texto e imagen PNG)
st.markdown(f"""
<div class="unidad-tag">Unidad 3.</div>
<div class="unidad-titulo">Solución de sistemas de ecuaciones lineales</div>

<p class="unidad-intro">
    Dado un sistema:
</p>

<div class="sistema-img-box">
    <img src="{img_sistema}" alt="Sistema de ecuaciones lineales">
</div>

<p class="unidad-intro" style="margin-bottom: 28px;">
    Donde <i>x<sub>1</sub>, ..., x<sub>n</sub></i> son incógnitas, los números <i>a<sub>ij</sub></i> son los coeficientes 
    del sistema y <i>b<sub>1</sub>, ..., b<sub>n</sub></i> son los términos independientes. El problema consiste en encontrar 
    los valores desconocidos de las variables <i>x<sub>1</sub>, x<sub>2</sub>, ..., x<sub>n</sub></i> que satisfacen todas las ecuaciones.
</p>
""", unsafe_allow_html=True)

# 2. SELECTOR VISUAL DE LOS 3 MÉTODOS DE LA UNIDAD 3
st.markdown("<h3 style='font-size: 18px; font-weight: 800; color: #1A1A1A; margin-bottom: 10px;'>Selecciona un método para ver su fundamento:</h3>", unsafe_allow_html=True)

tab_gj, tab_gs, tab_jac = st.tabs(["🔹 Método de Gauss-Jordan", "🔸 Método de Gauss-Seidel", "🔺 Método de Jacobi"])

# ==================== TAB 1: GAUSS-JORDAN (AZUL) ====================
with tab_gj:
    st.markdown("""
    <div class="unit-card" style="border-left: 5px solid #3182CE;">
        <h3 style="color: #2B6CB0; font-size: 21px; font-weight: 800; margin-top: 0; margin-bottom: 10px;">
            Método de Gauss-Jordan
        </h3>
        <div class="pendiente-tag">[ PENDIENTE: AGREGAR EXPLICACIÓN DE CLASE ]</div>
        <p class="theory-text" style="margin-bottom: 14px; color: #777777; font-style: italic;">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore 
            magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
        </p>
        <span style="background-color: #EBF8FF; color: #2B6CB0; padding: 5px 12px; border-radius: 6px; font-size: 13px; font-weight: 700;">
            Método directo
        </span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<h4 style='color: #2B6CB0; font-weight: 800; margin-top: 10px;'>Calculadora Interactiva — Gauss-Jordan</h4>", unsafe_allow_html=True)

    col_ej, col_dim, col_info = st.columns([1.3, 1, 1.7])
    ej_gj = col_ej.selectbox(
        "Ejercicio precargado:",
        ["Ejercicio de clase (4×4)", "Ejercicio del equipo (3×3)", "Personalizado"],
        key="gj_ej_sel"
    )

    if ej_gj == "Ejercicio de clase (4×4)":
        n_gj = col_dim.number_input("Tamaño del sistema (n × n):", min_value=2, max_value=8, value=4, step=1, key="gj_n_4")
        datos_init = [EJEMPLO_GJ_CLASE_A[i] + [EJEMPLO_GJ_CLASE_B[i]] for i in range(4)] if n_gj == 4 else [[1.0 if i == j else 0.0 for j in range(n_gj)] + [1.0] for i in range(n_gj)]
    elif ej_gj == "Ejercicio del equipo (3×3)":
        n_gj = col_dim.number_input("Tamaño del sistema (n × n):", min_value=2, max_value=8, value=3, step=1, key="gj_n_3")
        datos_init = [EJEMPLO_GJ_A[i] + [EJEMPLO_GJ_B[i]] for i in range(3)] if n_gj == 3 else [[1.0 if i == j else 0.0 for j in range(n_gj)] + [1.0] for i in range(n_gj)]
    else:
        n_gj = col_dim.number_input("Tamaño del sistema (n × n):", min_value=2, max_value=8, value=3, step=1, key="gj_n_p")
        datos_init = [[1.0 if i == j else 0.0 for j in range(n_gj)] + [1.0] for i in range(n_gj)]

    col_info.info("Edita los coeficientes de la matriz **A** y los términos independientes **b** directamente en la tabla.")

    # Nombres de variables según el tamaño (x, y, z para 3; v, x, y, z para 4)
    if n_gj == 3:
        nombres_vars_gj = ["x", "y", "z"]
    elif n_gj == 4:
        nombres_vars_gj = ["v", "x", "y", "z"]
    else:
        nombres_vars_gj = [f"x{j+1}" for j in range(n_gj)]

    columnas_gj = nombres_vars_gj + ["b"]
    filas_gj = [f"R{i+1}" for i in range(n_gj)]
    df_matriz_gj = pd.DataFrame(datos_init, columns=columnas_gj, index=filas_gj)

    df_editado_gj = st.data_editor(df_matriz_gj, use_container_width=True, key="editor_gj")

    if st.button("Resolver por Gauss-Jordan", key="btn_calc_gj"):
        try:
            matriz_np = df_editado_gj.to_numpy(dtype=float)
            A_in = matriz_np[:, :-1].tolist()
            b_in = matriz_np[:, -1].tolist()

            x_sol, pasos = gauss_jordan(A_in, b_in)

            st.markdown("**Vector Solución Obtenido:**")
            cols_sol = st.columns(len(x_sol))
            for idx, val in enumerate(x_sol):
                cols_sol[idx].metric(nombres_vars_gj[idx], f"{val:.4f}")

            with st.expander("Ver desarrollo matricial paso a paso (R1, R2...) y comprobación", expanded=True):
                st.code("\n".join(pasos), language="text")

        except Exception as e:
            st.error(f"Error en Gauss-Jordan: {e}")


# ==================== TAB 2: GAUSS-SEIDEL (ÁMBAR) ====================
with tab_gs:
    st.markdown("""
    <div class="unit-card" style="border-left: 5px solid #D97706;">
        <h3 style="color: #D97706; font-size: 21px; font-weight: 800; margin-top: 0; margin-bottom: 10px;">
            Método de Gauss-Seidel
        </h3>
        <div class="pendiente-tag">[ PENDIENTE: AGREGAR EXPLICACIÓN DE CLASE ]</div>
        <p class="theory-text" style="margin-bottom: 14px; color: #777777; font-style: italic;">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis aute irure dolor in reprehenderit in voluptate 
            velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident.
        </p>
        <span style="background-color: #FFFBEB; color: #B45309; padding: 5px 12px; border-radius: 6px; font-size: 13px; font-weight: 700;">
            Método iterativo
        </span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<h4 style='color: #D97706; font-weight: 800; margin-top: 10px;'>Calculadora Interactiva — Gauss-Seidel</h4>", unsafe_allow_html=True)

    c_ej_gs, c_dim, c_tol, c_max = st.columns([1.3, 1, 1, 1])
    ej_gs = c_ej_gs.selectbox(
        "Ejercicio precargado:",
        ["Ejercicio de clase (3×3)", "Ejercicio del equipo (3×3)", "Personalizado"],
        key="gs_ej_sel"
    )
    n_gs = c_dim.number_input("Tamaño (n × n):", min_value=2, max_value=8, value=3, step=1, key="gs_n")
    tol_gs = c_tol.number_input("Tolerancia (%):", value=0.0001, format="%.5f", key="gs_tol")
    max_gs = c_max.number_input("Máx. Iteraciones:", value=50, step=1, key="gs_max")

    if n_gs == 3 and ej_gs == "Ejercicio de clase (3×3)":
        datos_init_gs = [EJEMPLO_CLASE_3_A[i] + [EJEMPLO_CLASE_3_B[i]] for i in range(3)]
    elif n_gs == 3 and ej_gs == "Ejercicio del equipo (3×3)":
        datos_init_gs = [EJEMPLO_ITER_A[i] + [EJEMPLO_ITER_B[i]] for i in range(3)]
    else:
        datos_init_gs = [[5.0 if i == j else 1.0 for j in range(n_gs)] + [10.0] for i in range(n_gs)]

    nombres_vars_gs = ["x", "y", "z"] if n_gs == 3 else (["v", "x", "y", "z"] if n_gs == 4 else [f"x{j+1}" for j in range(n_gs)])
    columnas_gs = nombres_vars_gs + ["b"]
    filas_gs = [f"Ec. {i+1}" for i in range(n_gs)]
    df_matriz_gs = pd.DataFrame(datos_init_gs, columns=columnas_gs, index=filas_gs)

    df_editado_gs = st.data_editor(df_matriz_gs, use_container_width=True, key="editor_gs")

    if st.button("Resolver por Gauss-Seidel", key="btn_calc_gs"):
        try:
            matriz_np = df_editado_gs.to_numpy(dtype=float)
            A_in = matriz_np[:, :-1].tolist()
            b_in = matriz_np[:, -1].tolist()
            n_vars = len(A_in)

            _, _, es_dom, msg_dom = reordenar_diagonal_dominante(A_in, b_in)
            if es_dom:
                st.success(msg_dom)
            else:
                st.warning(msg_dom)

            iteraciones, x_final, conv = metodo_gauss_seidel(A_in, b_in, tol=tol_gs, max_iter=int(max_gs), auto_reordenar=True)

            st.markdown(f"**Vector Solución (en {len(iteraciones) - 1} iteraciones):**")
            cols_sol = st.columns(n_vars)
            for idx, val in enumerate(x_final):
                cols_sol[idx].metric(nombres_vars_gs[idx], f"{val:.4f}")

            # Tabla exacta con n = 0, 1, 2...
            filas_tabla = []
            for it in iteraciones:
                err_str = "-" if it['n'] == 0 else f"{it['error_rel']:.5f}%"
                filas_tabla.append([str(it['n'])] + [f"{val:.4f}" for val in it['x']] + [err_str])

            cols_tabla = ["n"] + nombres_vars_gs + ["Error Máx (%)"]
            df_tabla_gs = pd.DataFrame(filas_tabla, columns=cols_tabla)
            st.dataframe(df_tabla_gs, use_container_width=True, height=300, hide_index=True)

        except Exception as e:
            st.error(f"Error en Gauss-Seidel: {e}")

# ==================== TAB 3: JACOBI (VINO) ====================
with tab_jac:
    st.markdown("""
    <div class="unit-card" style="border-left: 5px solid #9B2C2C;">
        <h3 style="color: #9B2C2C; font-size: 21px; font-weight: 800; margin-top: 0; margin-bottom: 10px;">
            Método de Jacobi
        </h3>
        <div class="pendiente-tag">[ PENDIENTE: AGREGAR EXPLICACIÓN DE CLASE ]</div>
        <p class="theory-text" style="margin-bottom: 14px; color: #777777; font-style: italic;">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nemo enim ipsam voluptatem quia voluptas sit aspernatur 
            aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt.
        </p>
        <span style="background-color: #FFF5F5; color: #9B2C2C; padding: 5px 12px; border-radius: 6px; font-size: 13px; font-weight: 700;">
            Método iterativo
        </span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<h4 style='color: #9B2C2C; font-weight: 800; margin-top: 10px;'>Calculadora Interactiva — Jacobi</h4>", unsafe_allow_html=True)

    c_ej_jac, c_dim, c_tol, c_max = st.columns([1.3, 1, 1, 1])
    ej_jac = c_ej_jac.selectbox(
        "Ejercicio precargado:",
        ["Ejercicio de clase (3×3)", "Ejercicio del equipo (3×3)", "Personalizado"],
        key="jac_ej_sel"
    )
    n_jac = c_dim.number_input("Tamaño (n × n):", min_value=2, max_value=8, value=3, step=1, key="jac_n")
    tol_jac = c_tol.number_input("Tolerancia (%):", value=0.0001, format="%.5f", key="jac_tol")
    max_jac = c_max.number_input("Máx. Iteraciones:", value=50, step=1, key="jac_max")

    if n_jac == 3 and ej_jac == "Ejercicio de clase (3×3)":
        datos_init_jac = [EJEMPLO_CLASE_3_A[i] + [EJEMPLO_CLASE_3_B[i]] for i in range(3)]
    elif n_jac == 3 and ej_jac == "Ejercicio del equipo (3×3)":
        datos_init_jac = [EJEMPLO_JAC_A[i] + [EJEMPLO_JAC_B[i]] for i in range(3)]
    else:
        datos_init_jac = [[10.0 if i == j else 1.0 for j in range(n_jac)] + [12.0] for i in range(n_jac)]

    nombres_vars_jac = ["x", "y", "z"] if n_jac == 3 else (["v", "x", "y", "z"] if n_jac == 4 else [f"x{j+1}" for j in range(n_jac)])
    columnas_jac = nombres_vars_jac + ["b"]
    filas_jac = [f"Ec. {i+1}" for i in range(n_jac)]
    df_matriz_jac = pd.DataFrame(datos_init_jac, columns=columnas_jac, index=filas_jac)

    df_editado_jac = st.data_editor(df_matriz_jac, use_container_width=True, key="editor_jac")

    if st.button("Resolver por Jacobi", key="btn_calc_jac"):
        try:
            matriz_np = df_editado_jac.to_numpy(dtype=float)
            A_in = matriz_np[:, :-1].tolist()
            b_in = matriz_np[:, -1].tolist()
            n_vars = len(A_in)

            _, _, es_dom, msg_dom = reordenar_diagonal_dominante(A_in, b_in)
            if es_dom:
                st.success(msg_dom)
            else:
                st.warning(msg_dom)

            iteraciones, x_final, conv = metodo_jacobi(A_in, b_in, tol=tol_jac, max_iter=int(max_jac), auto_reordenar=True)

            st.markdown(f"**Vector Solución (en {len(iteraciones) - 1} iteraciones):**")
            cols_sol = st.columns(n_vars)
            for idx, val in enumerate(x_final):
                cols_sol[idx].metric(nombres_vars_jac[idx], f"{val:.4f}")

            # Tabla exacta con n = 0, 1, 2...
            filas_tabla = []
            for it in iteraciones:
                err_str = "-" if it['n'] == 0 else f"{it['error_rel']:.5f}%"
                filas_tabla.append([str(it['n'])] + [f"{val:.4f}" for val in it['x']] + [err_str])

            cols_tabla = ["n"] + nombres_vars_jac + ["Error Máx (%)"]
            df_tabla_jac = pd.DataFrame(filas_tabla, columns=cols_tabla)
            st.dataframe(df_tabla_jac, use_container_width=True, height=300, hide_index=True)

        except Exception as e:
            st.error(f"Error en Jacobi: {e}")

# 3. BOTONES DE NAVEGACIÓN ENTRE UNIDADES
st.write("")
col_prev, col_space, col_next = st.columns([1, 2, 1])
with col_prev:
    st.markdown('<a href="/Unidad_2" target="_self" class="btn-comenzar">Volver a Unidad 2</a>', unsafe_allow_html=True)
with col_next:
    st.markdown('<div style="text-align: right;"><a href="/Unidad_4" target="_self" class="btn-comenzar">Ir a Unidad 4</a></div>', unsafe_allow_html=True)
