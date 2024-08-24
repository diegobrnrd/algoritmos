def bondinho(a, m):
    limite = [x for x in range(1, 51)]
    if a + m in limite:
        return 'S'
    else:
        return 'N'


if __name__ == '__main__':
    print(bondinho(int(input()), int(input())))
