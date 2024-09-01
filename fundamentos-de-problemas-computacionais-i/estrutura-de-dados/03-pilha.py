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
        if self.is_vazia():  # A pilha está vazia.
            self.topo = novo_no
        else:  # A pilha não está vazia.
            novo_no.proximo = self.topo
            self.topo = novo_no
        return novo_no

    def remover(self):
        if self.is_vazia():  # A pilha está vazia.
            return None
        no_removido = self.topo  # A pilha não está vazia.
        self.topo = no_removido.proximo
        return no_removido

    def __str__(self):
        s = 'Minha pilha está assim: '
        i = self.topo
        while i is not None:
            s += f'{i.dado} '
            i = i.proximo
        return s

def principal():
    lista = list(range(1, 9))
    pilha = Pilha()
    for i in lista:
        print(f'Inserindo elemento {pilha.inserir(i * 3).dado}')
    print(pilha)

    for i in range(3):
        no_removido = pilha.remover()
        print(f'Estou removendo {" Nada " if no_removido is None else no_removido.dado}')
    print(pilha)

if __name__ == '__main__':
    principal()
