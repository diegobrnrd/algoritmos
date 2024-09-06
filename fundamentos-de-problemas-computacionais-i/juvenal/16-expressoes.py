class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None


class Pilha:
    def __init__(self):
        self.topo = None

    def is_vazia(self):
        return self.topo is None

    def inserir(self, dado):
        novo_no = No(dado)
        if self.is_vazia():
            self.topo = novo_no
        else:
            novo_no.proximo = self.topo
            self.topo = novo_no
        return novo_no

    def remover(self):
        if self.is_vazia():
            return None
        no_removido = self.topo
        self.topo = no_removido.proximo
        return no_removido.dado

    def __str__(self):
        s = 'Minha pilha está assim: '
        i = self.topo
        while i is not None:
            s += f'{i.dado} '
            i = i.proximo
        return s


def validar_expressao(cadeias, pilha):
    correspondente = {'}': '{', ']': '[', ')': '('}
    for caractere in cadeias:
        if caractere in correspondente.values():
            pilha.inserir(caractere)
            # Quando o caractere for um valor do dicionário, ele é adicionado na pilha.
        else:
            caractere_valor = pilha.remover()
            if caractere_valor is None or correspondente[caractere] != caractere_valor:
            # Quando o caractere for uma chave do dicionário, um caractere é retirado da pilha
            # e é verificado se o caractere retirado corresponde ao valor esperado.
                return 'N'
    if pilha.is_vazia():
        return 'S'
    else:
        return 'N'


def principal():
    t = int(input())
    respostas = [''] * t
    for i in range(t):
        cadeias = list(input())
        pilha = Pilha()
        respostas[i] = validar_expressao(cadeias, pilha)

    for resposta in respostas:
        print(resposta)


if __name__ == '__main__':
    principal()
