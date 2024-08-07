def heapsort(a):
    build_max_heap(a)
    tamanho_do_heap = len(a)
    for i in range(len(a) - 1, 0, -1):
        a[0], a[i] = a[i], a[0]
        tamanho_do_heap -= 1
        max_heapify(a, 0, tamanho_do_heap)


def build_max_heap(a):
    tamanho_do_heap = len(a)
    for i in range(len(a) // 2 - 1, -1, -1):
        max_heapify(a, i, tamanho_do_heap)


def max_heapify(a, i, tamanho_do_heap):
    l = 2 * i + 1
    r = 2 * i + 2
    maior = i
    if l < tamanho_do_heap and a[l] > a[maior]:
        maior = l
    if r < tamanho_do_heap and a[r] > a[maior]:
        maior = r
    if maior != i:
        a[i], a[maior] = a[maior], a[i]
        max_heapify(a, maior, tamanho_do_heap)


def central():
    import random

    vetor = [random.randint(1, 10000) for _ in range(10000)]
    heapsort(vetor)
    print(vetor)


if __name__ == '__main__':
    import timeit

    tempo_de_execucao = timeit.timeit(central, number=1)
    print(f'Tempo de execução: {tempo_de_execucao} segundos')
