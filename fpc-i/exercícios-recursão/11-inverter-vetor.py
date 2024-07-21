def inverter_vetor(vetor, es, di):
    if es >= di:
        return vetor
    else:
        temp = vetor[es]
        vetor[es] = vetor[di]
        vetor[di] = temp
        return inverter_vetor(vetor, es + 1, di - 1)


if __name__ == '__main__':
    lista = [x for x in range(3)]
    print(inverter_vetor(lista, 0, len(lista) - 1))
