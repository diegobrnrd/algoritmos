def interruptor(n):
    lampadas = [False, False]
    apertos = [int(x) for x in input().split()]

    for x in apertos:
        if x == 1:
            lampadas[0] = not lampadas[0]
        else:
            lampadas[0], lampadas[1] = not lampadas[0], not lampadas[1]

    return lampadas


if __name__ == '__main__':
    lamps = interruptor(int(input()))

    for i in lamps:
        if i:
            print(1)
        else:
            print(0)
