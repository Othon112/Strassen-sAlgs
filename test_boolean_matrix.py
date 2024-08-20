#Othón Berlanga Calderón - A01660663
import pytest

from boolean_matrix import split, add_matrices, strassen_boolean

def test_split():
    matrix = [
        [True, False, True, False],
        [False, True, False, True],
        [True, False, True, False],
        [False, True, False, True]
    ]
    a, b, c, d = split(matrix)
    
    assert a == [[True, False], [False, True]]
    assert b == [[True, False], [False, True]]
    assert c == [[True, False], [False, True]]
    assert d == [[True, False], [False, True]]

def test_add_matrices():
    a = [
        [True, False],
        [False, True]
    ]
    b = [
        [False, True],
        [True, False]
    ]
    result = add_matrices(a, b)
    
    assert result == [
        [True, True],
        [True, True]
    ]

def test_strassen_boolean():
    x = [
        [True, False],
        [False, True]
    ]
    y = [
        [False, True],
        [True, False]
    ]
    
    result = strassen_boolean(x, y)
    
    assert result == [
        [True, True],
        [True, True]
    ]

    
    # Test for zero matrices
    x_zero = [
        [False, False],
        [False, False]
    ]
    y_zero = [
        [False, False],
        [False, False]
    ]
    
    result_zero = strassen_boolean(x_zero, y_zero)
    
    assert result_zero == [
        [False, False],
        [False, False]
    ]


