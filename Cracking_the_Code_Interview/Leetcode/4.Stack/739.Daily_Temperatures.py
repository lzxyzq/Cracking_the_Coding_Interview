# Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

# For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

# Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ans = [0 for _ in range(len(T))] 
        stack = []
        for i in range(len(T) - 1 , -1 , -1):
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            if stack:
                ans[i] = stack[-1] - i
            stack.append(i)
        return ans


def dailyTemperatures(self, T):
    #initialize the result array with all '0's considering when there is no bigger temperature
    ans = [0]*len(T) 
    stack = []
    
    for i,v in enumerate(T):
        #check whether current val is greater than the last appended stack value.  We will pop all the elements which is lesser than the current temp
        while stack and stack[-1][1] < v:
            index,value = stack.pop()
            ans[index] = i - index # we are checking how many indices we have crossed since we last have a lesser temperature
		#Remember since we are comparing all the stack elements before inserting,all the stack elements will have temperatures greater than the current value	
        stack.append([i,v])      
    
    return ans