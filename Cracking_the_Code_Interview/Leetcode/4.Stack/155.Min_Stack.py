'''
@Author: your name
@Date: 2020-06-17 16:03:43
@LastEditTime: 2020-06-17 17:18:23
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/Stack/155.Min_Stack.py
'''
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.

class MinStack:
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []

    def push(self, x: int):
        self.stack.append(x)
        if len(self.min_stack) == 0 or x < self.min_stack[len(self.min_stack)-1]:
            self.min_stack.append(x)

    def pop(self):
        item = self.stack.pop()
        if item == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self):
        if len(self.stack) == 0 :
            return None
        return self.stack[-1]

    def getMin(self):
        if len(self.min_stack) == 0:
            return None
        else:
            return self.min_stack[-1]