def get_val(perm_string):
    permission_block = {'r': 4, 'w': 2, 'x': 1, '-': 0}
    val = 0
    for c in perm_string:
        val += permission_block[c]
    return str(val)


def symbolic_to_octal(perm_string):
    """
    :param perm_string: (String) UNIX permission string.
    :returns: (int) Numerical representation of given permissions.
    """
    perm_string_list = []  # novo parametro
    val = ''
    for i in range(len(perm_string)//3):
        string = perm_string[3*i: 3*(i+1)]
        val += get_val(string)

    return int(val)


if __name__ == '__main__':

    print(symbolic_to_octal('rwxr-x-w-'))
    """
    rwxr-x-w-
    0-8
    rwx [0, 1, 2]
    r-x [3, 4, 5]
    -w- [6, 7, 8]
    """
    {'a', 'b', 'c'}
    #lista, conjuntos e dicionarios


