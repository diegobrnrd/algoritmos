class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None


class ListaEncandeada:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def is_vazia(self):
        return self.inicio is None

    def inserir_no_fim(self, dado):
        novo_no = No(dado)
        if self.is_vazia():
            self.inicio = self.fim = novo_no
        else:
            self.fim.proximo = novo_no
            self.fim = novo_no

    def inserir_no_inicio(self, dado):
        novo_no = No(dado)
        if self.is_vazia():
            self.inicio = self.fim = novo_no
        else:
            novo_no.proximo = self.inicio
            self.inicio = novo_no

    def buscar(self, x):
        i = self.inicio
        while i is not None:
            if i.dado == x:
                return i
            i = i.proximo
        return None

    def remover(self, x):
        no_removido = self.buscar(x)
        # Não achou ou lista vazia.
        if no_removido is None:
            return None
        # Remove de uma lista com um único elemento.
        elif no_removido == self.inicio == self.fim:
            self.inicio = self.fim = None
            return no_removido
        # Remover do inicio quando n > 1.
        if no_removido == self.inicio:
            self.inicio = self.inicio.proximo
            return no_removido
        # Remover do fim quando n > 1.
        if no_removido == self.fim:
            penultimo = self.inicio
            while penultimo.proximo != self.fim:
                penultimo = penultimo.proximo
            penultimo.proximo = None
            self.fim = penultimo
            return no_removido
        # Remover do meio com n > 1.
        anterior = self.inicio
        while anterior.proximo != no_removido:
            anterior = anterior.proximo
        anterior.proximo = no_removido.proximo
        return no_removido

    def alterar(self, dado_antigo, novo_dado):
        no = self.buscar(dado_antigo)
        if no is None:
            return None
        no.dado = novo_dado
        return novo_dado


    def __str__(self):
        s = 'Minha lista está assim: '
        i = self.inicio
        while i is not None:
            s += f'{i.dado} '
            i = i.proximo
        return s


def principal():
    lista = ListaEncandeada()
    for i in range(1, 4):
        lista.inserir_no_fim(i)
    print(lista)


if __name__ == '__main__':
    principal()
