def bubble_sort(A):
    n = len(A)
    # Número de elementos.
    for i in range(n):
        # I será a quantidade de vezes o vetor é percorrido.
        for j in range(0, n - i - 1):
            # J será o índice de comparação.
            # Ele vai do ínicio até o "fim".
            # A janela de comparação diminui a cada rodada do primeiro for.
            if A[j] > A[j + 1]:
                # Compara se o atual é maior que o posterior.
                A[j], A[j + 1] = A[j + 1], A[j]
                # Caso sim, flutua o maior para direita.


def central():
    import random
    vetor = [random.randint(1, 10000) for _ in range(10000)]
    bubble_sort(vetor)
    print(vetor)


if __name__ == '__main__':
    import timeit
    tempo_de_execucao = timeit.timeit(central, number=1)
    print(f'Tempo de execução: {tempo_de_execucao} segundos')
