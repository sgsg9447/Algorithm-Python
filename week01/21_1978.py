n = int(input())
numbers = map(int,input().split())
demical = 0
for num in numbers:
    ctn = 0
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                ctn += 1
                break
        if ctn == 0:
            demical += 1
print(demical)

# import math

# n = int(input())
# numbers = map(int,input().split())
# demical = 0
# for num in numbers:
#     ctn = 0
#     if num > 1:
#         for i in range(2, math.sqrt(num)):
#             if num % i == 0:
#                 ctn += 1
#                 break
#         if ctn == 0:
#             demical += 1
# print(demical)