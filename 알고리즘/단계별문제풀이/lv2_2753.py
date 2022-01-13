years = int(input())
yoon = ((years %4 ==0) and (years%100 != 0)) or(years % 400 ==0)
if yoon:
    print("1")
else:
    print("0")
#처음엔 if years==yoon으로 하였다! 
#yoon은 bool타입 이기에 오류가남!
print(type(years))
print(type(yoon))