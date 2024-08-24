def verificacao_escher(alturas, i):
    controle = i

    for m, a in enumerate(alturas):
        if m == controle:
            return 'S'
        elif a + alturas[i] == alturas[m + 1] + alturas[i - 1]:
            i -= 1
        else:
            return 'N'


if __name__ == '__main__':
    n = int(input())
    lista_alturas = [int(x) for x in input().split()]
    print(verificacao_escher(lista_alturas, n - 1))
