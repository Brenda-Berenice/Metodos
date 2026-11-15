from typing import List, Tuple

Matriz = List[List[float]]
Vector = List[float]

# Ejercicio de clase precargado por tus compañeros
EJEMPLO_GJ_A = [
    [2.0, 1.0, -1.0],
    [-3.0, -1.0, 2.0],
    [-2.0, 1.0, 2.0]
]
EJEMPLO_GJ_B = [8.0, -11.0, -3.0]

def gauss_jordan(A: Matriz, b: Vector) -> Tuple[Vector, List[str]]:
    """
    Algoritmo exacto de Gauss-Jordan de tu equipo:
    Transforma [A | b] en [I | x] guardando el desarrollo paso a paso.
    """
    n = len(A)
    M = [list(map(float, A[i])) + [float(b[i])] for i in range(n)]
    pasos: List[str] = []

    pasos.append(f"Matriz aumentada inicial [A | b] ({n}x{n+1}):")
    for row in M:
        pasos.append("  [ " + "  ".join(f"{val:10.4f}" for val in row[:-1]) + f" | {row[-1]:10.4f} ]")

    for k in range(n):
        if abs(M[k][k]) < 1e-12:
            max_fila = max(range(k, n), key=lambda i: abs(M[i][k]))
            if abs(M[max_fila][k]) < 1e-14:
                raise ValueError(f"El sistema no tiene solución única (pivote nulo en columna {k+1}).")
            M[k], M[max_fila] = M[max_fila], M[k]
            pasos.append(f"\n[Paso {k+1}] Intercambio de R{k+1} <-> R{max_fila+1} para evitar pivote nulo.")

        pivote = M[k][k]
        pasos.append(f"\n[Paso {k+1}] Normalizar R{k+1} --> R{k+1} = R{k+1} / ({pivote:.4f}):")
        for j in range(k, n + 1):
            M[k][j] /= pivote

        pasos.append(f"  Eliminación en columna {k+1} (hacer ceros arriba y abajo del pivote):")
        for i in range(n):
            if i != k:
                factor = M[i][k]
                if abs(factor) > 1e-15:
                    for j in range(k, n + 1):
                        M[i][j] -= factor * M[k][j]
                    pasos.append(f"    R{i+1} = R{i+1} - ({factor:.4f}) · R{k+1}")

        pasos.append(f"  Matriz aumentada después del Paso {k+1}:")
        for row in M:
            pasos.append("  [ " + "  ".join(f"{val:10.4f}" for val in row[:-1]) + f" | {row[-1]:10.4f} ]")

    x_final = [M[i][n] for i in range(n)]
    return x_final, pasos

# ==================== MÉTODO DE GAUSS-SEIDEL ====================

EJEMPLO_ITER_A = [
    [4.0, 1.0, -1.0],
    [2.0, 7.0, 1.0],
    [1.0, -3.0, 12.0]
]
EJEMPLO_ITER_B = [3.0, 19.0, 31.0]

def norma_infinito(v: Vector) -> float:
    return max(abs(x) for x in v) if v else 0.0

def es_diagonalmente_dominante(A: Matriz) -> Tuple[bool, str]:
    n = len(A)
    for i in range(n):
        diag = abs(A[i][i])
        suma_otros = sum(abs(A[i][j]) for j in range(n) if j != i)
        if diag < suma_otros:
            return False, "La matriz no es diagonalmente dominante; podría no converger."
    return True, "Matriz diagonalmente dominante (convergencia garantizada)."

def metodo_gauss_seidel(
    A: Matriz,
    b: Vector,
    x0: Vector = None,
    tol: float = 1e-4,
    max_iter: int = 100
) -> Tuple[List[dict], Vector, bool]:
    n = len(A)
    for i in range(n):
        if abs(A[i][i]) < 1e-15:
            raise ZeroDivisionError(f"Elemento diagonal nulo en A[{i+1},{i+1}]. Reordena las ecuaciones.")

    x = [0.0] * n if x0 is None else list(x0)
    iteraciones = []
    convergido = False

    for k in range(1, max_iter + 1):
        x_ant = list(x)
        for i in range(n):
            suma1 = sum(A[i][j] * x[j] for j in range(i))
            suma2 = sum(A[i][j] * x_ant[j] for j in range(i + 1, n))
            x[i] = (b[i] - suma1 - suma2) / A[i][i]

        diff = [abs(x[i] - x_ant[i]) for i in range(n)]
        err = max(diff)
        norm_act = norma_infinito(x)
        err_rel = (err / norm_act) * 100.0 if norm_act > 1e-15 else err * 100.0

        iteraciones.append({
            'k': k,
            'x': list(x),
            'error_abs': err,
            'error_rel': err_rel
        })

        if err <= tol or err_rel <= tol:
            convergido = True
            break

    return iteraciones, x, convergido

# ==================== MÉTODO DE JACOBI ====================

EJEMPLO_JAC_A = [
    [10.0, 2.0, -1.0],
    [-2.0, 10.0, 1.0],
    [1.0, -2.0, 10.0]
]
EJEMPLO_JAC_B = [7.0, 8.0, 6.0]

def metodo_jacobi(
    A: Matriz,
    b: Vector,
    x0: Vector = None,
    tol: float = 1e-4,
    max_iter: int = 100
) -> Tuple[List[dict], Vector, bool]:
    n = len(A)
    for i in range(n):
        if abs(A[i][i]) < 1e-15:
            raise ZeroDivisionError(f"Elemento diagonal nulo en A[{i+1},{i+1}]. Reordena las ecuaciones.")

    x_ant = [0.0] * n if x0 is None else list(x0)
    iteraciones = []
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
            'k': k,
            'x': list(x_act),
            'error_abs': err,
            'error_rel': err_rel
        })

        if err <= tol or err_rel <= tol:
            convergido = True
            break

        x_ant = list(x_act)

    return iteraciones, x_act, convergido

# ==================== MÉTODO DE JACOBI ====================

EJEMPLO_JAC_A = [
    [10.0, 2.0, -1.0],
    [-2.0, 10.0, 1.0],
    [1.0, -2.0, 10.0]
]
EJEMPLO_JAC_B = [7.0, 8.0, 6.0]

def metodo_jacobi(
    A: Matriz,
    b: Vector,
    x0: Vector = None,
    tol: float = 1e-4,
    max_iter: int = 100
) -> Tuple[List[dict], Vector, bool]:
    n = len(A)
    for i in range(n):
        if abs(A[i][i]) < 1e-15:
            raise ZeroDivisionError(f"Elemento diagonal nulo en A[{i+1},{i+1}]. Reordena las ecuaciones.")

    x_ant = [0.0] * n if x0 is None else list(x0)
    iteraciones = []
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
            'k': k,
            'x': list(x_act),
            'error_abs': err,
            'error_rel': err_rel
        })

        if err <= tol or err_rel <= tol:
            convergido = True
            break

        x_ant = list(x_act)

    return iteraciones, x_act, convergido
