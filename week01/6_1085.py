# def MinValue(A):
#     Temp = 0
#     for i in A :
#         if Temp == 0 or i < Temp :
#             Temp = i
#     print(Temp)
 
# 한수는 지금 (x, y)에 있다. 직사각형은 각 변이 좌표축에 평행하고, 왼쪽 아래 꼭짓점은 (0, 0), 오른쪽 위 꼭짓점은 (w, h)에 있다. 직사각형의 경계선까지 가는 거리의 최솟값을 구하는 프로그램을 작성하시오.


x,y,w,h = list(map(int,input().split(" ")))
# print(min((h-y, w-x, x, y)))

minimum = x

if minimum > y:
    minimum = y
if minimum > (w-x):
    minimum = (w-x)
if minimum > (h-y):
    minimum = (h-y)

print(minimum)