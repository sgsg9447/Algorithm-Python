H,M = map(int,input().split())
if M<45:
    if H==0:
        print(23, M+15)
    else:
        print(H-1, M+15)
elif M>45:
    print(H, M-45)
else:
    print(H,0)

a,b=map(int,input().split())
c=a*60+b-45
print(c//60%24, c%60)