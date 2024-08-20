def colisao():
    x0a, y0a, x1a, y1a = [int(x) for x in input().split()]
    x0b, y0b, x1b, y1b = [int(x) for x in input().split()]

    if x0a > x1b or x1a < x0b:
        return 0
    elif y0a > y1b or y1a < y0b:
        return 0
    else:
        return 1


if __name__ == '__main__':
    print(colisao())
