def verificacao(string):
    pilha = []
    oposto = {'{': '}', '[': ']', '(': ')'}

    for caractere in string:
        if caractere in oposto:
            pilha.append(caractere)
        elif len(pilha) > 0 and caractere == oposto[pilha[-1]]:
            pilha.pop()
        else:
            return 'N'

    if len(pilha) == 0:
        return 'S'
    else:
        return 'N'


def funcao_principal():
    t = int(input())
    for _ in range(t):
        cadeia = input().strip()
        print(verificacao(cadeia))


if __name__ == '__main__':
    funcao_principal()
