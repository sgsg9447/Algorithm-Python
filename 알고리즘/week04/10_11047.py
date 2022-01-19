n,k = map(int, input().split())
coin_list=[]
for _ in range(n):
    coin_list.append(int(input()))
coin_list.sort(reverse=True)
total_sum = 0

for coin in coin_list:
    if coin <= k:
        total_sum += k//coin
        k = k%coin
    else:
        continue

print(total_sum)

