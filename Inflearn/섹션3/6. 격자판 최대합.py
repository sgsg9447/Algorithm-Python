n = int(input())
a =[list(map(int,input().split())) for _ in range(n)] #한줄읽어서 리스트화 시킨것!
for x in a:
    print(x) #2차원 리스트 처럼 보이게 출력!
largest = -2147000000 #가장 작은 값으로 초기화!
for i in range(n):
    sum1 = sum2 = 0
    for j in range(n):
        sum1 += a[i][j]
        sum2 += a[j][i]
    if sum1 > largest:
        largest = sum1
    if sum2 > largest:
        largest = sum2
#행과 열의 최대합이 largest에 저장되었음.
sum1 = sum2 = 0
for i in range(n):
    sum1 += a[i][i]
    sum2 += a[i][n-i-1]
if sum1 > largest:
    largest = sum1
if sum2 > largest:
    largest = sum2

print(largest)