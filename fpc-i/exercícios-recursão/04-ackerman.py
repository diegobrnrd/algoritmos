def ackerman(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackerman(m-1, 1)
    elif m > 0 and n > 0:
        return ackerman(m-1, ackerman(m, n-1))


if __name__ == '__main__':
    print(ackerman(1, 2))
