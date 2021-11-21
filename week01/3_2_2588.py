# a = int(input())
# b = input()

# for i in range(-1, -len(b)-1, -1):
#     print(a * int(b[i]))
    
# print(a*int(b))


num1 = int(input())
num2 = int(input())

while num2 != 0:
    print(num1*(num2%10))
    num2 = num2//10
    print(f'num2: {num2}')