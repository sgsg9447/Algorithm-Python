def demical_def(num):
    if num > 1:
        for i in range(2, num//2+1):
            if num % i == 0:
                return False
        return True
    return False


t = int(input())

for i in range(t):
    n = int(input())
    for i in range(n//2):
        a = n//2 + i
        b = n//2 - i
        if demical_def(a) & demical_def(b) == True:
            print(f'{b} {a}')
            break
    