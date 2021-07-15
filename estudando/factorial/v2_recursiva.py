import time


def factorial(n: int):
    """
    >>> factorial(5)
    120
    >>> factorial(4)
    24
    """
    if n == 1 or n == 0:
        return 1
    return n * factorial(n-1)


if __name__ == '__main__':
    init = time.time()
    print(factorial(100))
    elapsed = time.time() - init
    print(f"tempo {elapsed}")