def fibonacci_iterativo(n):
    if n <= 1:
        return n
    else:
        penultimo, ultimo, atual = 0, 1, None
        for _ in range(n - 1):
            atual = penultimo + ultimo
            penultimo, ultimo = ultimo, atual

        return atual


if __name__ == '__main__':
    print(fibonacci_iterativo(int(input())))
