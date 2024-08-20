def f(n, caso, chamadas_recursivas, maiores_valores):
    if n == 1:
        chamadas_recursivas += 1
        if chamadas_recursivas > maiores_valores[caso]:
            maiores_valores[caso] = chamadas_recursivas
        return maiores_valores
    elif n % 2 == 0:
        return f(n / 2, caso, chamadas_recursivas + 1, maiores_valores)
    else:
        return f(3 * n + 1, caso, chamadas_recursivas + 1, maiores_valores)


def g(intervalos, maiores_valores):
    for caso, intervalo in enumerate(intervalos):
        for numero in range(intervalo[0], intervalo[1] + 1):
            maiores_valores = f(numero, caso, 0, maiores_valores)

    for caso, valor in enumerate(maiores_valores, 1):
        print(f'Caso {caso}: {valor}')


def funcao_principal():
    t = int(input())
    intervalos = [[int(e) for e in input().split()] for _ in range(t)]
    maiores_valores = [0] * t
    g(intervalos, maiores_valores)


if __name__ == '__main__':
    funcao_principal()
