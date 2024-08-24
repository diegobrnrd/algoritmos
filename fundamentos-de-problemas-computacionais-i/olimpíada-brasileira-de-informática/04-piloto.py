def piloto_automatico(distancias):
    a, b, c = distancias
    if (b - a) < (c - b):
        return 1
    elif (b - a) > (c - b):
        return -1
    else:
        return 0


if __name__ == '__main__':
    lista_distancias = [int(input()) for _ in range(3)]
    print(piloto_automatico(lista_distancias))
