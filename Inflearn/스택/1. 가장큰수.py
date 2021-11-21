num, m= map(int, input().split())
num = list(map(int, str(num)))
stack = []
for x in num:
    while stack and m>0 and stack[-1]<x: #비어있으면 거짓 비어있지않으면 참 , #m이 0보다 커야 pop시킬 수 있지, stack[-1]맨뒤 숫자가 x(나라고 생각)보다 작더라 그럼 끄집어내! 
        stack.pop()
        m -= 1 #줄였으니, m을 1빼줘야지
    stack.append(x)

if m!=0:
    stack = stack[:-m] #제일 앞에서부터 m전까지 날려버리는것

# print(stack) #[7, 8, 2, 3]


# #결과값 붙여서 나타내는법 #7823
# res= ''.join(map(str, stack))
# print(res) 

#결과값 붙여서 나타내는법2
for x in stack:
    print(x, end='')

