#오늘은 2007년 1월 1일 월요일이다. 그렇다면 2007년 x월 y일은 무슨 요일일까? 이를 알아내는 프로그램을 작성하시오.

x,y = map(int,input().split())
day = ['SUN','MON','TUE','WED','THU','FRI','SAT']

if x == 1:
    for i in range(7):
        if 1<=y<=31 & y%7 == i:
            print(day[i]) 
if x == 2 :
    for i in range(7):
        if y <= 28 and y%7 == i:
            print(day[i-4])

if x == 2 :
    for i in range(7):
        if y%7 == i:
            print(day[i-4])

elif x == 4:
    for i in range(7):
        if y%7 == i:
            print(day[i])

elif x == 5:
    for i in range(7):
        if y%7 == i:
            print(day[i-6])

elif x == 6:
    for i in range(7):
        if y%7 == i:
            print(day[i-3])

elif x == 7:
    for i in range(7):
        if y%7 == i:
            print(day[i-1])

elif x == 8:
    for i in range(7):
        if y%7 == i:
            print(day[i-5])

elif x == 9:
    for i in range(7):
        if y%7 == i:
            print(day[i-2])

elif x == 10:
    for i in range(7):
        if y%7 == i:
            print(day[i])

elif x == 11:
    for i in range(7):
        if y%7 == i:
            print(day[i-4])

elif x == 12:
    for i in range(7):
        if y%7 == i:
            print(day[i-2])



# if x == 2:
#     if y%7 == 1:
#         print(day[4]) #thu
#     elif y%7 == 2:
#         print(day[5]) #fri
#     elif y%7 == 3:
#         print(day[6]) #sat
#     elif y%7 == 4:
#         print(day[0]) #sun
#     elif y%7 == 5:
#         print(day[1]) #mon
#     elif y%7 == 6:
#         print(day[2]) #tue
#     elif y%7 == 0:
#         print(day[3]) #wed
