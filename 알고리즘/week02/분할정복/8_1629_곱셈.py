def power(a,b):
    if b == 1: #b의 값이 1이면 a%c를 return
        return a % c
    else:
        temp = power(a,b // 2) #a의 b를 2로 나눈 몫
        if b % 2 ==0:
            return temp * temp % c #b가 짝수인 경우
        else:
            return temp * temp * (a % c) % c #b가 홀수인 경우

a,b,c = map(int,input().split())
result = power(a,b)
print(result)