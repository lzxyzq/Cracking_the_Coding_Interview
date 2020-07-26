# The same with 51 just return the len(res)

class Solution:
    def totalNQueens(self, n: int) -> int:
        res = []
        self.helper([],[],[],n,res)
        print(res)
        return len(res)
    
    def helper(self,queen_y,sum_x_y,minus_x_y,n,res):
        x=len(queen_y)
        if x == n:
            res.append(queen_y)
            return
        for y in range(n):
            if y not in queen_y and x+y not in sum_x_y and x-y not in minus_x_y:
                self.helper([y]+queen_y,[x+y]+sum_x_y,[x-y]+minus_x_y,n,res)

       