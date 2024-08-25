def levenshtein(s, t):
    tab = [[0 for _ in range(len(s) + 1)] for _ in range(len(t) + 1)]

    for i in range(len(t) + 1):
        tab[i][0] = i
    for j in range(len(s) + 1):
        tab[0][j] = j

    for i in range(1, len(t) + 1):
        for j in range(1, len(s) + 1):
            if t[i - 1] == s[j - 1]:
                c = 0
            else:
                c = 1
            tab[i][j] = min(tab[i - 1][j - 1] + c,
                            tab[i - 1][j] + 1,
                            tab[i][j - 1] + 1)

    return tab[len(t)][len(s)]


def funcao_principal():
    n_palavras_dicionario, n_palavras_analisar = map(int, input().split())
    dicionario = [input() for _ in range(n_palavras_dicionario)]
    analisar = [input() for _ in range(n_palavras_analisar)]
    for palavra_a in analisar:
        palavras_encontradas = []
        for palavra_d in dicionario:
            distancia = levenshtein(palavra_a, palavra_d)
            if distancia <= 2:
                palavras_encontradas.append(palavra_d)
        if len(palavras_encontradas) == 0:
            print()
        else:
            print(' '.join(palavras_encontradas))


if __name__ == '__main__':
    funcao_principal()
