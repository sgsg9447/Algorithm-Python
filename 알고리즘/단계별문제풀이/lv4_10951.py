#탈출조건 없을때!
#입력이 끝날 때까지 A+B를 출력하는 문제. EOF에 대해 알아 보세요.

while True:
    try:
        a,b = map(int,input().split())
        print(a+b)
    except:
        break