def decimal_binario(n):
    if n == 0:
        return '0'
    elif n == 1:
        return '1'
    else:
        return str(n % 2) + decimal_binario(n // 2)


if __name__ == '__main__':
    print(decimal_binario(3))
