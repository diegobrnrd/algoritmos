def somar_array(vetor, i):
    if i == -1:
        return 0
    else:
        return vetor[i] + somar_array(vetor, i - 1)


if __name__ == '__main__':
    lista = [x for x in range(1, 5)]
    print(somar_array(lista, len(lista) - 1))
