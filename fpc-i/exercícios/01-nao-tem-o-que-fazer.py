def f(n, caso, chamadas_recursivas):
    if n == 1:
        g(caso, chamadas_recursivas)
    elif n % 2 == 0:
        f(n / 2, caso, chamadas_recursivas + 1)
    else:
        f(3 * n + 1, caso, chamadas_recursivas + 1)


def g(caso, chamadas_recursivas):
    global maiores_valores
    if chamadas_recursivas > maiores_valores[caso]:
        maiores_valores[caso] = chamadas_recursivas


def saida(maiores):
    for x, valor in enumerate(maiores, 1):
        print(f'Caso {x}: {valor}')


if __name__ == '__main__':
    t = int(input())
    intervalos = [[int(x) for x in input().split()] for _ in range(t)]
    maiores_valores = [0] * t

    for i, intervalo in enumerate(intervalos):
        for numero in range(intervalo[0], intervalo[1] + 1):
            f(numero, i, 1)

    saida(maiores_valores)
