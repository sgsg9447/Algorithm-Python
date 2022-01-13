# 0이 들어올 때까지 A+B를 출력하는 문제

while(1):
    a,b = map(int,input().split())
    if (a ==0 and b==0):
        break
    else:
        print(a+b)
    