#내코드

t = int(input())
n = input()
n_list = []
sum = 0
for i in range(t):
    n_list.append(n[i])
n_list = list(map(int, n_list))

sum = 0

for i in range(t):
    sum += n_list[i]

# print(sum)

#직관적인 정답코드
x = int(input())
n = input()

cnt = 0

for i in n:
    cnt = cnt + int(i)

print(cnt)

#더짧은 정답코드

input()
print(sum(map(int, input())))