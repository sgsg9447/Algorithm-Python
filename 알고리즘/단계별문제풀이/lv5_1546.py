# import statistics

# n = int(input())

# list = list(map(int,input().split()))

# m = max(list)
# # print(list)

# m_list= []
# for i in range(len(list)):
#     div = list[i]/m*100
#     m_list.append(div)

# # print(m_list)
# print(statistics.mean(m_list))

#두번째
n = int(input())
list = list(map(int,input().split()))
m = max(list)

sum = 0
for i in range(len(list)):
    sum += list[i]/m*100
print(sum/n)

