def f(n):
    if n < 4:
        return 3 * n
    else:
        return 2 * f(n - 4) + 5


if __name__ == '__main__':
    print(f(3))
    print(f(7))
