def pontuacao(d):
    if 1400 < d <= 2000:
        return 3
    elif 800 < d <= 1400:
        return 2
    elif d <= 800:
        return 1


if __name__ == '__main__':
    print(pontuacao(int(input())))
