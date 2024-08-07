def heapsort(arr):
    build_max_heap(arr)
    tamanho_do_heap = len(arr)
    for i in range(len(arr) - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        tamanho_do_heap -= 1
        max_heapify(arr, 0, tamanho_do_heap)


def build_max_heap(arr):
    tamanho_do_heap = len(arr)
    for i in range(len(arr) // 2 - 1, -1, -1):
        max_heapify(arr, i, tamanho_do_heap)


def max_heapify(arr, i, tamanho_do_heap):
    l = 2 * i + 1
    r = 2 * i + 2
    maior = i
    if l < tamanho_do_heap and arr[l] > arr[maior]:
        maior = l
    if r < tamanho_do_heap and arr[r] > arr[maior]:
        maior = r
    if maior != i:
        arr[i], arr[maior] = arr[maior], arr[i]
        max_heapify(arr, maior, tamanho_do_heap)


def central():
    import random

    vetor = [random.randint(1, 10000) for _ in range(10000)]
    heapsort(vetor)
    print(vetor)


if __name__ == '__main__':
    import timeit

    tempo_de_execucao = timeit.timeit(central, number=1)
    print(f'Tempo de execução: {tempo_de_execucao} segundos')
