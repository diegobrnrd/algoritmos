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

    def __str__(self):
        s = 'Minha pilha está assim: '
        i = self.topo
        while i is not None:
            s += f'{i.dado} '
            i = i.proximo
        return s


def avaliar_expressao_prefixa(expressao):
    pilha = Pilha()

    for token in expressao:
        if token.isdigit():
            pilha.inserir(int(token))
        else:
            operando1 = pilha.remover().dado
            operando2 = pilha.remover().dado
            if token == '+':
                resultado = operando1 + operando2
                pilha.inserir(resultado)
            elif token == '-':
                resultado = operando1 - operando2
                pilha.inserir(resultado)
            elif token == '*':
                resultado = operando1 * operando2
                pilha.inserir(resultado)
            elif token == '/':
                resultado = operando1 // operando2
                pilha.inserir(resultado)

    return pilha.remover().dado



def principal():
    expressoes = [input().split()[::-1] for _ in range(10)]

    for expr in expressoes:
        print(avaliar_expressao_prefixa(expr))


if __name__ == '__main__':
    principal()
