def levenshtein():
    s = 'ONTOLOGICO' # linha.
    t = 'ANTOLOGIA' # coluna.

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
                            tab[i][j - 1] + 1) # Substituição, exclusão e inserção.

    return tab[len(t)][len(s)]


if __name__ == '__main__':
    print(levenshtein())
