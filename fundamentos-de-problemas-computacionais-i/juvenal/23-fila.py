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
        if self.is_vazia():
            self.inicio = novo_no
            self.fim = novo_no
        else:
            self.fim.proximo = novo_no
            novo_no.anterior = self.fim
            self.fim = novo_no
        return novo_no

    def remover(self):
        no_removido = self.inicio
        if self.is_vazia():
            return None
        elif self.inicio == self.fim:
            self.inicio = self.fim = None
        else:
            segundo = self.inicio.proximo
            segundo.anterior = None
            self.inicio = segundo
        return no_removido

    def remover_pessoa(self, dado):
        atual = self.inicio
        while atual is not None:
            if atual.dado == dado:
                if atual.anterior is not None:
                    atual.anterior.proximo = atual.proximo
                else:
                    self.inicio = atual.proximo
                if atual.proximo is not None:
                    atual.proximo.anterior = atual.anterior
                else:
                    self.fim = atual.anterior
                return atual
            atual = atual.proximo
        return None

    def __str__(self):
        s = ''
        i = self.inicio
        while i is not None:
            s += f'{i.dado} '
            i = i.proximo
        return s


def principal():
    n = int(input())
    lista = [int(x) for x in input().split()]
    fila = Fila()
    for pessoa in lista:
        fila.inserir(pessoa)
    m = int(input())
    lista_2 = [int(x) for x in input().split()]
    for pessoa in lista_2:
        fila.remover_pessoa(pessoa)
    print(fila)


if __name__ == '__main__':
    principal()
