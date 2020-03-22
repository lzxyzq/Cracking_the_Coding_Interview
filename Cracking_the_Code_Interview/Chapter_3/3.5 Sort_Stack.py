# Write a program to sort a stack such that the smallest items are on the top. You can use an additional temporary stack,but you may not copy the elements into any other data structure. The stack supports the following operations: push,pop,peek,and isEmpty.


class Stack():
    def __init__(self):
        self.array = []

    def push(self,item):
        self.array.append(item)

    def pop(self):
        if not len(self.array):
            return None
        return self.array.pop()

    def top(self):
        return self.array[len(self.array)-1]
    
    def isEmpty(self):
        return len(self.array) == 0

def sortStack(stack):
    tempStack = Stack()
    while(stack.isEmpty() == False):
        temp = stack.top()
        stack.pop()
        while(tempStack.isEmpty() == False and tempStack.top() < temp):
            stack.push(tempStack.top())
            tempStack.pop()
        tempStack.push(temp)
    return tempStack
    
def prints(stack): 
    for i in range(0,len(stack)): 
        print(stack[i], end = ' ') 
    

if __name__ == '__main__':
    stack = Stack()
    stack.push(34)
    stack.push(3)
    stack.push(31)
    stack.push(98)
    stack.push(92)
    stack.push(23)
    print("Stack numbers are:") 
    prints(stack.array)
    print("\nSorted numbers are: ") 
    sortedst = sortStack(stack) 
    prints(sortedst.array) 


    
    