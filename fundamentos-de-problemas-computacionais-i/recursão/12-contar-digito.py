def contar_digito(n, k):
    if n == 0:
        return 0
    else:
        return contar_digito(n // 10, k) + (n % 10 == k)


if __name__ == '__main__':
    print(contar_digito(762021192,  2))
