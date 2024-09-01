def maior(x, y):
    return x if x > y else y


def funcao_principal():
    n_planos, n_planetas = map(int, input().split())

    planos = [[int(x) for x in input().split()] for _ in range(n_planos)]
    regioes = {}
    planetas = 0

    for _ in range(n_planetas):
        x, y, z = map(int, input().split())
        chave = ''

        for plano in planos:
            a, b, c, d = plano
            if (a * x) + (b * y) + (c * z) > d:
                chave += '1'
            else:
                chave += '0'

        regiao = int(chave, 2)
        if regiao not in regioes:
            regioes[regiao] = 0
        regioes[regiao] += 1
        planetas = maior(planetas, regioes[regiao])

    print(planetas)


if __name__ == '__main__':
    funcao_principal()