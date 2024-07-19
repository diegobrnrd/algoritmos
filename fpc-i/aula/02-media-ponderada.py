def media_ponderada():
    valores = [float(x) for x in input().split()]
    pesos = [float(x) for x in input().split()]
    total_valores, n_pesos = 0, len(pesos)

    for numero, peso in zip(valores, pesos):
        total_valores += numero * peso

    print(f'Média ponderada: {total_valores / n_pesos}')


if __name__ == '__main__':
    media_ponderada()
