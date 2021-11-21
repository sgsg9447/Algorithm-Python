s = input()
stack = []
cnt = 0
for i in range(len(s)):
    if s[i]=='(':
        stack.append(s[i])
    else:
        if s[i-1]=='(': #레이져인지!
            stack.pop()
            cnt += len(stack)
        else:
            stack.pop() #쇠막대기 시작지점
            cnt += 1  #마지막 부분 카운트!

print(cnt) 
