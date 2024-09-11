class No:
    def __init__(self, chave, dado):
        self.chave = chave
        self.dado = dado
        self.proximo = None


# Endereçamento fechado (encadeamento)
class Lista:
    def __init__(self):
        self.inicio = None

    def is_vazia(self):
        return self.inicio is None

    def inserir(self, chave, dado):
        novo_no = No(chave, dado)
        novo_no.proximo = self.inicio
        self.inicio = novo_no

    def buscar(self, chave):
        i = self.inicio
        while i is not None:
            if i.chave == chave:
                return i.dado
            i = i.proximo
        return None

    def remover(self, chave):
        i = self.inicio
        anterior = None
        while i is not None:
            if i.chave == chave:
                if anterior is None:
                    self.inicio = i.proximo
                else:
                    anterior.proximo = i.proximo
                return True
            anterior = i
            i = i.proximo
        return False

    def __str__(self):
        i = self.inicio
        s = ''
        while i is not None:
            s += f'Chave={i.chave}, Dado={i.dado} | '
            i = i.proximo
        return s


class TabelaHashFechada:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela = [None for _ in range(tamanho)]

    def funcao_hash(self, chave):
        return chave % self.tamanho

    def inserir(self, chave, dado):
        haash = self.funcao_hash(chave)
        if self.tabela[haash] is None:  # Verificando colisão.
            self.tabela[haash] = Lista()
        self.tabela[haash].inserir(chave, dado)

    def buscar(self, chave):
        haash = self.funcao_hash(chave)
        lista = self.tabela[haash]
        if lista is not None:
            return lista.buscar(chave)
        return None

    def remover(self, chave):
        haash = self.funcao_hash(chave)
        lista = self.tabela[haash]
        if lista is not None:
            return lista.remover(chave)
        return False

    def __str__(self):
        s = ''
        for indice, lista in enumerate(self.tabela):
            s += f'Índice {indice}: '
            if lista is not None:
                s += str(lista)
            else:
                s += 'Nada aqui'
            s += '\n'
        return s


def funcao_principal():
    minha_tabela = TabelaHashFechada(5)
    chaves = [i for i in range(10)]
    dados = [i * 100 for i in range(10)]

    for chave, dado in zip(chaves, dados):
        minha_tabela.inserir(chave, dado)

    print(minha_tabela)


if __name__ == '__main__':
    funcao_principal()
