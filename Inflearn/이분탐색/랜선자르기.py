def Count(len):
    cnt = 0
    for x in line:
        cnt += (x//len)
    return cnt


k, n = map(int, input().split())
line = []
res = 0
largest = 0
for i in range(k):
    tmp = int(input())
    line.append(tmp)
    largest = max(largest, tmp)
start = 1
end = largest

while start <= end:
    mid = (start + end)//2
    if Count(mid)>=n:
        res = mid
        start=mid + 1

    else:
        end = mid - 1

print(res)
