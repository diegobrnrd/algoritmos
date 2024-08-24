def mdc(x, y):
    if x > y:
        return mdc(x - y, y)
    elif y > x:
        return mdc(y, x)
    else:
        return x


if __name__ == '__main__':
    print(mdc(10, 50))
