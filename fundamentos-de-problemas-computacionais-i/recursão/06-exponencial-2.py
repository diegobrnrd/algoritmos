def exponencial(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        metade = exponencial(x, n // 2)
        return metade * metade
    else:
        return x * exponencial(x, n - 1)


if __name__ == '__main__':
    print(exponencial(5, 2))
