N = int(input())

n_list = []
for _ in range(N):
    n_list.append(int(input()))

cnt = 1
max = n_list[-1]
for i in n_list[::-1]:
    if max < i:
        cnt += 1
        max = i
print(cnt)