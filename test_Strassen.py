#Othón Berlanga Calderón - A01660663
import pytest
from Strassen import strassen

def test_strassen_base_case():
    """esta funcion hace algo
    othon is ga

    Args:
        a (int): primer numero
    Return:
        None: el resultado magic
    """
    # Caso base: matrices de 1x1
    x = [[1]]
    y = [[2]]
    result = strassen(x, y)
    expected = [[2]]
    assert result == expected

def test_strassen_2x2():
    # Caso 2x2
    x = [[1, 2], 
         [3, 4]]
    y = [[5, 6],
         [7, 8]]
    result = strassen(x, y)
    expected = [[19, 22],
                [43, 50]]
    assert result == expected

def test_strassen_4x4():
    # Caso 4x4
    x = [[1, 2, 3, 4], 
         [5, 6, 7, 8], 
         [9, 10, 11, 12], 
         [13, 14, 15, 16]]
    
    y = [[17, 18, 19, 20], 
         [21, 22, 23, 24], 
         [25, 26, 27, 28], 
         [29, 30, 31, 32]]
    
    result = strassen(x, y)
    expected = [[250, 260, 270, 280],
                [618, 644, 670, 696],
                [986, 1028, 1070, 1112],
                [1354, 1412, 1470, 1528]]
    assert result == expected

def test_strassen_non_power_of_two():
    x = [[1, 2, 3], 
         [4, 5, 6], 
         [7, 8, 9]]
    
    y = [[9, 8, 7], 
         [6, 5, 4], 
         [3, 2, 1]]
    
    with pytest.raises(ValueError, match="Matrix dimensions must be a power of two"):
        strassen(x, y)

def test_strassen_large_matrices():
    # Caso de matrices grandes
    from random import randint
    
    x = [[randint(1, 10) for _ in range(8)] for _ in range(8)]
    y = [[randint(1, 10) for _ in range(8)] for _ in range(8)]
    result = strassen(x, y)
    expected = [[sum(x[i][k] * y[k][j] for k in range(8)) for j in range(8)] for i in range(8)]
    assert result == expected

def test_strassen_sample_array():
    x = [[1,1,1,1],
         [2,2,2,2],
         [3,3,3,3],
         [2,2,2,2]]

    y = [[1,1,1,1],
         [2,2,2,2],
         [3,3,3,3],
         [2,2,2,2]]

    expected = [[8,8,8,8],
                [16,16,16,16],
                [24,24,24,24],
                [16,16,16,16]]
    
    result = strassen(x, y)
    assert result == expected
