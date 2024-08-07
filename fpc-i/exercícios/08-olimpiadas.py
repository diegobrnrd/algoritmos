def quicksort(arr, p, r):
    if p < r:
        q = partition(arr, p, r)
        quicksort(arr, p, q - 1)
        quicksort(arr, q + 1, r)


def partition(arr, p, r):
    x = arr[r]
    i = p - 1
    for j in range(p, r):
        if compara(arr[j], x):
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1


def compara(pais1, pais2):
    criterios_pais1 = (medalhas_paises[pais1][1], medalhas_paises[pais1][2], medalhas_paises[pais1][3], -pais1)
    criterios_pais2 = (medalhas_paises[pais2][1], medalhas_paises[pais2][2], medalhas_paises[pais2][3], -pais2)

    return criterios_pais1 > criterios_pais2


if __name__ == '__main__':
    n_paises, n_modalidade = map(int, input().split())
    modalidades = [[int(x) for x in input().split()] for _ in range(n_modalidade)]
    medalhas_paises = {x: {1: 0, 2: 0, 3: 0} for x in range(1, n_paises + 1)}

    for modalidade in modalidades:
        for tipo, pais in enumerate(modalidade, 1):
            medalhas_paises[pais][tipo] += 1

    paises = list(medalhas_paises.keys())
    quicksort(paises, 0, len(paises) - 1)

    print(" ".join(map(str, paises)))
