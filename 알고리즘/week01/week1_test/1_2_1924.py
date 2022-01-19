m,d =map(int, input().split())
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

count = d

for i in range(m-1):
    count += days[i]

num = count % 7

dayOfWeek = ['SUN','MON','TUE','WED','THU','FRI','SAT','SUN']

ans = dayOfWeek[num]

print(ans)