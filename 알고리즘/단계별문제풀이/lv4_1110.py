# n = input()
# n_list = []
# ans_list=[]

# if int(n)<10:
#     n_list.append(0)
#     n_list.append(n)

# else:
#     n_list.append(int(n[0]))
#     n_list.append(int(n[1]))

# first_ans = str(n_list[0] + n_list[1])
# print('first_ans :', first_ans)
# ans_list.append(n_list[1])
# ans_list.append(int(first_ans[-1]))
# print('ans_list :',ans_list)
# cnt = 0
# tmp = n
# print('tmp : ', tmp)
# # ans = 
# # while n != ans:
#     # ans = ans_list[0] + ans_list[1]
#     # ans = str(ans)
#     # ans_list.append(int(ans[-1]))
#     # print('ans_list2: ', ans_list)
# res = ans_list[-1]+ans_list[-2]
# tmp = 
# res = str(res)
# ans_list.append(int(res[-1]))
# cnt += 1
# res = ans_list[-1]+ans_list[-2]
# tmp = res
# print('tmp : ', tmp)
# res = str(res)
# ans_list.append(int(res[-1]))
# cnt += 1
# res = ans_list[-1]+ans_list[-2]
# tmp = res
# print('tmp : ', tmp)
# res = str(res)
# ans_list.append(int(res[-1]))
# cnt += 1
# res = ans_list[-1]+ans_list[-2]
# tmp = res
# print('tmp : ', tmp)
# res = str(res)
# ans_list.append(int(res[-1]))
# cnt += 1
# print('ans_list2:',ans_list)
# print('cnt : ', cnt)

#다시
input_num = tmp = int(input())
cnt = 0

while True:
    num1 = tmp // 10
    num2 = tmp % 10
    sum_num = num1+num2
    tmp = int(str(num2)+str(sum_num % 10))
    cnt += 1
    if input_num == tmp:
        break
print(cnt)



# n = tmp = input()
# n_list = []
# ans_list=[]

# if int(n)<10:
#     n_list.append(0)
#     n_list.append(n)

# else:
#     n_list.append(int(n[0]))
#     n_list.append(int(n[1]))
# print('n_list : ', n_list)
        # res = ans_list[-1]+ans_list[-2]
# tmp = 
# res = str(res)
# ans_list.append(int(res[-1]))
# cnt += 1