
def n_queens(i, col):
    cnt = 0
    n =  len(col) -1
    if(promising(i,col)):
        if (i ==n):
            print(col[1:n+1])

        else:
            for j in range(1, n+1):
                col[i+1] = j
                n_queens(i+1, col)

def promising(i, col):
    k = 1
    flag = True
    while(k<i and flag):
        if (col[i] == col[k] or abs(col[i]-col[k]) == (i-k)):
            flag = False
        k += 1
    return flag



n = 8
col = [0]*(n+1)
n_queens(0, col)


