# for i in range(5):
# 	for j in range(i+1):
# 		print("*",end=' ')
# 	print()

# for i in range(5):
#     for j in range(5-i):
#         print("*", end=' ')
#     print()
# msg='It is Time'
# tmp=msg.upper() # IT IS TIME
# print(tmp)
# print(tmp.find('T'))


# for i in range(len(msg)):
# 	print(msg[i], end=' ')

# for x in msg:
#     print(x, end=' ')

# for x in msg:
#     if x.isupper():
#         print(x, end=' ')

# for x in msg:
#     if x.islower():
#         print(x, end=' ')

# for x in msg:
#     if x.isalpha(): #알파벳일때만 참
#         print(x, end='')
# print()

# tmp='AZ'
# for x in tmp:
#     print(ord(x)) #아스키 넘버 출력 #65 #90

# tmp=65
# print(chr(tmp)) #숫자를 아스키넘버의 문자열로 변환

# a = [23, 12, 36, 53, 19]
# # for x in enumerate(a):
# #     print(x[0],x[1])

# # for x in enumerate(a):
# # 	print(x) 

# for index, value in enumerate(a):
#     print(index, value)


# def isPrime(x):
# 	for i in range(2,x): #x의 약수는 1과 자기자신빼곤 존재하지 않아야지! 만약 이사이에 약수가 있다면, False 인거지
# 		if x%i == 0:
# 			return False
# 	return True  
# a = [12, 13, 7, 9, 19]
# for s in a:
# 	if isPrime(s):
# 	    print(s, end=' ')

# def plus_one(x):
#     return x+1

# print(plus_one(1))

plus_two = lambda x: x+2
print(plus_two(1))

def plus_one(x):
    return x+1
a=[1, 2, 3]
print(list(map(plus_one, a)))

print(list(map(lambda x:x+1, a)))
