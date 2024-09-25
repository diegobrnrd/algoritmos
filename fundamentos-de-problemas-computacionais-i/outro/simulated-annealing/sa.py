import random
import math


def ler_arquivo():
    """Coleta as coordenadas e as armazena em um dicionário."""
    coordenadas = {}
    with open('berlin52.tsp', 'r') as arquivo:
        for linha in arquivo.readlines()[6:58]:
            cidade, x, y = linha.strip().split()
            coordenadas[int(cidade)] = (float(x), float(y))
    return coordenadas


def gerar_percurso(coordenadas):
    """Gera um percurso aleatório de cidades e calcula a distância total desse percurso."""
    lista = list(range(1, len(coordenadas) + 1))
    percurso = random.sample(lista, len(coordenadas))
    inicio = percurso[0]
    percurso.append(inicio)
    distancia = calcular_percurso(percurso, coordenadas)
    return percurso, distancia


def recozimento_simulado(percurso, distancia, coordenadas, temperatura_inicial, taxa_de_resfriamento, maximo_de_interacoes):
    """Implementa o algoritmo de Recozimento Simulado."""
    percurso_atual = percurso
    melhor_percurso = percurso_atual
    distancia_atual = distancia
    melhor_distancia = distancia_atual

    temperatura = temperatura_inicial

    for _ in range(maximo_de_interacoes):
        vizinho = gerar_vizinho(percurso_atual)
        distancia_vizinho = calcular_percurso(vizinho, coordenadas)

        variacao_de_distancia = distancia_vizinho - distancia_atual

        if variacao_de_distancia < 0 or random.random() < math.exp(-variacao_de_distancia / temperatura):
            percurso_atual = vizinho
            distancia_atual = distancia_vizinho

        if distancia_atual < melhor_distancia:
            melhor_percurso = percurso_atual
            melhor_distancia = distancia_atual

        temperatura *= taxa_de_resfriamento

    return melhor_percurso, melhor_distancia


def gerar_vizinho(percurso_atual):
    """Gera uma solução vizinha trocando duas cidades aleatórias."""
    vizinho = list(percurso_atual)
    i, j = random.sample(range(1, len(percurso_atual) - 1), 2)
    vizinho[i], vizinho[j] = vizinho[j], vizinho[i]
    return vizinho


def calcular_percurso(vizinho, coordenadas):
    """Calcula a distância total de um percurso passando por todas as cidades."""
    distancia = 0
    for i in range(len(vizinho) - 1):
        cidade_1 = vizinho[i]
        cidade_2 = vizinho[i + 1]
        x1, y1 = coordenadas[cidade_1]
        x2, y2 = coordenadas[cidade_2]
        distancia += calcular_distancia(x1, y1, x2, y2)
    return distancia


def calcular_distancia(x1, y1, x2, y2):
    """Calcula a distância euclidiana entre dois pontos no plano cartesiano."""
    a = (x2 - x1) ** 2
    b = (y2 - y1) ** 2
    x = a + b
    return raiz_quadrada(x, 3.2, 0.001)


def raiz_quadrada(x, x0, e):
    """Calcula a raiz quadrada."""
    if abs(x0 ** 2 - x) <= e:
        return x0
    else:
        return raiz_quadrada(x, ((x0 ** 2 + x) / (2 * x0)), e)


def funcao_central():
    """Função central que gerencia a chamada de todas as outras funções."""
    coordenadas = ler_arquivo()
    percurso, distancia = gerar_percurso(coordenadas)

    temperatura_inicial = 1000
    taxa_de_resfriamento = 0.99
    maximo_de_interacoes = 10000

    melhor_percurso, melhor_distancia = recozimento_simulado(
        percurso,
        distancia,
        coordenadas,
        temperatura_inicial,
        taxa_de_resfriamento,
        maximo_de_interacoes
    )

    print(f'\nTour:\n')

    melhor_percurso[-1] = -1
    for c in melhor_percurso:
        print(c)

    print(f'\nDistância: {int(melhor_distancia)}')


if __name__ == '__main__':
    """Cronometra o tempo necessário para a execução do algoritmo."""
    import timeit
    tempo_de_execucao = timeit.timeit(funcao_central, number=1)
    print(f'\nTempo de execução: {tempo_de_execucao:.6f} segundos.')
