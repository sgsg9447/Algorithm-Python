#-*- coding: utf-8 -*-

#재귀함수
# def recursive(data):
#     if data < 0:
#         print ("ended")
#     else:
#         print(data)
#         recursive(data-1)
#         print("returned", data)

# recursive(4)

#파이썬 리스트 기능에서 제공하는 메서드로 스택 사용해보기
#append(push), pop메서드 제공

# data_stack = list()
# data_stack.append(1)
# data_stack.append(2)
# print(data_stack)

# print(data_stack.pop())

#연습1. 리스트 변수로 스택을 다루는 pop, push 기능 구현해보기 (pop, push함수 사용하지 않고 직접 구현해보기!)
stack_list = list()
def push(data):
    stack_list.append(data)

def pop():
    stack_list[-1]
    del stack_list[-1]
    return

for index in range(10):
    push(index)
    pop()
print(index)