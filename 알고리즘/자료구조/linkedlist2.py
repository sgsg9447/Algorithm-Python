#-*- coding: utf-8 -*-

#각각의 노드 생성할수있는 클래스
class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

# 노드매니지먼트 각각의 링크드리스트를 관리할 수 있는 클래스
class NodeMgmt:
    def __init__(self,data):
        self.head = Node(data)
    def add(self,data) :
        if self.head == '':
            self.head = Node(data) 
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data) 

    def desc(self): #순회하는것
        node = self.head
        while node:
            print(node.data)
            node = node.next
    
    def delete(self, data):
        if self.head == '':
            print("해당 값을 가진 노드가 없습니다.")
            return
        
        if self.head.data == data:
            temp = self.head
            self.head = self.head.next
            del temp
        else:
            node = self.head
            while node.next:
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next
                    del temp   
                    return
                else:
                    node = node.next

linkedlist1 = NodeMgmt(0)
print(linkedlist1.desc())

for data in range(1,10):
    linkedlist1.add(data) 
print(linkedlist1.desc())
