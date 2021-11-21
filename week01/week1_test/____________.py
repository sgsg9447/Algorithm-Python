from itertools import permutations, combinations

# List all permutation for answer
ans = []
li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pers = list(combinations(li, 3))
for per in pers:
    per2 = list(permutations(per, 3))
    for p in per2:
        ans.append(list(p))

guess_num = int(input())

for _ in range(guess_num):
    guess, s, b = input().split()
    s = int(s)
    b = int(b)

    guess_list = []

    for j in guess:
        guess_list.append(int(j))

    for idx, i in enumerate(ans):
        strike = 0
        ball = 0
        for index, num in enumerate(i):
            if num == guess_list[index]:
                strike += 1
            elif num == guess_list[index - 1] or num == guess_list[index - 2]:
                ball += 1
        if strike != s or ball != b:
            ans[idx] = [0, 0, 0]

final_count = 0

for k in ans:
    if k != [0, 0, 0]:
        final_count += 1

print(final_count)


