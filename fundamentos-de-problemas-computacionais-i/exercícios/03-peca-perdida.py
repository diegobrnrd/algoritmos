def peca_perdida():
    total_pecas = sum(int(p) for p in range(1, int(input()) + 1))
    minhas_pecas = sum(int(p) for p in input().split())
    return total_pecas - minhas_pecas


if __name__ == '__main__':
    print(peca_perdida())
