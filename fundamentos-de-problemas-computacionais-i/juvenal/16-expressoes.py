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
        return no_removido


def validar_expressao(cadeias, pilha):
    correspondente = {'}': '{', ']': '[', ')': '('}
    for caractere in cadeias:
        if caractere in correspondente.values():
            pilha.inserir(caractere)
        else:
            caractere_valor = pilha.remover()
            if caractere_valor is None or correspondente[caractere] != caractere_valor.dado:
            # Verifica se chave e valor são correspondentes.
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
