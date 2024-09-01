class No:
    def __init__(self, dado):
        self.dado = dado
        self.anterior = None
        self.proximo = None


class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def is_vazia(self):
        return self.inicio is None or self.fim is None

    def inserir(self, dado):
        novo_no = No(dado)
        if self.is_vazia(): # A fila está vazia.
            self.inicio = novo_no
            self.fim = novo_no
        else: # A fila não está vazia.
            self.fim.proximo = novo_no
            novo_no.anterior = self.fim
            self.fim = novo_no
        return novo_no

    def remover(self):
        no_removido = self.inicio
        if self.is_vazia():  # A fila está vazia.
            return None
        elif self.inicio == self.fim:  # A fila tem 1 elemento.
            self.inicio = self.fim = None
        else:  # A fila tem mais de 1 elemento.
            segundo = self.inicio.proximo
            segundo.anterior = None
            self.inicio = segundo
        return no_removido

    def __str__(self):
        s = 'Minha fila está assim: '
        i = self.inicio
        while i is not None:
            s += f'{i.dado} '
            i = i.proximo
        return s


def principal():
    lista = list(range(1, 9))
    fila = Fila()
    for i in lista:
        print(f'Inserindo elemento {fila.inserir(i * 3).dado}')
    print(fila)

    for i in range(3):
        no_removido = fila.remover()
        print(f'Estou removendo {" Nada " if no_removido is None else no_removido.dado}')
    print(fila)


if __name__ == '__main__':
    principal()