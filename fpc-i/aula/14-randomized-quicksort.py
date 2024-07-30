def randomized_quicksort(arr, p, r):
    if p < r:
        q = partition(arr, p, r)
        randomized_quicksort(arr, p, q - 1)
        randomized_quicksort(arr, q + 1, r)


def randomized_partition(arr, p, r):
    import random

    i = random.randint(p, r)
    arr[r], arr[i] = arr[i], arr[r]
    return partition(arr, p, r)


def partition(arr, p, r):
    x = arr[r]
    i = p - 1
    for j in range(p, r):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1


def central():
    import random

    vetor = [random.randint(1, 10000) for _ in range(10000)]
    randomized_quicksort(vetor, 0, len(vetor) - 1)
    print(vetor)


if __name__ == '__main__':
    import timeit

    tempo_de_execucao = timeit.timeit(central, number=1)
    print(f'Tempo de execução: {tempo_de_execucao} segundos')
