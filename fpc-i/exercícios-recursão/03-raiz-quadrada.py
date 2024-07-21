def raiz_quadrada(x, x0, e):
    if abs(x0 ** 2 - x) <= e:
        return x0
    else:
        return raiz_quadrada(x, ((x0 ** 2 + x) / (2 * x0)), e)


if __name__ == '__main__':
    print(raiz_quadrada(13, 3.2, 0.001))
