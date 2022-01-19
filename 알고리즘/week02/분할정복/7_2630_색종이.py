import sys
n=int(sys.stdin.readline())

# n_list = [list(map(int,sys.stdin.readline().split())) for _ in range(n)] #x행 y열

n_list = []
for _ in range(n):
    n_list.append(list(map(int, input().split())))


white = 0 #흰색일때는 0 
blue = 0 # 파란색일때는 1

def cut(n, x=0,y=0):
    global blue,white
    check = n_list[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if check != n_list[i][j]: #하나라도 같은 색 아닐시
                cut (n//2, x, y) #1사분면
                cut (n//2, x, y+n//2) #2사분면
                cut (n//2, x+n//2, y) #3사분면
                cut (n//2, x+n//2, y+n//2) #4사분면
                return

    if check == 0:
        white += 1
        return
    else:
        blue += 1
        return

cut(n)
print(white)
print(blue)



