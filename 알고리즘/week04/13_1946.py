# n= int(input())
# body = []
# for i in range(n):
#     a,b = map(int, input().split())
#     body.append((a,b))
# #키순 내림차순 !
# body.sort(reverse=True)
# largest=0
# cnt = 0
# #x=키 y=몸무게 
# for x,y in body:
#     if y > largest:
#         largest = y #최댓값 갱신
#         cnt +=1

# print(cnt)
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    list=[]
    for _ in range(n):
        resume, interview = map(int,input().split())
        list.append((resume,interview))
    list.sort()
    min = list[0][1]
    cnt =1
    for x, y in list:
        if y < min:
            min=y
            cnt+=1
    print(cnt)
