def fibonacci_recursivo(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursivo(n - 2) + fibonacci_recursivo(n - 1)


if __name__ == '__main__':
    print(fibonacci_recursivo(int(input())))
