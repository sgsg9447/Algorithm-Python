a = []

def hanoi_1to3(n):
    if n == 1:
        a.append('1 3')
    else:
        hanoi_1to2(n-1)
        a.append('1 3')
        hanoi_2to3(n-1)

def hanoi_1to2(n):
   
    if n == 1:
        a.append('1 2')
    else:
        hanoi_1to3(n-1)
        a.append('1 2')
        hanoi_3to2(n-1)

def hanoi_2to3(n):

    if n == 1:
        a.append('2 3')
    else:
        hanoi_2to1(n-1)
        a.append('2 3')
        hanoi_1to3(n-1)

def hanoi_3to2(n):

    if n == 1:
        a.append('3 2')
    else:
        hanoi_3to1(n-1)
        a.append('3 2')
        hanoi_1to2(n-1)

def hanoi_2to1(n):

    if n == 1:
        a.append('2 1')
    else:
        hanoi_2to3(n-1)
        a.append('2 1')
        hanoi_3to1(n-1)

def hanoi_3to1(n):

    if n == 1:
        a.append('3 1')
    else:
        hanoi_3to2(n-1)
        a.append('3 1')
        hanoi_2to1(n-1)

n = int(input())
if n<21:
    hanoi_1to3(n)
    print(len(a))
    for i in a:
        print(i)
else:
    print(pow(2,n)-1)
