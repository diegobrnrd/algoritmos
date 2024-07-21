def multiplicacao(x, n):
    if n == 0:
        return 0
    elif n == 1:
        return x
    else:
        return x + multiplicacao(x, n - 1)


if __name__ == '__main__':
    print(multiplicacao(2, 5))
