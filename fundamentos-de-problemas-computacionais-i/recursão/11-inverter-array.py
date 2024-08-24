def inverter_array(vetor, es, di):
    if es >= di:
        return vetor
    else:
        temp = vetor[es]
        vetor[es] = vetor[di]
        vetor[di] = temp
        return inverter_array(vetor, es + 1, di - 1)


if __name__ == '__main__':
    lista = [x for x in range(3)]
    print(inverter_array(lista, 0, len(lista) - 1))
