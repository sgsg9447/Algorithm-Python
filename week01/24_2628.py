x,y = map(int, input().split())
n = int(input())
x_list = [0, x ]
y_list = [0, y ]

for i in range(n):

    v,k = map(int, input().split())
    if v == 0:
        y_list.append(k)
    elif v ==1 :
        x_list.append(k)

x_list.sort()
y_list.sort()

max_squre = 0
for i in range(1, len(x_list)):
    for j in range(1, len(y_list)):
        width = y_list[j] - y_list[j-1]
        height = x_list[i] - x_list[i-1]
        max_squre = max(max_squre, width * height)

print(max_squre)

