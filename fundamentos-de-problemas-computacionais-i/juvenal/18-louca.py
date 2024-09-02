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

    def remover_inicio(self):
        if self.is_vazia():
            return None
        no_removido = self.inicio
        if self.inicio == self.fim:
            self.inicio = self.fim = None
        else:
            self.inicio = self.inicio.proximo
            self.inicio.anterior = None
        return no_removido.dado

    def __str__(self):
        s = 'Minha lista está assim: '
        i = self.inicio
        while i is not None:
            s += f'{i.dado} '
            i = i.proximo
        return s


def jogar(deck_mesa, convidados):
    fila_mesa = ListaDuplamenteEncandeada()
    for carta in deck_mesa:
        fila_mesa.inserir_no_fim(carta)

    filas_convidados = []
    for deck in convidados:
        fila_convidado = ListaDuplamenteEncandeada()
        for carta in deck:
            fila_convidado.inserir_no_fim(carta)
        filas_convidados.append(fila_convidado)

    rodadas = 0
    while rodadas < 1000:
        carta_mesa = fila_mesa.remover_inicio()
        fila_mesa.inserir_no_fim(carta_mesa)

        for i, fila_convidado in enumerate(filas_convidados, 1):
            if fila_convidado.is_vazia():
                return i  # Convidado vencedor.

            carta_convidado = fila_convidado.remover_inicio()
            if carta_convidado == carta_mesa:
                continue  # Carta descartada.
            else:
                fila_convidado.inserir_no_fim(carta_convidado) # Carta retorna para o fim do deck.

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
