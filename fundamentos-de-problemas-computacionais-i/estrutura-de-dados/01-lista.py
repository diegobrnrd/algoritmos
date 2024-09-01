class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None
        self.anterior = None


class ListaDuplamenteEncandeada:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def is_vazia(self):
        return self.inicio is None or self.fim is None

    def inserir_no_fim(self, dado):
        novo_no = No(dado)
        if self.is_vazia():
            self.inicio = self.fim = novo_no
        else:
            self.fim.proximo = novo_no
            novo_no.anterior = self.fim
            self.fim = novo_no

    def inserir_no_inicio(self, dado):
        novo_no = No(dado)
        if self.is_vazia():
            self.inicio = self.fim = novo_no
        else:
            novo_no.proximo = self.inicio
            self.inicio.anterior = novo_no
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
        # Remover do início quando n > 1.
        if no_removido == self.inicio:
            self.inicio = self.inicio.proximo
            self.inicio.anterior = None
            return no_removido
        # Remover do fim quando n > 1.
        if no_removido == self.fim:
            penultimo = self.fim.anterior
            penultimo.proximo = None
            self.fim = penultimo
            return no_removido
        # Remover do meio com n > 1.
        anterior = no_removido.anterior
        proximo = no_removido.proximo
        anterior.proximo = proximo
        proximo.anterior = anterior
        return no_removido

    def __str__(self):
        s = ''
        i = self.inicio
        while i is not None:
            s += f'{i.dado} '
            i = i.proximo
        return s


def principal():
    lista = ListaDuplamenteEncandeada()
    for i in range(10):
        lista.inserir_no_fim(randint(0, 9))
    print(lista)
    print(f'O 9 foi sorteado? {"Sim!" if lista.buscar(9) else "Não!"}')


if __name__ == '__main__':
    from random import randint
    principal()
