def identificar_navio(tabuleiro, i, j, identificador, n_linhas, n_colunas):
    n_celulas_identificadas = 0
    if 0 <= i < n_linhas and 0 <= j < n_colunas:
        if tabuleiro[i][j] == '#':
            tabuleiro[i][j] = identificador
            n_celulas_identificadas += 1
            orientacoes = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for orientacao_i, orientacao_j in orientacoes:
                n_celulas_identificadas += identificar_navio(
                    tabuleiro,
                    i + orientacao_i,
                    j + orientacao_j,
                    identificador,
                    n_linhas,
                    n_colunas
                )

    return n_celulas_identificadas


def contar_navios_destruidos(dict_tamanhos):
    n_navios_destruidos = 0
    for tamanho_navio in dict_tamanhos.values():
        if tamanho_navio == 0:
            n_navios_destruidos += 1

    return n_navios_destruidos


def disparos(tabuleiro, n_disparos, n_linhas, n_colunas):
    identificador = 0
    dict_tamanhos = {}
    for _ in range(n_disparos):
        i, j = [int(i) - 1 for i in input().split()]
        tamanho_navio = identificar_navio(tabuleiro, i, j, identificador, n_linhas, n_colunas)
        if tamanho_navio > 0:
            dict_tamanhos[identificador] = tamanho_navio - 1
            identificador += 1
        elif tabuleiro[i][j] != ".":
            dict_tamanhos[tabuleiro[i][j]] -= 1

    return contar_navios_destruidos(dict_tamanhos)


def funcao_principal():
    n_linhas, n_colunas = map(int, input().split())
    tabuleiro = [list(input()) for _ in range(n_linhas)]
    n_disparos = int(input())
    print(disparos(tabuleiro, n_disparos, n_linhas, n_colunas))


if __name__ == '__main__':
    funcao_principal()
