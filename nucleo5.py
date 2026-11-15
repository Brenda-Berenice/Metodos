from typing import List, Tuple

Matriz = List[List[float]]
Vector = List[float]

# Ejercicio de clase precargado por tus compañeros
EJEMPLO_POT_A = [
    [4.0, 1.0, 2.0],
    [1.0, 2.0, 0.0],
    [2.0, 0.0, 5.0]
]

def multiplicar_matriz_vector(A: Matriz, v: Vector) -> Vector:
    return [sum(A[i][j] * v[j] for j in range(len(v))) for i in range(len(A))]

# ==================== MÉTODO DE LA POTENCIA (VALOR PROPIO MÁXIMO) ====================

def metodo_potencia_maximo(
    A: Matriz,
    x0: Vector = None,
    tol: float = 1e-4,
    max_iter: int = 100
) -> Tuple[float, Vector, List[dict], bool]:
    n = len(A)
    x = [1.0] * n if x0 is None else list(x0)

    lambda_ant = 0.0
    iteraciones = []
    convergido = False

    for k in range(1, max_iter + 1):
        y = multiplicar_matriz_vector(A, x)

        # Componente de mayor valor absoluto (conservando su signo)
        idx_max = max(range(n), key=lambda i: abs(y[i]))
        c_max = y[idx_max]

        if abs(c_max) < 1e-15:
            raise ValueError(f"El vector propio colapsó a cero en la iteración {k}.")

        x_sig = [val / c_max for val in y]

        if k == 1:
            err_rel = 100.0
        else:
            err_lam = abs((c_max - lambda_ant) / c_max) * 100.0
            err_vec = max(abs(x_sig[i] - x[i]) for i in range(n)) * 100.0
            err_rel = max(err_lam, err_vec)

        iteraciones.append({
            'k': k,
            'y': list(y),
            'lambda': c_max,
            'vector': list(x_sig),
            'error': err_rel
        })

        if k > 1 and err_rel <= tol:
            convergido = True
            break

        lambda_ant = c_max
        x = x_sig

    lambda_final = iteraciones[-1]['lambda']
    vector_final = iteraciones[-1]['vector']
    return lambda_final, vector_final, iteraciones, convergido

# ==================== MÉTODO DE LA POTENCIA INVERSA (VALOR PROPIO MÍNIMO) ====================

def inversa_gauss_jordan(A: Matriz) -> Tuple[Matriz, List[str]]:
    """Calcula la matriz inversa A^-1 mediante Gauss-Jordan."""
    n = len(A)
    M = [list(map(float, A[i])) + [1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    for k in range(n):
        if abs(M[k][k]) < 1e-12:
            max_fila = max(range(k, n), key=lambda i: abs(M[i][k]))
            if abs(M[max_fila][k]) < 1e-14:
                raise ValueError("La matriz es singular y no tiene inversa.")
            M[k], M[max_fila] = M[max_fila], M[k]
        pivote = M[k][k]
        for j in range(k, 2 * n):
            M[k][j] /= pivote
        for i in range(n):
            if i != k:
                factor = M[i][k]
                for j in range(k, 2 * n):
                    M[i][j] -= factor * M[k][j]
    A_inv = [row[n:] for row in M]
    return A_inv, []

def metodo_potencia_inversa(
    A: Matriz,
    x0: Vector = None,
    tol: float = 1e-4,
    max_iter: int = 100
) -> Tuple[float, Vector, List[dict], bool]:
    n = len(A)
    A_inv, _ = inversa_gauss_jordan(A)
    x = [1.0] * n if x0 is None else list(x0)

    lambda_ant = 0.0
    iteraciones = []
    convergido = False

    for k in range(1, max_iter + 1):
        y = multiplicar_matriz_vector(A_inv, x)

        idx_max = max(range(n), key=lambda i: abs(y[i]))
        mu_max = y[idx_max]

        if abs(mu_max) < 1e-15:
            raise ValueError(f"El vector colapsó a cero en la iteración {k}.")

        lambda_min = 1.0 / mu_max
        x_sig = [val / mu_max for val in y]

        if k == 1:
            err_rel = 100.0
        else:
            err_lam = abs((lambda_min - lambda_ant) / lambda_min) * 100.0 if abs(lambda_min) > 1e-15 else 0.0
            err_vec = max(abs(x_sig[i] - x[i]) for i in range(n)) * 100.0
            err_rel = max(err_lam, err_vec)

        iteraciones.append({
            'k': k,
            'mu': mu_max,
            'lambda': lambda_min,
            'vector': list(x_sig),
            'error': err_rel
        })

        if k > 1 and err_rel <= tol:
            convergido = True
            break

        lambda_ant = lambda_min
        x = x_sig

    lambda_final = iteraciones[-1]['lambda']
    vector_final = iteraciones[-1]['vector']
    return lambda_final, vector_final, iteraciones, convergido
