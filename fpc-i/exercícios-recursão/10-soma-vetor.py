def somar_vetor(vetor):
    if len(vetor) == 1:
        return vetor[0]
    else:
        return vetor[0] + somar_vetor(vetor[1:])


if __name__ == '__main__':
    lista = [x for x in range(1, 5)]
    print(somar_vetor(lista))
