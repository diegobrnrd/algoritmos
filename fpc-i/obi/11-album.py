def figurinhas(n):
    album_completo = sum(1 for _ in range(n))
    m = int(input())
    figurinhas_unicas = set(int(input()) for _ in range(m))
    figurinhas_unicas = sum(1 for _ in figurinhas_unicas)

    return album_completo - figurinhas_unicas


if __name__ == '__main__':
    print(figurinhas(int(input())))
