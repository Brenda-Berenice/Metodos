import sympy as sp
from typing import List, Dict, Any, Tuple, Optional

# Ecuaciones vistas en clase (de tus compañeros)
ECUACIONES_CLASE = [
    ("x^3 - 2*x - 5", 2.0, 3.0),
    ("x^3 + 4*x^2 - 10", 1.0, 2.0),
    ("cos(x) - x", 0.0, 1.0),
    ("exp(-x) - x", 0.0, 1.0),
]

def evaluar_funcion(expr_str: str, val_x: float) -> float:
    """Evalúa expresiones matemáticas aceptando tanto ^ como ** para potencias."""
    expr_limpia = expr_str.replace("^", "**")
    x = sp.Symbol('x')
    expr = sp.sympify(expr_limpia)
    return float(expr.subs(x, val_x))

def buscar_extremo_cambio_signo(expr: str, a: float) -> float:
    """Lógica original de tus compañeros para localizar automáticamente el extremo b."""
    fa = evaluar_funcion(expr, a)
    if abs(fa) < 1e-15:
        return a + 0.5
    for paso in [0.5, 1.0, 1.5, 2.0, 3.0, 5.0]:
        for signo in (1.0, -1.0):
            cand = a + signo * paso
            try:
                fc = evaluar_funcion(expr, cand)
                if fa * fc <= 0:
                    return cand
            except Exception:
                pass
    x_scan = -10.0
    while x_scan <= 10.0:
        try:
            fc = evaluar_funcion(expr, x_scan)
            if fa * fc <= 0 and abs(x_scan - a) > 1e-6:
                return x_scan
        except Exception:
            pass
        x_scan += 0.25
    raise ValueError(
        f"No se encontró cambio de signo alrededor del valor inicial {a}. "
        f"Ingresa un intervalo [a, b] donde f(a) y f(b) tengan signos opuestos."
    )

def biseccion(
    expr: str,
    a: float,
    b: Optional[float] = None,
    tol: float = 1e-4,
    max_iter: int = 100
) -> Tuple[List[Dict[str, Any]], Dict[str, Any]]:
    """Algoritmo exacto de Bisección desarrollado por tu equipo."""
    if b is None or abs(b - a) < 1e-14:
        b = buscar_extremo_cambio_signo(expr, a)

    fa = evaluar_funcion(expr, a)
    fb = evaluar_funcion(expr, b)

    if fa * fb > 0:
        b = buscar_extremo_cambio_signo(expr, a)
        fb = evaluar_funcion(expr, b)

    if a > b:
        a, b = b, a
        fa, fb = fb, fa

    iteraciones = []
    xr_ant = None
    raiz = (a + b) / 2.0
    convergido = False
    a_ini, b_ini = a, b

    for k in range(1, max_iter + 1):
        xr = (a + b) / 2.0
        fxr = evaluar_funcion(expr, xr)

        if xr_ant is not None and abs(xr) > 1e-15:
            ea = abs((xr - xr_ant) / xr) * 100.0
        elif xr_ant is not None:
            ea = abs(xr - xr_ant) * 100.0
        else:
            ea = 100.0

        iteraciones.append({
            'iter': k,
            'a': a,
            'b': b,
            'xr': xr,
            'fa': fa,
            'fb': fb,
            'fxr': fxr,
            'ea': ea
        })

        if abs(fxr) < 1e-15 or (xr_ant is not None and ea <= tol):
            raiz = xr
            convergido = True
            break

        if fa * fxr < 0:
            b = xr
            fb = fxr
        else:
            a = xr
            fa = fxr

        xr_ant = xr
        raiz = xr

    resumen = {
        'raiz': raiz,
        'f_raiz': evaluar_funcion(expr, raiz),
        'iteraciones_totales': len(iteraciones),
        'convergido': convergido,
        'error_final': iteraciones[-1]['ea'] if iteraciones else 0.0,
        'a_usado': a_ini,
        'b_usado': b_ini
    }

    return iteraciones, resumen


# ==================== MÉTODO DE NEWTON ====================

ECUACIONES_CLASE_NEWTON = [
    ("cos(x) - x", "-sin(x) - 1", 1.0),
    ("x^3 - 2*x - 5", "3*x^2 - 2", 2.0),
    ("exp(-x) - x", "-exp(-x) - 1", 0.5),
    ("x^3 + 4*x^2 - 10", "3*x^2 + 8*x", 1.5),
]

def derivada_numerica(expr: str, x: float, h: float = 1e-7) -> float:
    return (evaluar_funcion(expr, x + h) - evaluar_funcion(expr, x - h)) / (2.0 * h)

def newton_raphson(
    expr: str,
    x0: float,
    expr_derivada: Optional[str] = None,
    tol: float = 1e-4,
    max_iter: int = 100
) -> Tuple[List[Dict[str, Any]], Dict[str, Any]]:
    iteraciones = []
    xi = x0
    raiz = x0
    convergido = False

    for k in range(1, max_iter + 1):
        f_xi = evaluar_funcion(expr, xi)

        if expr_derivada and expr_derivada.strip():
            df_xi = evaluar_funcion(expr_derivada.strip(), xi)
        else:
            df_xi = derivada_numerica(expr, xi)

        if abs(df_xi) < 1e-14:
            raise ZeroDivisionError(
                f"Derivada nula o casi nula en la iteración {k}: f'({xi:.6g}) = {df_xi:.4e}. "
                f"Prueba con otro valor inicial x0."
            )

        x_siguiente = xi - (f_xi / df_xi)

        if abs(x_siguiente) > 1e-15:
            ea = abs((x_siguiente - xi) / x_siguiente) * 100.0
        else:
            ea = abs(x_siguiente - xi) * 100.0

        iteraciones.append({
            'iter': k,
            'xi': xi,
            'f_xi': f_xi,
            'df_xi': df_xi,
            'x_sig': x_siguiente,
            'ea': ea
        })

        raiz = x_siguiente
        if abs(f_xi) < 1e-15 or ea <= tol:
            convergido = True
            break

        xi = x_siguiente

    resumen = {
        'raiz': raiz,
        'f_raiz': evaluar_funcion(expr, raiz),
        'iteraciones_totales': len(iteraciones),
        'convergido': convergido,
        'error_final': iteraciones[-1]['ea'] if iteraciones else 0.0
    }

    return iteraciones, resumen

# ==================== MÉTODO DE LA SECANTE ====================

ECUACIONES_CLASE_SECANTE = [
    ("exp(-x^2) - x", 0.0, 1.0),
    ("x^3 - 2*x - 5", 2.0, 3.0),
    ("cos(x) - x", 0.5, 1.0),
    ("x^3 + 4*x^2 - 10", 1.0, 2.0),
]

def secante(
    expr: str,
    x0: float,
    x1: float,
    tol: float = 1e-4,
    max_iter: int = 100
) -> Tuple[List[Dict[str, Any]], Dict[str, Any]]:
    iteraciones = []
    x_ant = x0
    x_act = x1
    f_ant = evaluar_funcion(expr, x_ant)
    raiz = x1
    convergido = False

    for k in range(1, max_iter + 1):
        f_act = evaluar_funcion(expr, x_act)
        den = f_act - f_ant

        if abs(den) < 1e-15:
            raise ZeroDivisionError(f"División entre cero en iteración {k}: f(x_i) ≈ f(x_{{i-1}}).")

        x_sig = x_act - (f_act * (x_act - x_ant)) / den

        if abs(x_sig) > 1e-15:
            ea = abs((x_sig - x_act) / x_sig) * 100.0
        else:
            ea = abs(x_sig - x_act) * 100.0

        iteraciones.append({
            'iter': k,
            'x_ant': x_ant,
            'x_act': x_act,
            'f_ant': f_ant,
            'f_act': f_act,
            'x_sig': x_sig,
            'ea': ea
        })

        raiz = x_sig
        if abs(f_act) < 1e-15 or ea <= tol:
            convergido = True
            break

        x_ant = x_act
        f_ant = f_act
        x_act = x_sig

    resumen = {
        'raiz': raiz,
        'f_raiz': evaluar_funcion(expr, raiz),
        'iteraciones_totales': len(iteraciones),
        'convergido': convergido,
        'error_final': iteraciones[-1]['ea'] if iteraciones else 0.0
    }

    return iteraciones, resumen
