def com_2_lacos(s):
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            print(s[i:j])


def com_1_laco(s, i, j):
    if j < len(s):
        print(s[i:j + 1])
        com_1_laco(s, i, j + 1)


def com_0_laco(s, i, j):
    if i < len(s):
        if j < len(s):
            print(s[i:j + 1])
            com_0_laco(s, i, j + 1)
        else:
            com_0_laco(s, i + 1, i + 1)


if __name__ == '__main__':
    st = 'rum'

    com_2_lacos(st)

    for x in range(len(st)):
        com_1_laco(st, x, x)

    com_0_laco(st, 0, 0)
