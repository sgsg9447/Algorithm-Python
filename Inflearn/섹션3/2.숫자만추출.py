s = input()
res = 0 #result의 약자
for x in s:
    if x.isdecimal(): #1~9 까지 숫자
        res = res*10 + int(x)
print(res)
cnt = 0
for i in range(1, res+1):
    if res%1==0:
        cnt+=1
print(cnt)

 