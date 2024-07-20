def sucessor(a):
    return a + 1


def soma(a, b):
    resultado = a
    for _ in range(b):
        resultado = sucessor(resultado)
    return resultado


def multiplicacao(a, b):
    resultado = 0
    for _ in range(b):
        resultado = soma(resultado, a)
    return resultado


def exponenciacao(a, b):
    resultado = 1
    for _ in range(b):
        resultado = multiplicacao(resultado, a)
    return resultado


if __name__ == '__main__':
    print(soma(5, 2))
    print(multiplicacao(5, 2))
    print(exponenciacao(5, 2))
