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
        return no_removido.dado

    def __str__(self):
        s = 'Minha fila está assim: '
        i = self.inicio
        while i is not None:
            s += f'{i.dado} '
            i = i.proximo
        return s


def jogar(deck_mesa, convidados):
    fila_mesa = Fila()
    for carta in deck_mesa:
        fila_mesa.inserir(carta)

    filas_convidados = []
    for deck in convidados:
        fila_convidado = Fila()
        for carta in deck:
            fila_convidado.inserir(carta)
        filas_convidados.append(fila_convidado)

    rodadas = 0
    while rodadas < 1000:
        carta_mesa = fila_mesa.remover()
        fila_mesa.inserir(carta_mesa)

        for i, fila_convidado in enumerate(filas_convidados, 1):
            if fila_convidado.is_vazia():
                return i  # Convidado vencedor.

            carta_convidado = fila_convidado.remover()
            if carta_convidado == carta_mesa:
                continue  # Carta descartada.
            else:
                fila_convidado.inserir(carta_convidado) # Carta retorna para o fim do deck.

        rodadas += 1

    return 0  # Juvenal vence se o jogo não terminar em 1000 rodadas.


def principal():
    n_festas = int(input())
    vencedor = [0] * n_festas
    for i in range(n_festas):
        deck_mesa = list(map(int, input().split()))
        convidados = []
        while True:
            entrada = input().split()
            if entrada[0] == '-1':
                break
            convidados.append(list(map(int, entrada)))
        vencedor[i] = jogar(deck_mesa, convidados)
    for x in vencedor:
        print(x)


if __name__ == '__main__':
    principal()
