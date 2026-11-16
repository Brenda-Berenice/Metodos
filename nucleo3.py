from typing import List, Tuple, Dict, Any

Matriz = List[List[float]]
Vector = List[float]

# ==================== EJERCICIOS DE CLASE ====================

EJEMPLO_GJ_CLASE_A = [
    [2.0, 3.0, -2.0, 1.0],
    [1.0, 3.0, 2.0, -1.0],
    [2.0, -2.0, 0.0, 1.0],
    [-1.0, 1.0, 1.0, 0.0]
]
EJEMPLO_GJ_CLASE_B = [0.0, -2.0, 2.0, 1.0]

EJEMPLO_GJ_A = [
    [2.0, 1.0, -1.0],
    [-3.0, -1.0, 2.0],
    [-2.0, 1.0, 2.0]
]
EJEMPLO_GJ_B = [8.0, -11.0, -3.0]

EJEMPLO_CLASE_3_A = [
    [11.0, -3.0, -2.0],
    [4.0, -7.0, 2.0],
    [5.0, -2.0, -8.0]
]
EJEMPLO_CLASE_3_B = [18.0, 2.0, 13.0]

EJEMPLO_ITER_A = [
    [4.0, 1.0, -1.0],
    [2.0, 7.0, 1.0],
    [1.0, -3.0, 12.0]
]
EJEMPLO_ITER_B = [3.0, 19.0, 31.0]

EJEMPLO_JAC_A = [
    [10.0, 2.0, -1.0],
    [-2.0, 10.0, 1.0],
    [1.0, -2.0, 10.0]
]
EJEMPLO_JAC_B = [7.0, 8.0, 6.0]


# ==================== MÉTODO DE GAUSS-JORDAN ====================

def gauss_jordan(A: Matriz, b: Vector) -> Tuple[Vector, List[str]]:
    
    n = len(A)
    A_orig = [list(map(float, fila)) for fila in A]
    b_orig = list(map(float, b))
    M = [A_orig[i] + [b_orig[i]] for i in range(n)]
    pasos: List[str] = []

    pasos.append(f"Matriz aumentada inicial [A | b] ({n}x{n+1}):")
    for row in M:
        pasos.append("  ( " + "  ".join(f"{val:9.4f}" for val in row[:-1]) + f" | {row[-1]:9.4f} )")

    for k in range(n):
        # Si el pivote es cero, intercambiamos renglones
        if abs(M[k][k]) < 1e-12:
            max_fila = max(range(k, n), key=lambda i: abs(M[i][k]))
            if abs(M[max_fila][k]) < 1e-14:
                raise ValueError(f"El sistema no tiene solución única (pivote nulo en columna {k+1}).")
            M[k], M[max_fila] = M[max_fila], M[k]
            pasos.append(f"\n[Paso {k+1}] Intercambio de renglones: R{k+1} <-> R{max_fila+1}")

        pivote = M[k][k]
        if abs(pivote - 1.0) > 1e-12:
            pasos.append(f"\n[Paso {k+1}] Hacer 1 el pivote: (1 / {pivote:.4f}) R{k+1} -> R{k+1}")
            for j in range(k, n + 1):
                M[k][j] /= pivote
        else:
            pasos.append(f"\n[Paso {k+1}] El pivote en R{k+1} ya es 1:")

        ops_elim = []
        for i in range(n):
            if i != k:
                factor = M[i][k]
                if abs(factor) > 1e-15:
                    for j in range(k, n + 1):
                        M[i][j] -= factor * M[k][j]
                    signo = "-" if factor > 0 else "+"
                    ops_elim.append(f"    {signo}{abs(factor):.4f} R{k+1} + R{i+1} -> R{i+1}")

        if ops_elim:
            pasos.append("  Eliminación en columna " + str(k + 1) + ":")
            pasos.extend(ops_elim)

        pasos.append(f"  Matriz equivalente después del Paso {k+1}:")
        for row in M:
            pasos.append("  ( " + "  ".join(f"{val:9.4f}" for val in row[:-1]) + f" | {row[-1]:9.4f} )")

    x_final = [M[i][n] for i in range(n)]

    # Comprobación
    pasos.append("\nComprobación (sustituyendo en el sistema original):")
    for i in range(n):
        suma_comp = sum(A_orig[i][j] * x_final[j] for j in range(n))
        pasos.append(f"  Ecuación {i+1}: {suma_comp:.4f} ≈ {b_orig[i]:.4f}")

    return x_final, pasos


# ==================== HERRAMIENTAS PARA MÉTODOS ITERATIVOS ====================

def norma_infinito(v: Vector) -> float:
    return max(abs(x) for x in v) if v else 0.0

def reordenar_diagonal_dominante(A: Matriz, b: Vector) -> Tuple[Matriz, Vector, bool, str]:
    """
    Reescribe el sistema intercambiando ecuaciones (como en clase) para lograr
    que la matriz sea diagonalmente dominante y asegurar la convergencia.
    """
    n = len(A)
    A_nueva = [list(map(float, fila)) for fila in A]
    b_nuevo = list(map(float, b))
    usadas = [False] * n
    A_ord = []
    b_ord = []

    for col in range(n):
        mejor_fila = -1
        mejor_val = -1.0
        for fila in range(n):
            if not usadas[fila] and abs(A_nueva[fila][col]) > mejor_val:
                mejor_val = abs(A_nueva[fila][col])
                mejor_fila = fila
        if mejor_fila != -1:
            usadas[mejor_fila] = True
            A_ord.append(A_nueva[mejor_fila])
            b_ord.append(b_nuevo[mejor_fila])

    # Verificar si ya cumple ser diagonalmente dominante
    es_dom = True
    for i in range(n):
        diag = abs(A_ord[i][i])
        suma_otros = sum(abs(A_ord[i][j]) for j in range(n) if j != i)
        if diag < suma_otros:
            es_dom = False

    if es_dom:
        msg = "Sistema reescrito como matriz diagonalmente dominante (convergencia garantizada)."
    else:
        msg = "Advertencia: El sistema no es estrictamente diagonalmente dominante; podría no converger."

    return A_ord, b_ord, es_dom, msg


# ==================== MÉTODO DE GAUSS-SEIDEL ====================

def metodo_gauss_seidel(
    A: Matriz,
    b: Vector,
    x0: Vector = None,
    tol: float = 1e-4,
    max_iter: int = 100,
    auto_reordenar: bool = True
) -> Tuple[List[Dict[str, Any]], Vector, bool]:
    
    n = len(A)
    if auto_reordenar:
        A, b, _, _ = reordenar_diagonal_dominante(A, b)

    for i in range(n):
        if abs(A[i][i]) < 1e-15:
            raise ZeroDivisionError(f"Elemento diagonal nulo en A[{i+1},{i+1}].")

    x = [0.0] * n if x0 is None else list(map(float, x0))
    
    iteraciones = [{
        'n': 0,
        'x': list(x),
        'error_abs': 0.0,
        'error_rel': 100.0
    }]
    convergido = False

    for k in range(1, max_iter + 1):
        x_ant = list(x)
        for i in range(n):
            suma_nuevos = sum(A[i][j] * x[j] for j in range(i))
            suma_anteriores = sum(A[i][j] * x_ant[j] for j in range(i + 1, n))
            x[i] = (b[i] - suma_nuevos - suma_anteriores) / A[i][i]

        diff = [abs(x[i] - x_ant[i]) for i in range(n)]
        err = max(diff)
        norm_act = norma_infinito(x)
        err_rel = (err / norm_act) * 100.0 if norm_act > 1e-15 else err * 100.0

        iteraciones.append({
            'n': k,
            'x': list(x),
            'error_abs': err,
            'error_rel': err_rel
        })

        if err <= tol or err_rel <= tol:
            convergido = True
            break

    return iteraciones, x, convergido


# ==================== MÉTODO DE JACOBI ====================

def metodo_jacobi(
    A: Matriz,
    b: Vector,
    x0: Vector = None,
    tol: float = 1e-4,
    max_iter: int = 100,
    auto_reordenar: bool = True
) -> Tuple[List[Dict[str, Any]], Vector, bool]:
    
    n = len(A)
    if auto_reordenar:
        A, b, _, _ = reordenar_diagonal_dominante(A, b)

    for i in range(n):
        if abs(A[i][i]) < 1e-15:
            raise ZeroDivisionError(f"Elemento diagonal nulo en A[{i+1},{i+1}].")

    x_ant = [0.0] * n if x0 is None else list(map(float, x0))
    iteraciones = [{
        'n': 0,
        'x': list(x_ant),
        'error_abs': 0.0,
        'error_rel': 100.0
    }]
    convergido = False
    x_act = list(x_ant)

    for k in range(1, max_iter + 1):
        x_act = [0.0] * n
        for i in range(n):
            suma = sum(A[i][j] * x_ant[j] for j in range(n) if j != i)
            x_act[i] = (b[i] - suma) / A[i][i]

        diff = [abs(x_act[i] - x_ant[i]) for i in range(n)]
        err = max(diff)
        norm_act = norma_infinito(x_act)
        err_rel = (err / norm_act) * 100.0 if norm_act > 1e-15 else err * 100.0

        iteraciones.append({
            'n': k,
            'x': list(x_act),
            'error_abs': err,
            'error_rel': err_rel
        })

        if err <= tol or err_rel <= tol:
            convergido = True
            break

        x_ant = list(x_act)

    return iteraciones, x_act, convergido
