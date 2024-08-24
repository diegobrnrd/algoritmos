def permutacoes(simbolos):
    if len(simbolos) == 0:
        return ['']

    resultado = []

    for i in range(len(simbolos)):
        primeiro_simbolo = simbolos[i]
        simbolos_restantes = simbolos[:i] + simbolos[i + 1:]

        for per in permutacoes(simbolos_restantes):
            resultado.append(primeiro_simbolo + per)

    return resultado


if __name__ == '__main__':
    lista_simbolos = ['D', 'H', 'F']
    print(permutacoes(lista_simbolos))
