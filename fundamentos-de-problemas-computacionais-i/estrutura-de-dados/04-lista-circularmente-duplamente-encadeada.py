class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None
        self.anterior = None


class ListaCircularDuplamenteEncadeada:
    def __init__(self):
        self.fim = None

    def is_vazia(self):
        return self.fim is None

    def inserir_no_inicio(self, dado):
        novo_no = No(dado)
        if self.is_vazia():
            self.fim = novo_no
            novo_no.proximo = novo_no
            novo_no.anterior = novo_no
        else:
            primeiro = self.fim.proximo
            novo_no.proximo = primeiro
            novo_no.anterior = self.fim
            primeiro.anterior = novo_no
            self.fim.proximo = novo_no
            # self.fim = novo_no

    def buscar(self, x):
        if self.is_vazia():
            return None

        i = self.fim.proximo
        while True:
            if i.dado == x:
                return i
            i = i.proximo
            if i == self.fim.proximo:
                break
        return None

    def remover(self, x):
        no_removido = self.buscar(x)
        # Não achou ou lista vazia.
        if no_removido is None:
            return None

        i = self.fim.proximo
        anterior = self.fim

        while True:
            if i.dado == x:
                # Remove de uma lista com um único elemento.
                if i == self.fim and i.proximo == self.fim:
                    self.fim = None
                # Remove quando n > 1.
                else:
                    anterior.proximo = i.proximo
                    i.proximo.anterior = anterior
                    if i == self.fim:
                        self.fim = anterior
                return no_removido
            anterior = i
            i = i.proximo
            if i == self.fim.proximo:
                break

        return no_removido

    def alterar(self, dado_antigo, novo_dado):
        no = self.buscar(dado_antigo)
        if no is None:
            return
        no.dado = novo_dado
        return novo_dado

    def __str__(self):
        if self.is_vazia():
            return 'Minha lista está assim: '

        s = 'Minha lista está assim: '
        i = self.fim.proximo
        while True:
            s += f'{i.dado} '
            i = i.proximo
            if i == self.fim.proximo:
                break
        return s


def principal():
    lista = ListaCircularDuplamenteEncadeada()
    for i in range(1, 6):
        lista.inserir_no_inicio(i)
    lista.inserir_no_inicio(1)
    print(lista)


if __name__ == '__main__':
    principal()
