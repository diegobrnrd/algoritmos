def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    esquerda = [x for x in arr if x < pivot]
    meio = [x for x in arr if x == pivot]
    direita = [x for x in arr if x > pivot]
    return quick_sort(esquerda) + meio + quick_sort(direita)


def central():
    import random

    vetor = [random.randint(1, 10000) for _ in range(10000)]
    novo = quick_sort(vetor)
    print(novo)


if __name__ == '__main__':
    import timeit

    tempo_de_execucao = timeit.timeit(central, number=1)
    print(f'Tempo de execução: {tempo_de_execucao} segundos')
