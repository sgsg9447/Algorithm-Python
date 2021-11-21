def DFS(x):
    if x >0:
        DFS(x-1)
        print(x, end=' ')

if __name__ == "__main__": #메인함수와 재귀함수 구분
    n = int(input())
    DFS(n)
