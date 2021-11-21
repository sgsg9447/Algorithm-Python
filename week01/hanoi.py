# N = 3
# def hanoi(N, one, two, three) :
#         if N > 1:
#             hanoi(N-1, one, three, two)         # n-1번 원반과 위의 원반들을 1 -> 2 이동
#             print(f'{one},{three}')             # n번 원반을 1->3 으로 이동을 출력
#             hanoi(N-1, two, one, three)         # n-1번 원반과 위의 원반들을 2 -> 3으로 이동
#         if N > 1:
#             hanoi(N-1, mid, end)
# print(2**N-1)
# hanoi(N, 1, 2 ,3) # n번 원반과 위의 원반들을 1 -> 3으로 이동

# def hanoi(n, start, end):
#     6


list=[]
cnt = 0

def hanoi(n, s, e):
    global cnt
    cnt +=1

    if n > 1:
        hanoi(n-1, s, 6-s-e)
    list.append([s,e])
    
    if n > 1:
        hanoi(n-1, 6-s-e, e)
    
n = int(input())
if n <= 20:
    hanoi(n, 1, 3)
    print(cnt)
    for i in range(len(list)):
        print(f'{list[i][0]} {list[i][1]}')
else:
    x = pow(2,n) - 1
    print(x)