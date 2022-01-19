def max_of(x):
    maximum = x[0]
    for i in range(1, len(x)):
        if x[i] > maximum:
            maximum = x[i]
    return maximum

num = int(input())
x = [None] * num

for i in range(num):
    x[i] = int(input(f'x[{i}]값을 입력하시오'))
print(f'최댓값은 {max_of(x)}, 순서는{x.index(max_of(x))+1}  입니다.')
# max_of(x) = 53

# num_list = []
# for i in range(9):
#     num_list.append(int(input()))

# print(max(num_list))
# print(num_list.index(max(num_list))+1)