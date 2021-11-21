s = int(input())
for i in range(s):
    n, alphabets = input().split()
    for alphabet in alphabets:
        print(x*int(n), end='')
    print()



s = int(input())
for i in range(s):
    n, word = list(input().split())

    re_word = ""
    for j in range(len(word)):
        print("for j start")
        re_word += (int(n) * word[j])
    print(re_word)