def somatorio(lista_colunas):
    soma = 0
    for i in lista_colunas:
        soma += i
    return soma


def tamanho_escada_perfeita(n_colunas):
    """Calcula o número total de blocos necessários para formar uma escada perfeita com n_colunas."""
    return int(n_colunas * (n_colunas + 1) // 2)


def contar_movimentos(lista_colunas, n_colunas, base):
    n_movimentos = 0
    # Número de blocos por coluna.
    blocos_por_coluna = base // n_colunas
    for i in range(n_colunas):
        # Calcula o número de blocos desejado na coluna i.
        desejado = i + 1 + blocos_por_coluna
        if lista_colunas[i] > desejado:
            # Soma a diferença se a coluna atual tiver mais blocos do que o desejado.
            n_movimentos += lista_colunas[i] - desejado

    return n_movimentos


def funcao_principal():
    n_colunas = int(input())
    lista_colunas = [int(i) for i in input().split()]
    n_blocos = somatorio(lista_colunas)
    tamanho_escada = tamanho_escada_perfeita(n_colunas)
    # Calcula o número de blocos extras disponíveis após formar uma escada perfeita.
    base = n_blocos - tamanho_escada
    # Verifica se é possível distribuir os blocos extras igualmente entre as colunas.
    if base % n_colunas != 0:
        return -1
    else:
        return contar_movimentos(lista_colunas, n_colunas, base)


if __name__ == '__main__':
    print(funcao_principal())
