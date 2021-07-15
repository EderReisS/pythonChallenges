import time


def factorial(n: int):
    """
    >>> factorial(5)
    120
    >>> factorial(4)
    24
    """
    resultado = 1
    for i in range(1, n + 1):
        resultado = resultado * i
    return resultado


if __name__ == '__main__':
    init = time.time()
    print(factorial(1_000_000))
    elapsed = time.time() - init
    print(f"tempo {elapsed}")