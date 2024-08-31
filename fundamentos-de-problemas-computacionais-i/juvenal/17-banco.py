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

    def primeiro(self):
        return self.inicio


def principal():
    n_casos_teste = int(input())
    for i in range(n_casos_teste):
        n_comandos = int(input())
        fila_normal = Fila()
        fila_preferencial = Fila()
        print(f'Caso {i + 1}:')
        for _ in range(n_comandos):
            entrada = input().split()
            if len(entrada) == 2:
                if entrada[0] == 'f':
                    fila_normal.inserir(int(entrada[1]))
                elif entrada[0] == 'p':
                    fila_preferencial.inserir(int(entrada[1]))
            elif entrada[0] == 'A':
                if fila_normal.is_vazia():
                    fila_preferencial.remover()
                else:
                    fila_normal.remover()
            elif entrada[0] == 'B':
                if fila_preferencial.is_vazia():
                    fila_normal.remover()
                else:
                    fila_preferencial.remover()
            elif entrada[0] == 'I':
                normal = fila_normal.primeiro()
                preferencial = fila_preferencial.primeiro()
                normal_str = normal.dado if normal else 0
                preferencial_str = preferencial.dado if preferencial else 0
                print(f'{normal_str} {preferencial_str}')


if __name__ == '__main__':
    principal()
