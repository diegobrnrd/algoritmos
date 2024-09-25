def fatorial(n):
    fat = 1
    for x in range(1, n + 1):
        fat *= x
    return fat


def comb(n, k):
    return fatorial(n) / (fatorial(k) * fatorial(n - k))


if __name__ == '__main__':
    print(comb(5, 3))
