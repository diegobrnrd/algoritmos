def organizar_arquivos(limite, arquivos):
    n_pastas = 0
    i, j = 0, len(arquivos) - 1
    while i <= j:
        if arquivos[i] + arquivos[j] <= limite:
            # Se a soma de dois arquivos for menor ou igual ao limite, ambos são adicionados na mesma pasta.
            n_pastas += 1
            i += 1
            j -= 1
        else:
            # Caso contrário, apenas o amior arquivo é adicionado na pasta.
            n_pastas += 1
            j -= 1

    return n_pastas


if __name__ == '__main__':
    n_arquivos, limite_pasta = input().split()
    lista_arquivos = [int(x) for x in input().split()]
    lista_arquivos.sort()
    print(organizar_arquivos(int(limite_pasta), lista_arquivos))
