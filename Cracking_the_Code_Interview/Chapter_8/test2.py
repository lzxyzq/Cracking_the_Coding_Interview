class Solution:
    def combine(self,n, k):
        output = []
        self.backtracking(1,[],k,n,output)
        return output

    def backtracking(self,start,curr,k,n,output):
        if len(curr) == k:
            output.append(curr)
            return
        for i in range(start,n+1):
            self.backtracking(i+1,curr+[i],k,n,output)
if __name__ == '__main__':
    print(Solution().combine(4,2))
    