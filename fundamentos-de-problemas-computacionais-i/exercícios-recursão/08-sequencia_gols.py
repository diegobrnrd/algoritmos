def sequencia_de_gols(m, n, sequencia):
    if m == 0 and n == 0:
        print(" ".join(sequencia))

    if m > 0:
        sequencia.append('A')
        sequencia_de_gols(m - 1, n, sequencia)
        sequencia.pop()

    if n > 0:
        sequencia.append('B')
        sequencia_de_gols(m, n - 1, sequencia)
        sequencia.pop()


def central():
    m, n = 3, 1
    print(f'Possíveis sequências de gols para {m} x {n}:')
    sequencia_de_gols(m, n, [])


if __name__ == '__main__':
    central()
