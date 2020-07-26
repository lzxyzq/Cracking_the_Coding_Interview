'''
@Author: your name
@Date: 2020-06-06 00:13:03
@LastEditTime: 2020-06-06 14:31:55
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/Singly_Linked_List/146.LRU.py
'''
# Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

# Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

# Follow up:
# Could you do both operations in O(1) time complexity?


# https://www.youtube.com/watch?v=kGlSZdDfm8M
# 为了使查找、插入和删除都有较高的性能，这题的关键是要使用一个双向链表和一个HashMap，因为：
#   1.HashMap保存每个节点的地址，可以基本保证在O(1)时间内查找节点
#   2.双向链表能后在O(1)时间内添加和删除节点，单链表则不行
# 具体实现细节：
#   1.越靠近链表头部，表示节点上次访问距离现在时间最短，尾部的节点表示最近访问最少
#   2.访问节点时，如果节点存在，把该节点交换到链表头部，同时更新hash表中该节点的地址
#   3.插入节点时，如果cache的size达到了上限capacity，则删除尾部节点，同时要在hash表中删除对应的项；新节点插入链表头部

class dll:
    def __init__(self,key,val):
        self.key = key
        self.val = val 
        self.next = None
        self.prev = None
class LRUCache: 
    def __init__(self, capacity: int):
        self.head = dll(-1,-1)
        self.tail = self.head
        self.capacity=capacity
        self.hash = {}
        self.length = 0

    def get(self, key: int) :
        if key not in self.hash:
            return -1 
        node = self.hash[key]
        val = node.val
        while node.next:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.tail.next = node
            node.prev = self.tail
            node.next =None
            self.tail = node
        return val

    def put(self, key: int, value: int) :
        if key in self.hash:
            node =self.hash[key]
            node.val = value
            while node.next:
                node.prev.next = node.next
                node.next.prev = node.prev
                self.tail.next = node
                node.prev = self.tail
                node.next = None
                self.tail = node
        else:
            node = dll(key,value)
            self.hash[key] = node
            self.tail.next = node
            node.prev = self.tail
            self.tail = node 
            self.length += 1 
            if self.length > self.capacity:
                remove = self.head.next
                self.head.next = self.head.next.next
                self.head.next.prev = self.head
                del self.hash[remove.key]
                self.length -= 1