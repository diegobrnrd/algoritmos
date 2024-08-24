def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def central():
    import random

    vetor = [random.randint(1, 10000) for _ in range(10000)]
    bubble_sort(vetor)
    print(vetor)


if __name__ == '__main__':
    import timeit

    tempo_de_execucao = timeit.timeit(central, number=1)
    print(f'Tempo de execução: {tempo_de_execucao} segundos')
