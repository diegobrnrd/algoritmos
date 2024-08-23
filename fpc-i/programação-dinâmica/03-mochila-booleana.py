def mochila_booleana(l, peso, valor, n):
    tab = [[0 for _ in range(l + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for li in range(l + 1):
            if i == 0 or li == 0:
                # Se não há itens ou capacidade, o valor é 0.
                tab[i][li] = 0
            elif peso[i - 1] <= li:
                # Se o peso do item atual é menor ou igual à capacidade disponível da mochila,
                # calcula-se o valor máximo possível ao incluir ou não o item atual.
                # Incluir o item atual significa somar o valor do item atual à solução
                # ótima do subproblema com a capacidade reduzida (li - peso[i - 1]).
                tab[i][li] = max(valor[i - 1] + tab[i - 1][li - peso[i - 1]], tab[i - 1][li])
            else:
                # Se o peso do item atual é maior que a capacidade disponível da mochila,
                # não podemos incluir o item. Mantemos o valor máximo do subproblema sem
                # incluir o item atual.
                tab[i][li] = tab[i - 1][li]

    return tab[n][l]


def funcao_principal():
    valor = [500, 400, 300, 450]
    peso = [4, 2, 1, 3]
    l = 5 # Limite de peso da mochila.
    n = len(valor) # Número de itens.
    print(mochila_booleana(l, peso, valor, n))


if __name__ == '__main__':
    funcao_principal()