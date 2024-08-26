def contar_cruzamentos():
    n = int(input())
    horizontal = [int(x) for x in input().split()]

    cruzamentos = 0

    for i in range(n):
        for j in range(i + 1, n):
            if horizontal[i] > horizontal[j]:
                cruzamentos += 1

    return cruzamentos


if __name__ == '__main__':
    print(contar_cruzamentos())
