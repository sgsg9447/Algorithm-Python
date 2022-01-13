#-*- coding: utf-8 -*-


import queue

data_queue = queue.Queue() #일반적인 FIFO queue #소문자 queue는 라이브러리 명이고, 대문자 Queue는 일종의 클래스 

data_queue.put('sseul')
data_queue.put(1)

print(data_queue.qsize())  #2

data_queue.get() #'sseul'빠져나오겠지

print(data_queue.qsize()) #1

##############################################################

data_queue = queue.LifoQueue()

data_queue.put(10)
data_queue.put(100)

print(data_queue.qsize())  #2

print(data_queue.get()) #100

###############################################################

import queue

data_queue = queue.PriorityQueue()
data_queue.put((10, "sseul")) #튜플형식으로 첫번째 항목은 우선순위, 두번째는 데이터 
data_queue.put((5,1))
data_queue.put((1,1))

print(data_queue.qsize()) #3

print(data_queue.get()) #(1,1)

print(data_queue.get()) #(5,1)

##############################################################

#연습 : 리스트변수로 큐를 다루는 enqueue, dequeue 기능 구현

queue_list = list()

def enqueue(data):
    queue_list.append(data)
def dequeue():
    data = queue_list[0]
    del queue_list[0] #이부분을 안해주면 계속 0번째 데이터의 동일한 값만 나오겠지!
    return data

for index in range(10):
    enqueue(index)

print(len(queue_list)) #10

print(dequeue()) #0

print(dequeue()) #1

print(dequeue()) #2

