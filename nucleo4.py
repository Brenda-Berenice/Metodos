from typing import List, Tuple

Matriz = List[List[float]]
Vector = List[float]

EJEMPLO_LU_A = [
    [2.0, -1.0, -2.0],
    [-4.0, 6.0, 3.0],
    [-4.0, -2.0, 8.0]
]
EJEMPLO_LU_B = [-1.0, 13.0, -6.0]

def crear_matriz(filas: int, cols: int, val: float = 0.0) -> Matriz:
    return [[val for _ in range(cols)] for _ in range(filas)]

def matriz_identidad(n: int) -> Matriz:
    return [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]

def sustitucion_progresiva(L: Matriz, b: Vector, unos_diagonal: bool = True) -> Vector:
    """Resuelve L · v = b"""
    n = len(L)
    v = [0.0] * n
    for i in range(n):
        suma = sum(L[i][j] * v[j] for j in range(i))
        v[i] = (b[i] - suma) if unos_diagonal else (b[i] - suma) / L[i][i]
    return v

def sustitucion_regresiva(U: Matriz, v: Vector, unos_diagonal: bool = False) -> Vector:
    """Resuelve U · x = v"""
    n = len(U)
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        suma = sum(U[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (v[i] - suma) if unos_diagonal else (v[i] - suma) / U[i][i]
    return x

# ==================== MÉTODO DE DOOLITTLE (l_kk = 1)====================

def factorizacion_doolittle(A: Matriz, b: Vector = None) -> Tuple[Matriz, Matriz, Vector, List[str]]:
    n = len(A)
    L = matriz_identidad(n)
    U = crear_matriz(n, n, 0.0)
    pasos = []

    pasos.append("1. Factorización A = L · U por Doolittle (especificando l_kk = 1):")

    for k in range(n):
        # Calcular u_kk = a_kk - sum(l_ks * u_sk)
        suma_diag = sum(L[k][s] * U[s][k] for s in range(k))
        U[k][k] = A[k][k] - suma_diag
        pasos.append(f"   [k={k+1}] u[{k+1},{k+1}] = {A[k][k]:.4f} - ({suma_diag:.4f}) = {U[k][k]:.4f}")

        if abs(U[k][k]) < 1e-15:
            raise ZeroDivisionError(f"Pivote nulo en u[{k+1},{k+1}] = 0.")

        # Calcular fila k de U (j = k+1 ... n)
        for j in range(k + 1, n):
            suma = sum(L[k][s] * U[s][j] for s in range(k))
            U[k][j] = (A[k][j] - suma) / L[k][k]
            pasos.append(f"   u[{k+1},{j+1}] = ({A[k][j]:.4f} - ({suma:.4f})) / 1 = {U[k][j]:.4f}")

        # Calcular columna k de L (i = k+1 ... n)
        for i in range(k + 1, n):
            suma = sum(L[i][s] * U[s][k] for s in range(k))
            L[i][k] = (A[i][k] - suma) / U[k][k]
            pasos.append(f"   l[{i+1},{k+1}] = ({A[i][k]:.4f} - ({suma:.4f})) / {U[k][k]:.4f} = {L[i][k]:.4f}")

    x = None
    if b is not None and len(b) == n:
        pasos.append("\n2. Sustitución progresiva en L · v = b:")
        v = sustitucion_progresiva(L, b, unos_diagonal=True)
        for i, vi in enumerate(v, 1):
            pasos.append(f"   v{i} = {vi:.4f}")

        pasos.append("\n3. Sustitución regresiva en U · x = v:")
        x = sustitucion_regresiva(U, v, unos_diagonal=False)
        for i, xi in enumerate(x, 1):
            pasos.append(f"   x{i} = {xi:.4f}")

    return L, U, x, pasos

# ==================== MÉTODO DE CROUT (u_kk = 1)====================

def factorizacion_crout(A: Matriz, b: Vector = None) -> Tuple[Matriz, Matriz, Vector, List[str]]:
    
    n = len(A)
    L = crear_matriz(n, n, 0.0)
    U = matriz_identidad(n)
    pasos = []

    pasos.append("1. Factorización A = L · U por Crout (especificando u_kk = 1):")

    for k in range(n):
        # Calcular l_kk = a_kk - sum(l_ks * u_sk)
        suma_diag = sum(L[k][s] * U[s][k] for s in range(k))
        L[k][k] = A[k][k] - suma_diag
        pasos.append(f"   [k={k+1}] l[{k+1},{k+1}] = {A[k][k]:.4f} - ({suma_diag:.4f}) = {L[k][k]:.4f}")

        if abs(L[k][k]) < 1e-15:
            raise ZeroDivisionError(f"Pivote diagonal nulo en l[{k+1},{k+1}] = 0.")

        # Calcular fila k de U (j = k+1 ... n)
        for j in range(k + 1, n):
            suma = sum(L[k][s] * U[s][j] for s in range(k))
            U[k][j] = (A[k][j] - suma) / L[k][k]
            pasos.append(f"   u[{k+1},{j+1}] = ({A[k][j]:.4f} - ({suma:.4f})) / {L[k][k]:.4f} = {U[k][j]:.4f}")

        # Calcular columna k de L (i = k+1 ... n)
        for i in range(k + 1, n):
            suma = sum(L[i][s] * U[s][k] for s in range(k))
            L[i][k] = (A[i][k] - suma) / U[k][k]
            pasos.append(f"   l[{i+1},{k+1}] = ({A[i][k]:.4f} - ({suma:.4f})) / 1 = {L[i][k]:.4f}")

    x = None
    if b is not None and len(b) == n:
        pasos.append("\n2. Sustitución progresiva en L · v = b :")
        v = sustitucion_progresiva(L, b, unos_diagonal=False)
        for i, vi in enumerate(v, 1):
            pasos.append(f"   v{i} = {vi:.4f}")

        pasos.append("\n3. Sustitución regresiva en U · x = v:")
        x = sustitucion_regresiva(U, v, unos_diagonal=True)
        for i, xi in enumerate(x, 1):
            pasos.append(f"   x{i} = {xi:.4f}")

    return L, U, x, pasos
