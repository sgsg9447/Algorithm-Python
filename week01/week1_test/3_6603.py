from itertools import combinations

while True:
    ins = list(map(int, input().split()))

    if ins[0] == 0:
        break

    case_num = ins[0]
    nums = ins[1:]

    coms = list(combinations(nums, 6))

    for com in coms:
        list(com)
        print(*com)

    print()