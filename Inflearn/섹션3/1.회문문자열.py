# n = int(input())
# for i in range(n):
#     s = input()
#     s = s.upper()
#     # size = len(s)
#     for j in range(len(s)//2):
#         if s[j] != s[-1-j]:
#             print("#%d NO" %(i+1))
#             break
#     else:
#         print("#%d YES" %(i+1))

# n = int(input())
# for i in range(n):
#     s = input()
#     s = s.upper()
#     # print(s[::-1]) #맨뒤부터 하나씩 작아지며 문자열을 거꾸로 바꿔라!
#     if s == s[::-1]:
#         print("#%d YES" %(i+1))
#     else:
#         print("#%d NO" %(i+1))

n = int(input())
for i in range(n):
    s = input()
    s = s.upper()
    # size = len(s)
    for j in range(len(s)//2):
        if s[j] == s[-1-j]:
            print("#%d YES" %(i+1))
            break
    else:
        print("#%d NO" %(i+1))

n = int(input())
for i in range(n):
    s = input()
    s = s.upper()
    for j in range(len(s)//2):
        if s[j] == s[-1-j]:
            print("#%d YES" %(i+1))
            break
    else:
        print("#%d NO" %(i+1))

