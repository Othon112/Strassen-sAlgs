#Othón Berlanga Calderón - A01660663

def split(matrix):
    """Divide una matriz cuadrada en cuatro submatrices iguales.

    Args:
        matrix (list[list[int]]): Matriz cuadrada a dividir.

    Returns:
        tuple: Cuatro submatrices, cada una correspondiente a un cuadrante de la matriz original.
    """
    size = len(matrix)
    mid = size // 2
    return [row[:mid] for row in matrix[:mid]], [row[mid:] for row in matrix[:mid]], \
           [row[:mid] for row in matrix[mid:]], [row[mid:] for row in matrix[mid:]]


def add_matrices(a, b):
    """Suma dos matrices del mismo tamaño.

    Args:
        a (list[list[int]]): Primera matriz.
        b (list[list[int]]): Segunda matriz.

    Returns:
        list[list[int]]: Matriz resultante de la suma de `a` y `b`.
    """
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def subtract_matrices(a, b):
    """Resta dos matrices del mismo tamaño.

    Args:
        a (list[list[int]]): Primera matriz.
        b (list[list[int]]): Segunda matriz.

    Returns:
        list[list[int]]: Matriz resultante de la resta de `b` a `a`.
    """
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def strassen(x, y):
    """Realiza la multiplicación de matrices utilizando el algoritmo de Strassen.

    Args:
        x (list[list[int]]): Primera matriz a multiplicar.
        y (list[list[int]]): Segunda matriz a multiplicar.

    Returns:
        list[list[int]]: Matriz resultante de la multiplicación de `x` y `y` utilizando el algoritmo de Strassen.

    Raises:
        ValueError: Si las dimensiones de las matrices no son potencias de dos.
    """
    size = len(x)
    
    # Verificar si las dimensiones son potencias de dos
    if (size & (size - 1) != 0) or (len(y) & (len(y) - 1) != 0) or \
       (len(x[0]) & (len(x[0]) - 1) != 0) or (len(y[0]) & (len(y[0]) - 1) != 0):
        raise ValueError("Matrix dimensions must be a power of two")
    
    if size == 1:
        return [[x[0][0] * y[0][0]]]
    
    a, b, c, d = split(x)
    e, f, g, h = split(y)
    
    p1 = strassen(a, subtract_matrices(f, h))
    p2 = strassen(add_matrices(a, b), h)
    p3 = strassen(add_matrices(c, d), e)
    p4 = strassen(d, subtract_matrices(g, e))
    p5 = strassen(add_matrices(a, d), add_matrices(e, h))
    p6 = strassen(subtract_matrices(b, d), add_matrices(g, h))
    p7 = strassen(subtract_matrices(a, c), add_matrices(e, f))
    
    c11 = add_matrices(subtract_matrices(add_matrices(p5, p4), p2), p6)
    c12 = add_matrices(p1, p2)
    c21 = add_matrices(p3, p4)
    c22 = subtract_matrices(subtract_matrices(add_matrices(p1, p5), p3), p7)
    
    upper_half = [c11[i] + c12[i] for i in range(len(c11))]
    lower_half = [c21[i] + c22[i] for i in range(len(c21))]
    
    return upper_half + lower_half
