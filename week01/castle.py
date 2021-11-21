def make_castle(m):
    if m == 0:
        return
    else:
        print('*'* m)
        make_castle(m-1)
        # print('*'* m)

n = int(input())
make_castle(n)
