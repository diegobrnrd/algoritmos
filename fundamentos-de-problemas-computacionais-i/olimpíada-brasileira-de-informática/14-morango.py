def maior_area():
    dimensoes = [int(input()) for _ in range(4)]
    area_1, area_2 = dimensoes[0] * dimensoes[1], dimensoes[2] * dimensoes[3]
    if area_1 > area_2:
        return area_1
    else:
        return area_2


if __name__ == '__main__':
    print(maior_area())
