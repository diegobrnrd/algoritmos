def mod(x, y):
    if x > y:
        return mod(x - y, y)
    elif y > x:
        return x
    elif x == y:
        return 0


if __name__ == '__main__':
    print(mod(10, 3))
