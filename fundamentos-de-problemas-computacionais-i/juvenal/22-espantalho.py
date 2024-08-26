def ronda(n_estacao, estacao_prox, comandos):
    vezes = 0
    localizacao = 1
    if localizacao == estacao_prox:
        vezes += 1
    for c in comandos:
        localizacao += c
        if localizacao > n_estacao:
            localizacao = 1
        elif localizacao < 1:
            localizacao = n_estacao
        if localizacao == estacao_prox:
            vezes += 1

    return vezes


def funcao_principal():
    n_estacao, n_comandos, estacao_prox = map(int, input().split())
    comandos = [int(x) for x in input().split()]
    print(ronda(n_estacao, estacao_prox, comandos))


if __name__ == '__main__':
    funcao_principal()
