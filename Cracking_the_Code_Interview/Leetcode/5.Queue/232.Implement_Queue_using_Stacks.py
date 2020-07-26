
# Implement the following operations of a queue using stacks.

# push(x) -- Push element x to the back of queue.
# pop() -- Removes the element from in front of queue.
# peek() -- Get the front element.
# empty() -- Return whether the queue is empty.

""" Example:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);  
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false
Notes:

1.You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
2.Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
3.You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue). """

class MyQueue:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.temp = []

    def push(self, x: int) :
        """
        Push element x to the back of queue.
        """
        while(self.stack):
            element = self.stack.pop()
            self.temp.append(element)
        self.temp.append(x)
        while(self.temp):
            element = self.temp.pop()
            self.stack.append(element)
            
    def pop(self) :
        """
        Removes the element from in front of queue and returns that element.
        """
        if len(self.stack) == 0:
            return None
        else:
            return self.stack.pop()

    def peek(self) :
        """
        Get the front element.
        """
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[-1]

    def empty(self) :
        """
        Returns whether the queue is empty.
        """
        if len(self.stack) == 0:
            return True
        else:
            return False
