def colher_cajus(l, c, m, n, matriz):
    tab = [[0 for _ in range(c)] for _ in range(l)]
    for i in range(l):
        for j in range(c):
            if i == 0 and j == 0:
                tab[i][j] = matriz[i][j]
            elif i == 0 and j != 0:
                tab[i][j] = tab[i][j - 1] + matriz[i][j]
            elif i != 0 and j == 0:
                tab[i][j] = tab[i - 1][j] + matriz[i][j]
            else:
                tab[i][j] = tab[i - 1][j] + tab[i][j - 1] + matriz[i][j] - tab[i - 1][j - 1]

    cajus_colhidos = 0
    for i in range(l):
        for j in range(c):
            if i - m < 0 and j - n < 0:
                atual_colhidos = tab[i][j]
                cajus_colhidos = max(atual_colhidos, cajus_colhidos)
            elif i - m < 0:
                autal_colhidos = tab[i][j] - tab[i][j - n]
                cajus_colhidos = max(autal_colhidos, cajus_colhidos)
            elif j - n < 0:
                autal_colhidos = tab[i][j] - tab[i - m][j]
                cajus_colhidos = max(autal_colhidos, cajus_colhidos)
            else:
                autal_colhidos = tab[i][j] - tab[i][j - n] - tab[i - m][j] + tab[i - m][j - n]
                cajus_colhidos = max(autal_colhidos, cajus_colhidos)

    return cajus_colhidos


def funcao_principal():
    l, c, m, n = map(int, input().split())
    matriz = [[int(x) for x in input().split()] for _ in range(l)]
    print(colher_cajus(l, c, m, n, matriz))


if __name__ == '__main__':
    funcao_principal()
