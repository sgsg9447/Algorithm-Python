#-*- coding: utf-8 -*-

data = [[1,2,3], [4,5,6], [7,8,9]]
print(data[0])
#[1, 2, 3]
print(data[0][0])
#[1]

# #위의 2차원 배열에서 9,8,7 순서로 출력해보기
print(data[2][2])

# #다음 dataset에서 'M'이 몇번 나왔는지 출력하는 프로그램 작성
dataset = ['Merry', 'Memory', 'seulgi', 'jungle', 'Hi', 'Mirror', "MiMo"]
M_count = 0
for data in dataset:
    for index in range(len(data)):
        if data[index] == 'M':
            M_count += 1
print(M_count)