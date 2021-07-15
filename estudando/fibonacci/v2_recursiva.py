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

    return fib(n-1) + fib(n-2)
