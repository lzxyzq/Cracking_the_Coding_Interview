# Describe how you could use a single array to implement three stacks.  
class ThreeStacks:
    def __init__(self,size):
        self.array = [None, None, None]
        self.current = [0, 1, 2]
    def push(self, item, stack_number):
        if not stack_number in [0, 1, 2]:
            raise Exception("Bad stack number")
        while len(self.array) <= self.current[stack_number]:
            self.array += [None] * len(self.array)
        self.array[self.current[stack_number]] = item
        self.current[stack_number] += 3
    def pop(self,stack_num):
        if not stack_num in [0,1,2]:
            raise Exception("Bad stack number")
        if self.current[stack_num] > 3:
            self.current[stack_num] -= 3
        item = self.array[self.current[stack_num]]
        self.array[self.current[stack_num]] = None
        return item


if __name__ == '__main__':
    three_stacks = ThreeStacks(3)
    three_stacks.push(101,0)
    three_stacks.push(102,0)
    three_stacks.push(103,0)
    three_stacks.push(104,0)
    three_stacks.push(201,1)
    three_stacks.push(301,2)
    print(three_stacks.pop(0))
    print(three_stacks.pop(0))
