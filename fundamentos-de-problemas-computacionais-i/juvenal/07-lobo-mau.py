def achar_cercas(area, i, j, ovelhas, lobos, t):
    if i < 0 or i >= len(area) or j < 0 or j >= len(area[0]):
        return ovelhas, lobos, t
    if area[i][j] == 'k':
        ovelhas += 1
        area[i][j] = 'x'
        t += 1
    elif area[i][j] == 'v':
        lobos += 1
        area[i][j] = 'x'
        t += 1
    elif area[i][j] == 'x' or area[i][j] == '#':
        return ovelhas, lobos, t

    area[i][j] = 'x'

    ovelhas, lobos, t = achar_cercas(area, i - 1, j, ovelhas, lobos, t)
    ovelhas, lobos, t = achar_cercas(area, i, j - 1, ovelhas, lobos, t)
    ovelhas, lobos, t = achar_cercas(area, i + 1, j, ovelhas, lobos, t)
    ovelhas, lobos, t = achar_cercas(area, i, j + 1, ovelhas, lobos, t)

    return ovelhas, lobos, t


def funcao_principal():
    n_linhas, n_colunas = map(int, input().split())
    total_ovelhas, total_lobos = 0, 0
    area = [list(input()) for _ in range(n_linhas)]

    for i in range(n_linhas):
        for j in range(n_colunas):
            if area[i][j] == 'v' or area[i][j] == 'k':
                lobos, ovelhas, t = 0, 0, 0
                ovelhas, lobos, t = achar_cercas(area, i, j, ovelhas, lobos, t)
                if t > 0:
                    if ovelhas > lobos:
                        total_ovelhas += ovelhas
                    else:
                        total_lobos += lobos

    print(f'{total_ovelhas} {total_lobos}')


if __name__ == '__main__':
    funcao_principal()
