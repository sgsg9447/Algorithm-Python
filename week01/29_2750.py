#1번풀이
# N = int(input())
# numbers = []
# for i in range(N):
#     numbers.append(int(input()))
# for i in range(len(numbers)):
#     for j in range(len(numbers)):
#         if numbers[i] < numbers[j]:
#             numbers[i], numbers[j] = numbers[j], numbers[i]
# for n in numbers :
#     print(n)


#2번 풀이
# N = int(input())

# numbers = []

# for i in range(N):
#     numbers.append(int(input()))

# numbers = sorted(numbers)
# for i in range(len(numbers)):
#     print(numbers[i])

# 3번 풀이
N = int(input())
numbers = []
for i in range(N):
    numbers.append(int(input()))
numbers = list(numbers)
numbers.sort()
print(numbers)
# for i in range(len(numbers)):
#     print(numbers[i])