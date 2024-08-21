def lcs():
    s = 'BACBAD' # Linha.
    t = 'ABAZDC' # Coluna.

    tab = [[0 for _ in range(len(s) + 1)] for _ in range(len(t) + 1)]

    for i in range(1, len(t) + 1):
        for j in range(1, len(s) + 1):
            if t[i - 1] != s[j - 1]:
                tab[i][j] = max(tab[i - 1][j], tab[i][j - 1])
            else:
                tab[i][j] = 1 + tab[i - 1][j - 1]

    lcs_lista = []
    i, j = len(t), len(s)
    while i > 0 and j > 0:
        if t[i - 1] == s[j - 1]:
            lcs_lista.append(t[i - 1])
            i -= 1
            j -= 1
        elif tab[i - 1][j] > tab[i][j - 1]:
            i -= 1
        else:
            j -= 1

    lcs_str = ''.join(lcs_lista)
    return lcs_str[::-1]


if __name__ == '__main__':
    print(lcs())
