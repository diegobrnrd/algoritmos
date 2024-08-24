def quicksort(arr, p, r):
    if p < r:
        q = partition(arr, p, r)
        quicksort(arr, p, q - 1)
        quicksort(arr, q + 1, r)


def partition(arr, p, r):
    x = arr[r]
    i = p - 1
    for j in range(p, r):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1


def organizar_arquivos(limite_pasta, lista_arquivos):
    n_pastas = 0
    i, j = 0, len(lista_arquivos) - 1
    while i <= j:
        # Se a soma de dois arquivos for menor ou igual ao limite, ambos são adicionados na mesma pasta.
        if lista_arquivos[i] + lista_arquivos[j] <= limite_pasta:
            n_pastas += 1
            i += 1
            j -= 1
        # Caso contrário, apenas o maior arquivo é adicionado na pasta.
        else:
            n_pastas += 1
            j -= 1

    return n_pastas


def funcao_princial():
    n_arquivos, limite_pasta = map(int, input().split())
    lista_arquivos = [int(x) for x in input().split()]
    quicksort(lista_arquivos, 0, len(lista_arquivos) - 1)
    print(organizar_arquivos(limite_pasta, lista_arquivos))


if __name__ == '__main__':
    funcao_princial()
