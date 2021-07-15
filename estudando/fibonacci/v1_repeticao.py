def fib(n):
    """
    >>> fib(7)
    13
    >>> fib(3)
    2
    >>> fib(0)
    0
    """
    if n < 1:
        return 0
    elif n <= 2:
        return 1

    fib0, fib1 = 0, 1
    for i in range(2, n+1):
        fibn = fib0 + fib1
        fib0, fib1 = fib1, fibn

    return fibn
