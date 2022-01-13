a = int(input())
b = int(input())
c = int(input())

x = a*b*c
# print(x)
list = []

for i in range(len(str(x))):
    list.append(str(x)[i])

# print(list)

for i in range(10):
    print(list.count(str(i)))
