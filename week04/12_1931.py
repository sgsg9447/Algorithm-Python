n = int(input())
meeting = []

for i in range(n):
    start, end = map(int,input().split())
    meeting.append((start, end))
meeting.sort(key = lambda x : (x[1],x[0]))#정렬순서를 end를 우선수위로하고 start를 다음순위로 해라!

end_time = 0
cnt=0

for start,end in meeting:
    if start >= end_time:
        end_time = end
        cnt += 1

print(cnt)