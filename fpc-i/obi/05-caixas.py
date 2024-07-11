def calcular_viagem(caixas):
    a, b, c = caixas
    if a == b == c:
        return 3
    elif a < b < c:
        return 1
    elif a == b < c:
        if (a + b) < c:
            return 1
        else:
            return 2
    elif a < b == c:
        return 2


if __name__ == '__main__':
    lista_caixas = [int(input()) for _ in range(3)]
    print(calcular_viagem(lista_caixas))
