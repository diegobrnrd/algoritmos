def sequencia_secreta(n):
    sequencia = [int(input()) for _ in range(n)]
    atual, contador = 2, 0

    for numero in sequencia:
        if numero != atual:
            contador += 1
            atual = numero

    return contador


if __name__ == '__main__':
    print(sequencia_secreta(int(input())))
