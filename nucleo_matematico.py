import sympy as sp
from typing import List, Dict, Any, Tuple, Optional

# ==================== HERRAMIENTAS BASE ====================

def evaluar_funcion(expr_str: str, val_x: float) -> float:
    """Evalúa f(x) aceptando tanto ^ como ** para potencias."""
    expr_limpia = expr_str.replace("^", "**")
    x = sp.Symbol('x')
    expr = sp.sympify(expr_limpia)
    return float(expr.subs(x, val_x))

def buscar_extremo_cambio_signo(expr: str, a: float) -> float:
    """Busca un extremo b donde f(a) y f(b) tengan signos opuestos (Teorema de Bolzano)."""
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
        f"No se encontró cambio de signo alrededor de a = {a}. "
        f"Ingresa un intervalo [a, b] donde f(a) y f(b) tengan signos opuestos."
    )


# ==================== MÉTODO DE BISECCIÓN ====================

ECUACIONES_CLASE = [
    ("x^2 - exp(x) - 3*x + 2", -12.0, 3.0), 
    ("x^3 - 2*x - 5", 2.0, 3.0),
    ("x^3 + 4*x^2 - 10", 1.0, 2.0),
    ("cos(x) - x", 0.0, 1.0),
    ("exp(-x) - x", 0.0, 1.0),
]

def biseccion(
    expr: str,
    a: float,
    b: Optional[float] = None,
    tol: float = 1e-4,
    max_iter: int = 100
) -> Tuple[List[Dict[str, Any]], Dict[str, Any]]:
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
    c_ant = None
    c = (a + b) / 2.0
    convergido = False
    a_ini, b_ini = a, b

    for n in range(1, max_iter + 1):
        c = (a + b) / 2.0
        fc = evaluar_funcion(expr, c)

        if c_ant is not None and abs(c) > 1e-15:
            ea = abs((c - c_ant) / c) * 100.0
        elif c_ant is not None:
            ea = abs(c - c_ant) * 100.0
        else:
            ea = 100.0

        iteraciones.append({
            'n': n,
            'a': a,
            'b': b,
            'c': c,
            'fa': fa,
            'fb': fb,
            'fc': fc,
            'ea': ea
        })

        if abs(fc) < 1e-15 or (c_ant is not None and ea <= tol):
            convergido = True
            break

        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

        c_ant = c

    resumen = {
        'raiz': c,
        'f_raiz': evaluar_funcion(expr, c),
        'iteraciones_totales': len(iteraciones),
        'convergido': convergido,
        'error_final': iteraciones[-1]['ea'] if iteraciones else 0.0,
        'a_usado': a_ini,
        'b_usado': b_ini
    }

    return iteraciones, resumen


# ==================== MÉTODO DE NEWTON ====================

ECUACIONES_CLASE_NEWTON = [
    ("x^2 - exp(x) - 3*x + 2", "2*x - exp(x) - 3", -5.0), 
    ("cos(x) - x", "-sin(x) - 1", 1.0),
    ("x^3 - 2*x - 5", "3*x^2 - 2", 2.0),
    ("exp(-x) - x", "-exp(-x) - 1", 0.5),
    ("x^3 + 4*x^2 - 10", "3*x^2 + 8*x", 1.5),
]

def derivada_numerica(expr: str, x: float, h: float = 1e-7) -> float:
    """Aproxima f'(x) mediante diferencias divididas centradas."""
    return (evaluar_funcion(expr, x + h) - evaluar_funcion(expr, x - h)) / (2.0 * h)

def metodo_newton(
    expr: str,
    x0: float,
    expr_derivada: Optional[str] = None,
    tol: float = 1e-4,
    max_iter: int = 100
) -> Tuple[List[Dict[str, Any]], Dict[str, Any]]:
    iteraciones = []
    xn = x0
    raiz = x0
    convergido = False

    for n in range(0, max_iter):
        f_xn = evaluar_funcion(expr, xn)

        if expr_derivada and expr_derivada.strip():
            df_xn = evaluar_funcion(expr_derivada.strip(), xn)
        else:
            df_xn = derivada_numerica(expr, xn)

        if abs(df_xn) < 1e-14:
            raise ZeroDivisionError(
                f"Derivada nula en n = {n}: f'({xn:.6g}) = {df_xn:.4e}. "
                f"Propón otro valor inicial x0."
            )

        x_siguiente = xn - (f_xn / df_xn)

        if abs(x_siguiente) > 1e-15:
            ea = abs((x_siguiente - xn) / x_siguiente) * 100.0
        else:
            ea = abs(x_siguiente - xn) * 100.0

        iteraciones.append({
            'n': n,
            'xn': xn,
            'f_xn': f_xn,
            'df_xn': df_xn,
            'ea': ea
        })

        raiz = x_siguiente
        if abs(f_xn) < 1e-15 or ea <= tol:
            convergido = True
            break

        xn = x_siguiente

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
    ("x^2 - exp(x) - 3*x + 2", -5.0, 0.0), 
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
    f0 = evaluar_funcion(expr, x0)
    f1 = evaluar_funcion(expr, x1)

    ea_inicial = abs((x1 - x0) / x1) * 100.0 if abs(x1) > 1e-15 else abs(x1 - x0) * 100.0

    iteraciones = [
        {'n': 0, 'xn': x0, 'f_xn': f0, 'ea': 100.0},
        {'n': 1, 'xn': x1, 'f_xn': f1, 'ea': ea_inicial}
    ]

    x_ant = x0
    x_act = x1
    f_ant = f0
    f_act = f1
    raiz = x1
    convergido = False

    for n in range(1, max_iter):
        den = f_act - f_ant
        if abs(den) < 1e-15:
            raise ZeroDivisionError(f"División entre cero en n = {n}: f(x_n) ≈ f(x_{{n-1}}).")

        x_sig = x_act - f_act * ((x_act - x_ant) / den)
        f_sig = evaluar_funcion(expr, x_sig)

        if abs(x_sig) > 1e-15:
            ea = abs((x_sig - x_act) / x_sig) * 100.0
        else:
            ea = abs(x_sig - x_act) * 100.0

        iteraciones.append({
            'n': n + 1,
            'xn': x_sig,
            'f_xn': f_sig,
            'ea': ea
        })

        raiz = x_sig
        if abs(f_sig) < 1e-15 or ea <= tol:
            convergido = True
            break

        x_ant, f_ant = x_act, f_act
        x_act, f_act = x_sig, f_sig

    resumen = {
        'raiz': raiz,
        'f_raiz': evaluar_funcion(expr, raiz),
        'iteraciones_totales': len(iteraciones),
        'convergido': convergido,
        'error_final': iteraciones[-1]['ea'] if iteraciones else 0.0
    }

    return iteraciones, resumen
