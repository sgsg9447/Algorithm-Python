from itertools import permutations, combinations

ans =[]
li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pers = list(combinations(li, 3)) #combinations = 조합 = 순서X ,3개짜리 [ , , ]조합을 만든다
for per in pers:
    per2 = list(permutations(per,3)) #permutations = 순열 = 순서O, 각각의 3개짜리 [ , , ] [ , , ]  --- 무수히 만든다. 만들수 있는 경우의 수 다 만든다
    for p in per2:
        ans.append(list(p)) #만약 p값이 per2 순열 안에 있다면, p에 더해서 리스트화 어팬드!

guess_num = int(input()) 

for _ in range(guess_num):
    guess, s, b =(input().split())
    s = int(s)
    b = int(b)

    guess_list = [] #빈배열 받기

    for j in guess:
        guess_list.append(int(j))
    
    for idx, i in enumerate(ans):
        strike = 0
        ball = 0
        for index, num in enumerate(i):
            if num == guess_list[index]: #만약 num값이 guess_list[]인덱스 값 과 동일하다면(위치), 스트라이크 +1
                strike += 1
            elif num == guess_list[index - 1] or num == guess_list[index - 2]: #만약, num값과 guess_list의 다른 순서와 값이 동일하다면, 볼 +1
                ball += 1
        if strike != s or ball != b: #만약 스트라이크, 볼 둘다 아닌경우, ans배열을 [0,0,0]으로 초기화한다.
            ans[idx] = [0,0,0]

final_count = 0

for k in ans :
    if k != [0,0,0]:
        final_count += 1

print(final_count)