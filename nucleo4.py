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

def sustitucion_adelante(L: Matriz, b: Vector, unos_diagonal: bool = True) -> Vector:
    n = len(L)
    y = [0.0] * n
    for i in range(n):
        suma = sum(L[i][j] * y[j] for j in range(i))
        y[i] = (b[i] - suma) if unos_diagonal else (b[i] - suma) / L[i][i]
    return y

def sustitucion_atras(U: Matriz, y: Vector, unos_diagonal: bool = False) -> Vector:
    n = len(U)
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        suma = sum(U[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (y[i] - suma) if unos_diagonal else (y[i] - suma) / U[i][i]
    return x

# ==================== MÉTODO DE DOOLITTLE ====================

def factorizacion_doolittle(A: Matriz, b: Vector = None) -> Tuple[Matriz, Matriz, Vector, List[str]]:
    n = len(A)
    L = matriz_identidad(n)
    U = crear_matriz(n, n, 0.0)
    pasos = []

    pasos.append("1. Factorización A = L · U por Doolittle (L con 1s en la diagonal principal):")

    for i in range(n):
        for j in range(i, n):
            suma = sum(L[i][k] * U[k][j] for k in range(i))
            U[i][j] = A[i][j] - suma
            pasos.append(f"   U[{i+1},{j+1}] = {A[i][j]:.4f} - ({suma:.4f}) = {U[i][j]:.6f}")

        if abs(U[i][i]) < 1e-15:
            raise ZeroDivisionError(f"Pivote nulo en U[{i+1},{i+1}] = 0.")

        for j in range(i + 1, n):
            suma = sum(L[j][k] * U[k][i] for k in range(i))
            L[j][i] = (A[j][i] - suma) / U[i][i]
            pasos.append(f"   L[{j+1},{i+1}] = ({A[j][i]:.4f} - ({suma:.4f})) / {U[i][i]:.4f} = {L[j][i]:.6f}")

    x = None
    if b is not None and len(b) == n:
        pasos.append("\n2. Sustitución progresiva (L · y = b):")
        y = sustitucion_adelante(L, b, unos_diagonal=True)
        for i, yi in enumerate(y, 1):
            pasos.append(f"   y{i} = {yi:.6f}")

        pasos.append("\n3. Sustitución regresiva (U · x = y):")
        x = sustitucion_atras(U, y, unos_diagonal=False)
        for i, xi in enumerate(x, 1):
            pasos.append(f"   x{i} = {xi:.6f}")

    return L, U, x, pasos

# ==================== MÉTODO DE CROUT ====================

def factorizacion_crout(A: Matriz, b: Vector = None) -> Tuple[Matriz, Matriz, Vector, List[str]]:
    n = len(A)
    L = crear_matriz(n, n, 0.0)
    U = matriz_identidad(n)
    pasos = []

    pasos.append("1. Factorización A = L · U por Crout (U con 1s en la diagonal principal):")

    for j in range(n):
        for i in range(j, n):
            suma = sum(L[i][k] * U[k][j] for k in range(j))
            L[i][j] = A[i][j] - suma
            pasos.append(f"   L[{i+1},{j+1}] = {A[i][j]:.4f} - ({suma:.4f}) = {L[i][j]:.6f}")

        if abs(L[j][j]) < 1e-15:
            raise ZeroDivisionError(f"Pivote diagonal nulo en L[{j+1},{j+1}] = 0.")

        for i in range(j + 1, n):
            suma = sum(L[j][k] * U[k][i] for k in range(j))
            U[j][i] = (A[j][i] - suma) / L[j][j]
            pasos.append(f"   U[{j+1},{i+1}] = ({A[j][i]:.4f} - ({suma:.4f})) / {L[j][j]:.4f} = {U[j][i]:.6f}")

    x = None
    if b is not None and len(b) == n:
        pasos.append("\n2. Sustitución progresiva (L · y = b):")
        y = sustitucion_adelante(L, b, unos_diagonal=False)
        for i, yi in enumerate(y, 1):
            pasos.append(f"   y{i} = {yi:.6f}")

        pasos.append("\n3. Sustitución regresiva (U · x = y con U[i][i] = 1):")
        x = sustitucion_atras(U, y, unos_diagonal=True)
        for i, xi in enumerate(x, 1):
            pasos.append(f"   x{i} = {xi:.6f}")

    return L, U, x, pasos
