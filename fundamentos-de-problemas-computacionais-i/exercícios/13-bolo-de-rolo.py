def maior(vetor, i=0):
    if i == len(vetor) - 1:
        return vetor[i]
    else:
        maior_atual = maior(vetor, i + 1)
        if vetor[i] > maior_atual:
            return vetor[i]
        else:
            return maior_atual


def maior_fatia(n, tamanhos):
    def pode_cortar(tamanho):
        # Calcula o número total de fatias possíveis para o tamanho dado.
        total_fatias = sum(bolo // tamanho for bolo in tamanhos)
        # Verifica se o número total de fatias é suficiente.
        return total_fatias >= n

    inicio, fim = 1, maior(tamanhos)
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if pode_cortar(meio):
            inicio = meio + 1
        else:
            fim = meio - 1
    return fim


def funcao_principal():
    n_pessoas = int(input())
    q_bolos = int(input())
    tamanho_dos_bolos = [int(b) for b in input().split()]
    print(maior_fatia(n_pessoas, tamanho_dos_bolos))


if __name__ == '__main__':
    funcao_principal()
