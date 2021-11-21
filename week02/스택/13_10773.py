n = int(input())
stack = []
for x in range(n):
    x = int(input())
    if x != 0:
        stack.append(x)
    else:
        stack.pop()

print(sum(stack))