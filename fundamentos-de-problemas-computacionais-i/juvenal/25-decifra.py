def principal():
    alfabeto_crip = input()
    frase_crip = input()
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    frase_descrip = ''
    contador = 0
    for i in range(len(frase_crip)):
        for j in range(len(alfabeto)):
            if frase_crip[i] == alfabeto_crip[j]:
                frase_descrip += alfabeto[j]
            contador += 1

    return frase_descrip


if __name__ == '__main__':
    print(principal())
