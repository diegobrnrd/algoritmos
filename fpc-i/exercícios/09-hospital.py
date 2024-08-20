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


def compara(paciente1, paciente2):
    criterios_paciente1 = (
        -pacientes[paciente1]['plano'], -pacientes[paciente1]['gravidade'], pacientes[paciente1]['nome']
    )
    criterios_paciente2 = (
        -pacientes[paciente2]['plano'], -pacientes[paciente2]['gravidade'], pacientes[paciente2]['nome']
    )

    return criterios_paciente1 < criterios_paciente2


if __name__ == '__main__':
    planos = {'premium': 6, 'diamante': 5, 'ouro': 4, 'prata': 3, 'bronze': 2, 'resto': 1}
    n_pacientes = int(input())

    pacientes = {}
    for k in range(1, n_pacientes + 1):
        nome, plano, gravidade = input().split()
        paciente = {k: {'plano': planos[plano], 'gravidade': int(gravidade), 'nome': nome.lower()}}
        pacientes.update(paciente)

    chaves = list(pacientes.keys())
    quicksort(chaves, 0, len(chaves) - 1)

    for k in chaves:
        print(pacientes[k]['nome'])
