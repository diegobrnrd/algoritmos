def mochila_booleana_infinita(l, peso, valor, n):
    dp = [0] * (l + 1)

    for i in range(n):
        for j in range(peso[i], l + 1):
            dp[j] = max(dp[j], dp[j - peso[i]] + valor[i])

    return dp[l]


def principal():
    n, t = map(int, input().split())
    valores = [0] * n
    pesos = [0] * n
    for i in range(n):
        pesos[i], valores[i] = map(int, input().split())

    print(mochila_booleana_infinita(t, pesos, valores, n))


if __name__ == '__main__':
    principal()
