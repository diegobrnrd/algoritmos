def par_impar(p):
    if p == 0:
        par, impar = 0, 1
    else:
        par, impar = 1, 0

    soma = sum(int(input()) for _ in range(2))

    if soma % 2 == 0:
        return par
    else:
        return impar


if __name__ == '__main__':
    print(par_impar(int(input())))
