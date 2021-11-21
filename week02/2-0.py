import sys
string = sys.stdin.readline().strip()
bomb = sys.stdin.readline().strip()
 
lastChar = bomb[-1] 
stack = []
length = len(bomb) 
for char in string:
    stack.append(char)
    if char == lastChar and ''.join(stack[-length:]) == bomb:
        print(stack)
        print(stack[-length:])
        print('aaaaaa'.join(stack[-length:]))
        del stack[-length:]
answer = ''.join(stack)
if answer == '':
    print("FRULA")
else:
    print(answer)
