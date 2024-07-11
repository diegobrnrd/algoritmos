def descobrir_idade():
    idades = [0 for _ in range(4)]

    for x in range(3):
        idades[x] = int(input())

    idades[3] = idades[0] - (idades[1] + idades[2])
    idades.sort()

    return idades[2]


if __name__ == '__main__':
    print(descobrir_idade())
