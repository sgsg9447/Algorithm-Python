#처음 생각한 풀이

# input_list=[]
# for _ in range(10):
#     a = int(input())
#     input_list.append(a)

# # print(input_list)

# div_list=[]
# for i in input_list:
#     d = i % 42
#     div_list.append(d)

# # print(div_list)

# print(len(set(div_list)))


#짧은 풀이!!!
arr = []
for i in range(10):
    tmp = int(input())%42
    arr.append(tmp)

print(len(set(arr)))