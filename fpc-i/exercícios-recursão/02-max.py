def maior(vetor, i=0):
    if i == len(vetor) - 1:
        # Caso base.
        return vetor[i]
        # Retorna o único valor do vetor ou o último.
    else:
        maior_atual = maior(vetor, i + 1)
        # Inicialmente o maior atual será o último valor do vetor.
        if vetor[i] > maior_atual:
            # De trás para frente compara o maior atual com o valor atual até chegar no início do vetor.
            return vetor[i]
        else:
            return maior_atual

# No fim das chamadas recursivas o último return terá nele o maior valor do vetor.


if __name__ == '__main__':
    lista = [1, 8, 2, 4, 3]
    print(maior(lista))
