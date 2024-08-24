def somar_linhas_colunas(n, quadrado, identificador):
    if identificador == 'linha':
        soma_das_linhas = [0] * n
        for i, l in enumerate(quadrado):
            for c in l:
                soma_das_linhas[i] += c
        return soma_das_linhas

    else:
        soma_das_colunas = [0] * n
        for l in quadrado:
            for i, c in enumerate(l):
                soma_das_colunas[i] += c
        return soma_das_colunas


def contar(vetor, item):
    quantidade = sum(1 for x in vetor if x == item)
    return quantidade


def funcao_principal():
    n = int(input())
    quadrado = [[int(x) for x in input().split()] for _ in range(n)]
    soma_das_linhas = somar_linhas_colunas(n, quadrado, 'linha')
    soma_das_colunas = somar_linhas_colunas(n, quadrado, 'coluna')

    linha_errada, coluna_errada, soma_errada, soma_correta = None, None, None, None
    for l in range(n):
        if linha_errada is not None and soma_errada is not None and soma_correta is not None:
            break
        elif contar(soma_das_linhas, soma_das_linhas[l]) == 1:
            linha_errada = l
            soma_errada = soma_das_linhas[l]

        elif contar(soma_das_linhas, soma_das_linhas[l]) > 1:
            soma_correta = soma_das_linhas[l]

    for c in range(n):
        if coluna_errada is not None:
            break
        elif contar(soma_das_colunas, soma_das_colunas[c]) == 1:
            coluna_errada = c

    valor_correto = quadrado[linha_errada][coluna_errada] - (soma_errada - soma_correta)
    valor_alterado = quadrado[linha_errada][coluna_errada]

    print(f'{valor_correto} {valor_alterado}')


if __name__ == '__main__':
    funcao_principal()
