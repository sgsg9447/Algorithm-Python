#동적 계획법(DP)
#입력 크기가 작은 부분문제들을 해결한 후, 해당부분문제의 해를 활용해서, 보다 큰 크기의 부분문제를 해결, 최종적으로 전체 문제를 해결하는 알고리즘
#상향식 접근법, 가장 최하위 해답을 구한 후, 이를 저장 후 , 해당 결과값을 이용해서 상위 문제를 풀어가는 방식
#memoization 기법을 사용함
#: 프로그램 실행 시 이전에 계산한 값을 저장하여, 다시 계산하지 않도록 하여 전체 실행 속도를 빠르게 하는 기술
#부분문제는 중복되어, 상위 문제 해결시 재활용됨

#피보나치 수열문제!
#reculsive call 활용

# def fibo(num):
#     if num <= 1:
#         return num
#     return fibo(num-1) + fibo(num-2)

# print(fibo(4))

#동적계획법 활용
def fibo_dp(num):
    # cache = [0 for index in range(num+1)]
    cache = [0] * (num+1)
    cache[0] = 0
    cache[1] = 1
    
    for index in range(2, num+1):
        cache[index] = cache[index-1]+cache[index-2]
    return cache[num]
    
print(fibo_dp(10))