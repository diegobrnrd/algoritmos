def peca_perdida():
    total_pecas = sum(int(x) for x in range(1, int(input()) + 1))
    minhas_pecas = sum(int(x) for x in input().split())
    print(total_pecas - minhas_pecas)


if __name__ == '__main__':
    peca_perdida()
