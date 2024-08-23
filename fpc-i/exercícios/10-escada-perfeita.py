def somatorio(lista_colunas):
    soma = 0
    for i in lista_colunas:
        soma += i
    return soma


def tamanho_escada_perfeita(n_colunas):
    return int(n_colunas * (n_colunas + 1) // 2)


def contar_movimentos(lista_colunas, n_colunas, base):
    n_movimentos = 0
    blocos_por_coluna = base // n_colunas
    for i in range(n_colunas):
        desejado = i + 1 + blocos_por_coluna
        if lista_colunas[i] > desejado:
            n_movimentos += lista_colunas[i] - desejado

    return n_movimentos


def funcao_principal():
    n_colunas = int(input())
    lista_colunas = [int(i) for i in input().split()]
    n_blocos = somatorio(lista_colunas)
    tamanho_escada = tamanho_escada_perfeita(n_colunas)
    base = n_blocos - tamanho_escada
    if base % n_colunas != 0:
        return -1
    else:
        return contar_movimentos(lista_colunas, n_colunas, base)


if __name__ == '__main__':
    print(funcao_principal())
