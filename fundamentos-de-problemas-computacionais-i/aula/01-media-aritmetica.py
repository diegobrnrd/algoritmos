def media_aritmetica():
    valores = [float(x) for x in input().split()]
    n = sum(1 for _ in valores)
    soma_valores = sum(x for x in valores)
    print(f'Média: {soma_valores / n}')


if __name__ == '__main__':
    media_aritmetica()
