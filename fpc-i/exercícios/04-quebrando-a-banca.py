def reverter_saldo(encontrar, saldo, encontrei=0):
    maiores_digitos = ['a'] * encontrar
    maior = float('-inf')

    for d in range(encontrar):
        # Condição para quando faltar mais de um dígito a ser encontrado.
        if encontrar - encontrei != 1:
            # É usado um índice negativo para controlar a janela.
            for digito in saldo[:1 - encontrar + encontrei]:
                if digito > maior:
                    maior = digito
            maiores_digitos[d] = str(maior)
            encontrei += 1
            index = saldo.index(maior)
            saldo = saldo[index + 1:]
            maior = float('-inf')
        # Condição para quando faltar apenas um dígito a ser encontrado.
        else:
            # Não é necessário nenhuma janela.
            for digito in saldo:
                if digito > maior:
                    maior = digito
            maiores_digitos[d] = str(maior)

    return ''.join(maiores_digitos)


def saida(saldos_revertidos):
    for saldo in saldos_revertidos:
        print(saldo)


def funcao_principal():
    saldos_revertidos = [''] * 3
    for i in range(len(saldos_revertidos)):
        total_digitos, retirar_digitos = map(int, input().split())
        saldo_string = input()
        encontrar_digitos = total_digitos - retirar_digitos
        lista_digitos_saldo = [int(d) for d in saldo_string]

        saldos_revertidos[i] = reverter_saldo(encontrar_digitos, lista_digitos_saldo)

    saida(saldos_revertidos)


if __name__ == '__main__':
    funcao_principal()
