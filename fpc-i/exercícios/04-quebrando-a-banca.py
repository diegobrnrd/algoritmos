def reverter_saldo(encontrar, saldo):
    encontrei = 0
    maiores_digitos = [None] * encontrar
    maior = float('-inf')
    for d in range(encontrar):
        if encontrar - encontrei != 1:
            # Condição para quando faltar mais de um dígito ser encontrado.
            for digito in saldo[:1 - encontrar + encontrei]:
                # É usado um índice negativo para controlar a janela de análise.
                if digito > maior:
                    maior = digito
            maiores_digitos[d] = maior
            encontrei += 1
            index = saldo.index(maior)
            saldo = saldo[index + 1:]
            maior = float('-inf')
        else:
            # Condição para quando faltar apenas um dígito ser encontrado.
            for digito in saldo:
                # Não é necessário nenhuma janela de análise.
                if digito > maior:
                    maior = digito
            maiores_digitos[d] = maior

    saldo_revertido = [str(y) for y in maiores_digitos]
    return ''.join(saldo_revertido)


if __name__ == '__main__':
    saldos_revertidos = [''] * 3
    for x in range(3):
        total_digitos, retirar_digitos = map(int, input().split())
        encontrar_digitos = total_digitos - retirar_digitos
        saldo_concatenado = input()
        saldo_inteiro = [int(x) for x in saldo_concatenado]

        saldos_revertidos[x] = reverter_saldo(encontrar_digitos, saldo_inteiro)

    for s in saldos_revertidos:
        print(s)
