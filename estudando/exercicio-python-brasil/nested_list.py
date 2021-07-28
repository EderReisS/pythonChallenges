
def pegar_nota(lista_notas, posicao=1):
    lista_ordenada = sorted(lista_notas)
    return lista_ordenada[posicao]


def pegar_pos_segunda_menor_nota(segunda_menor_nota, lista_notas):
    return lista_notas.index(segunda_menor_nota)


def pegar_nome_com_segunda_menor_nota(pos_segunda_menor_nota, lista_nomes):
    return lista_nomes[pos_segunda_menor_nota]


def pegar_lista_pos(nota, lista_notas):
    lista_segunda_pos = []
    n_lista = len(lista_notas)
    for pos in range(n_lista):
        if lista_notas[pos] == nota:
            lista_segunda_pos.append(pos)
    return lista_segunda_pos


def pegar_nomes_com_segunda(lista_pos_segunda, lista_nomes):
    lista_nomes_segunda = []
    for pos in lista_pos_segunda:
        nome = lista_nomes[pos]
        lista_nomes_segunda.append(nome)
    return lista_nomes_segunda


def ordernar_lista(nomes_com_segunda):
    return sorted(nomes_com_segunda)


def nested_list(lista_nomes, lista_notas):
    """
    :param lista_nomes: lista de nomes
    :param lista_notas: lista de notas
    :return: nome com a segunda menor nota
    """
    segunda_menor_nota = pegar_segunda_menor_nota(lista_notas)

    lista_pos_segunda = pegar_lista_pos_segunda(segunda_menor_nota, lista_notas)

    nomes_com_segunda = pegar_nomes_com_segunda(lista_pos_segunda, lista_nomes)

    nomes_com_segunda_ordenado = ordernar_lista(nomes_com_segunda)

    return nomes_com_segunda_ordenado


if __name__ == '__main__':
    entrada_nomes = ['Harry', 'Berry', 'Tina', 'Akriti', 'Harsh']
    entrada_notas = [37.21, 37.21, 37.2, 41, 39]
    resposta = ['Berry', 'Harry']

    print()
    print('nested_list execução:', nested_list(lista_nomes=entrada_nomes, lista_notas=entrada_notas))
    print('A função retorna corretamente', resposta == nested_list(entrada_nomes, entrada_notas))
