def posicao_inicial(arena):
    for i in range(len(arena)):
        for j in range(len(arena[i])):
            if arena[i][j] in 'NSLO':
                return arena[i][j], i, j


def coletar_figurinhas(arena, orientacao, i, j, movimentos):
    direcoes = {'N': (-1, 0), 'S': (1, 0), 'L': (0, 1), 'O': (0, -1)}
    esquerda = {'N': 'O', 'O': 'S', 'S': 'L', 'L': 'N'}
    direita = {'N': 'L', 'L': 'S', 'S': 'O', 'O': 'N'}
    figurinhas = 0

    for movimento in movimentos:
        if movimento in 'D':
            orientacao = direita[orientacao] # Gira 90 graus para a direita.
        elif movimento in 'E':
            orientacao = esquerda[orientacao] # Gira 90 graus para a esquerda.
        elif movimento == 'F':
            ni, nj = i + direcoes[orientacao][0], j + direcoes[orientacao][1] # Anda uma célula para a frente.
            if 0 <= ni < len(arena) and 0 <= nj < len(arena[0]) and arena[ni][nj] != '#':
                i, j = ni, nj
                if arena[i][j] == '*':
                    figurinhas += 1
                    arena[i][j] = '.'
    return figurinhas


def funcao_principal():
    n_figurinhas_coletadas = []
    while True:
        n_linhas, n_colunas, n_instrucoes = map(int, input().split())
        if n_linhas == 0 and n_colunas == 0 and n_instrucoes == 0:
            for f in n_figurinhas_coletadas:
                print(f)
            break

        arena = [list(input().strip()) for _ in range(n_linhas)]
        movimentos = input().strip()

        orientacao, i, j = posicao_inicial(arena)
        figurinhas_coletadas = coletar_figurinhas(arena, orientacao, i, j, movimentos)
        n_figurinhas_coletadas.append(figurinhas_coletadas)


if __name__ == '__main__':
    funcao_principal()
