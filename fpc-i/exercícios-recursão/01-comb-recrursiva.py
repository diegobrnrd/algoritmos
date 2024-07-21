def comb(n, k):
    if k == 1:
        return n
    elif k == n:
        return 1
    elif 1 < k < n:
        return comb(n - 1, k - 1) + comb(n - 1, k)


if __name__ == '__main__':
    print(comb(5, 3))
