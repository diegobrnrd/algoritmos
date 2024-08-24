def conjunto_potencia_recursivo(s):
    if len(s) == 0:
        return [[]]

    elemento = s[0]
    resto_do_conjunto = s[1:]

    conjunto_potencia_resto = conjunto_potencia_recursivo(resto_do_conjunto)

    novos_subconjuntos = []
    for subconjunto in conjunto_potencia_resto:
        novos_subconjuntos.append(subconjunto)
        novos_subconjuntos.append([elemento] + subconjunto)

    return novos_subconjuntos


def imprimir_conjunto_potencia(s):
    conjunto_potencia = conjunto_potencia_recursivo(s)
    for subconjunto in conjunto_potencia:
        print(subconjunto)


if __name__ == '__main__':
    conjunto_de_letras = ['A', 'B', 'C']
    print(f'O conjunto potência de {" ".join(conjunto_de_letras)} é:')
    imprimir_conjunto_potencia(conjunto_de_letras)
