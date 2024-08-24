def juntar_arrays(array, array_2):
    if not array:
        return array_2
    elif not array_2:
        return array
    else:
        return [array[0]] + juntar_arrays(array[1:], array_2)


if __name__ == '__main__':
    lista = [2, 3, 7, 8, 1]
    lista_2 = [4, 5, 6, 9, 0]
    print(juntar_arrays(lista, lista_2))
