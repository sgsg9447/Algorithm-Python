from bisect import bisect_left


arr = [10, 15, 20, 300, 200]
arr.sort()
print(arr)
ans=[10, 15]

value = 300
index = bisect_left(arr, value)

print(index)