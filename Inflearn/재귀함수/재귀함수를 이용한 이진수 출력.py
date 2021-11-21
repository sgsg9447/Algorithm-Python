def DFS(x):
    if x==0:
        return #함수값을 반환해주는 의미도 있고, 함수를 종료시킨다 라는 의미도 있음.
    else:
        DFS(x//2)
        print(x%2, end=' ') #2로 나눈 나머지 #DFS함수 밑으로 해야 제대로 나옴! 아니면, 거꾸로나옴


if __name__ == "__main__":
    n=int(input())
    DFS(n)


