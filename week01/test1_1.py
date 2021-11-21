x,y = map(int,input().split())
day = ['SUN','MON','TUE','WED','THU','FRI','SAT']


if x == 1 or x == 4 or x == 10:
    for i in range(7):
        if y%7 == i:
            print(day[i]) 
if x == 2 or x == 3 or x == 11:
    for i in range(7):
        if y%7 == i:
            print(day[i-4])
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
elif x == 9 or x == 12:
    for i in range(7):
        if y%7 == i:
            print(day[i-2])




x, y = map(int, input().split())

month_31 = [1, 3, 5, 7, 8, 10, 12]
month_30 = [4, 6, 9, 11]
month_28 = [2]

day = 0
for i in range(1, x):
    if i in month_31:
        day += 31
    elif i in month_30:
        day += 30
    elif i in month_28:
        day += 28

day += y

if day % 7 == 1:
    print("MON")
elif day % 7 == 2:
    print("TUE")
elif day % 7 == 3:
    print("WED")
elif day % 7 == 4:
    print("THU")
elif day % 7 == 5:
    print("FRI")
elif day % 7 == 6:
    print("SAT")
elif day % 7 == 0:
    print("SUN")


import sys

x, y = map(int, sys.stdin.readline().split())



total_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def checking(x, y):
    if x == 1:
        idx = y
        print(flatten_days[idx])
    else:
        idx = y + sum(total_month[:x-1])
        print(flatten_days[idx])



exact_days = [["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"] for _ in range(60)]
flatten_days = sum(exact_days, [])
checking(x, y)
