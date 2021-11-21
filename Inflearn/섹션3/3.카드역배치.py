# a, b = map(int,input().split())
# print(a, b)
# a, b = b, a #스와프 하는 방법!
# print(a,b)

list = list(range(1,21))
print(list)

for _ in range(10):
    s, e = map(int,input().split())
    for i in range((e-s+1)//2): #갯수만큼 절반!!
        list[s+i], list[e-i] = list[e-i], list[s+i]

print(list)

for x in list:
    print(x, end='')