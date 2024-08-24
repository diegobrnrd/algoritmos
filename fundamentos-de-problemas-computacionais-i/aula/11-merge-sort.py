def merge_sort(arr, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(arr, p, q)
        merge_sort(arr, q + 1, r)
        merge(arr, p, q, r)


def merge(arr, p, q, r):
    l_array = arr[p:q + 1] + [float('inf')]
    r_array = arr[q + 1:r + 1] + [float('inf')]

    i = 0
    j = 0

    for k in range(p, r + 1):
        if l_array[i] <= r_array[j]:
            arr[k] = l_array[i]
            i += 1
        else:
            arr[k] = r_array[j]
            j += 1


def central():
    import random

    vetor = [random.randint(1, 10000) for _ in range(10000)]
    merge_sort(vetor, 0, len(vetor) - 1)
    print(vetor)


if __name__ == '__main__':
    import timeit

    tempo_de_execucao = timeit.timeit(central, number=1)
    print(f'Tempo de execução: {tempo_de_execucao} segundos')
