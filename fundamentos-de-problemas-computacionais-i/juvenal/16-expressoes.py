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
    s_n = [''] * t

    for i, _ in enumerate(range(t)):
        cadeia = input().strip()
        s_n[i] = verificacao(cadeia)

    for c in s_n:
        print(c)


if __name__ == '__main__':
    funcao_principal()
