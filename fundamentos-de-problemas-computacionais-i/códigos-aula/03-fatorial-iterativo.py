def fatorial_for(n):
    fat = 1
    for x in range(1, n + 1):
        fat *= x
    print(fat)


def fatorial_while(n):
    fat = 1
    x = 1
    while x <= n:
        fat *= x
        x += 1
    print(fat)


if __name__ == '__main__':
    fatorial_for(int(input()))
    fatorial_while(int(input()))
