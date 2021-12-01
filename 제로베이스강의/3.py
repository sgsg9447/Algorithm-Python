# #1부터 num까지 곱이 출력되게 만드세요

# def multiple(num):
#     if num <= 1:
#         return num
#     return num * multiple(num-1)
    
# print(multiple(10)) 

# #숫자가 들어 있는 리스트가 주어졌을 대, 리스트의 합을 리턴하는 함수를 만드세요.
# import random
# data = random.sample(range(100), 10) #0~99까지 중에서, 임의로 10개 만들어서 10개 값 가지는 리스트 변수 만들기!

# def sum_list(data):
#     if len(data) <= 1:
#         return data[0]
#     return data[0] + sum_list(data[1:])

# print(sum_list(data))

# #회문 프로그래밍 만들기

# def palindrome(string):
#     if len(string) <=1:
#         return True
#     if string[0] == string[-1]:
#         return palindrome(string[1:-1])
#     else:
#         return False

# #정수n에 대해 n이 홀수이면 3 x n+1을 하고, n이 짝수이면 n을 2로 나눕니다. 이렇게 계속진행해서 n이 결국 1이 될때 까지 2와 3의 과정을 반복합니다.
# def func(n):
#     print(n)
#     if n == 1:
#         return n
#     if n % 2 == 1: #경우의 수를 나누어서 2번 리턴!
#         return(func((3*n)+1)) #홀수일때
#     else:
#         return(func(int((n/2)))) #짝수일때

# print(func(3))

def func(data):
    if data == 1:
        return 1
    elif data == 2:
        return 2
    elif data == 3:
        return 4

    return func(data-1)+func(data-2)+func(data-3)

print(func(4))