"""
1. Faça um programa para imprimir:
    1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n  ... n
"""

"""
str, int, float, bool, list, dict, set, tuple, object, ...
"""


def imprir_piramide(n: int):
    """
    >>> imprir_piramide(2)
    1
    2 2
    >>> imprir_piramide(5)
    1
    2 2
    3 3 3
    4 4 4 4
    5 5 5 5 5
    """
    for i in range(1, n + 1):
        valor = f'{i} '*i
        print(valor.strip())


if __name__ == '__main__':
    imprir_piramide(10)
