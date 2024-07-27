def insertion_sort(A):
    for j in range(1, len(A)):
        # J será o índice do segundo valor até o último.
        chave = A[j]
        # Chave será o número atual para ser ordenado
        i = j - 1
        # I será o índice do número que será comparado com o atual.
        while i >= 0 and A[i] > chave:
            # Verifica se chegou ao ínicio do vetor e se o número comparado é menor que o atual
            A[i + 1] = A[i]
            # Move o comparado uma posição para direita quando ele é maior que o atual.
            i -= 1
            # Decrementa o índice do comparado.
        A[i + 1] = chave
        # Coloca o atual uma posição a direita do comparado quando o atual é maior que ele.


def central():
    import random
    vetor = [random.randint(1, 10000) for _ in range(10000)]
    insertion_sort(vetor)
    print(vetor)


if __name__ == '__main__':
    import timeit
    tempo_de_execucao = timeit.timeit(central, number=1)
    print(f'Tempo de execução: {tempo_de_execucao} segundos')
