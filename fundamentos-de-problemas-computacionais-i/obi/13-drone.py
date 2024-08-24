def verificar_medidas():
    caixa = [int(input()) for _ in range(3)]
    janela = [int(input()) for _ in range(2)]
    caixa.sort()
    janela.sort()
    if caixa[0] <= janela[0] and caixa[1] <= janela[1]:
        return 'S'
    else:
        return 'N'


if __name__ == '__main__':
    print(verificar_medidas())
