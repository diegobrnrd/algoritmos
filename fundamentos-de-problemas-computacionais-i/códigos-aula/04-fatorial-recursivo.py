def fatorial_recursivo(n):
    if n < 2:
        return 1
    else:
        return n * fatorial_recursivo(n - 1)


if __name__ == '__main__':
    print(fatorial_recursivo(int(input())))
