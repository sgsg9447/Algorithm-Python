n = int(input())
a = list(map(int,input().split()))
ave = round(sum(a)/n)
min = 2147000000 
for idx, x in enumerate(a): #리스트 인덱스 값과, 값을 쌍으로 대응
    tmp = abs(x-ave)
    if tmp < min :
        min = tmp
        score = x
        res = idx + 1 # 0부터 시작하여서!
    elif tmp == min:
        if x > score:
            score = x
            res = idx + 1
print(ave, res)
