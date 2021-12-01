arr = input().split('-') #입력 받을 때에 '-' 기준으로 쪼갠다
ans = 0 
for i in arr[0].split('+'): #0번째 원소는 맨 처음 숫자부터 연산자 - 나오기 전까지 숫자들로 구성되어있으므로, 해당 인덱스안에있는 숫자 모두 더해주기
    ans += int(i)

for i in arr[1:]: #빼줘야할 숫자들중 +와 함께있는 숫자들 계산!
    for j in i.split('+'):
        ans -= int(j)

print(ans)