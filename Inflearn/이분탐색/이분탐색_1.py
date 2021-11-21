n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
start = 0
end = n-1
while start <= end:
    mid = (start+end)//2
    if a[mid] == m: #a의 중간에 있는 값이 입력받은 m과 같은지?
        print(mid+1) # 몇번째 이냐니까, +1
        break
    elif a[mid]>m:
        end = mid-1
    else:
        start = mid + 1
         
