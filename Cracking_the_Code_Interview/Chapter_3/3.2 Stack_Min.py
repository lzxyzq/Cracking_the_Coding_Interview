# How would you design a stack which,in addition to push and pop,has a function min which returns the minimum element? Push,pop and min should all operate in O(1) time.

class MinStack(object):
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        if len(self.min_stack) == 0 or x <= self.min_stack[len(self.min_stack)-1]:
            self.min_stack.append(x)

    def pop(self):
        """
        :rtype: None
        """
        item = self.stack.pop()
        if item == self.min_stack[-1]:
            self.min_stack.pop()
        return item

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0 :
            return None
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.min_stack) == 0:
            return None
        else:
            return self.min_stack[-1]
        
if __name__ == '__main__': 
    min_stack = MinStack()
    min_stack.push(5)
    min_stack.push(6)
    min_stack.push(7)
    min_stack.top()
    print(min_stack.stack)
    print(min_stack.pop())
    print(min_stack.top())
    print(min_stack.getMin()) 