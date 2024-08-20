#Othón Berlanga Calderón - A01660663
def split(matrix):
    """Divide una matriz cuadrada en cuatro submatrices iguales.

    Args:
        matrix (list[list[bool]]): Matriz cuadrada booleana a dividir.

    Returns:
        tuple: Cuatro submatrices booleanas, cada una correspondiente a un cuadrante de la matriz original.
    """
    size = len(matrix)
    mid = size // 2
    return [row[:mid] for row in matrix[:mid]], [row[mid:] for row in matrix[:mid]], \
           [row[:mid] for row in matrix[mid:]], [row[mid:] for row in matrix[mid:]]


def add_matrices(a, b):
    """Realiza la operación OR elemento por elemento entre dos matrices booleanas.

    Args:
        a (list[list[bool]]): Primera matriz booleana.
        b (list[list[bool]]): Segunda matriz booleana.

    Returns:
        list[list[bool]]: Matriz resultante de la operación OR entre `a` y `b`.
    """
    return [[a[i][j] or b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def strassen_boolean(x, y):
    """Multiplica dos matrices booleanas usando el algoritmo de Strassen.

    Args:
        x (list[list[bool]]): Primera matriz booleana.
        y (list[list[bool]]): Segunda matriz booleana.

    Returns:
        list[list[bool]]: Matriz booleana resultante de la multiplicación.
    """
    size = len(x)
    
    # Verificar si las dimensiones son potencias de dos
    if (size & (size - 1) != 0) or (len(y) & (len(y) - 1) != 0) or \
       (len(x[0]) & (len(x[0]) - 1) != 0) or (len(y[0]) & (len(y[0]) - 1) != 0):
        raise ValueError("Matrix dimensions must be a power of two")
    
    if size == 1:
        return [[x[0][0] and y[0][0]]]
    
    a, b, c, d = split(x)
    e, f, g, h = split(y)
    
    p1 = strassen_boolean(a, add_matrices(f, h))  # (f OR h)
    p2 = strassen_boolean(add_matrices(a, b), h)  # (a OR b)
    p3 = strassen_boolean(add_matrices(c, d), e)  # (c OR d)
    p4 = strassen_boolean(d, add_matrices(g, e))  # (g OR e)
    p5 = strassen_boolean(add_matrices(a, d), add_matrices(e, h))  # (a OR d) AND (e OR h)
    p6 = strassen_boolean(add_matrices(b, d), add_matrices(g, h))  # (b OR d) AND (g OR h)
    p7 = strassen_boolean(add_matrices(a, c), add_matrices(e, f))  # (a OR c) AND (e OR f)
    
    c11 = add_matrices(add_matrices(p5, p4), p6)  # (p5 OR p4) AND p6
    c12 = add_matrices(p1, p2)  # p1 OR p2
    c21 = add_matrices(p3, p4)  # p3 OR p4
    c22 = add_matrices(add_matrices(p5, p3), p7)  # (p5 OR p3) AND p7
    
    upper_half = [c11[i] + c12[i] for i in range(len(c11))]
    lower_half = [c21[i] + c22[i] for i in range(len(c21))]
    
    return upper_half + lower_half
