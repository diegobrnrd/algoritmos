def definir_grupo(partidas):
    grupos = [-1, 3, 3, 2, 2, 1, 1]
    vitorias = sum(1 for x in partidas if x == 'v')

    return grupos[vitorias]


if __name__ == '__main__':
    lista_partidas = [input().lower() for _ in range(6)]
    print(definir_grupo(lista_partidas))
