# Implement an algorithm to print all valid combinations of n pairs of parentheses.
# Example 
# Input 3 
# Output ((())) (()()) (())() ()(()) ()()()

def generateParenthesis(N):
    ans = []
    def backtrack(S = '', left = 0, right = 0):
        if len(S) == 2 * N:
            ans.append(S)
            return
        if left < N:
            backtrack(S+'(', left+1, right)
        if right < left:
            backtrack(S+')', left, right+1)

    backtrack()
    return ans

if __name__ == '__main__':
    print(generateParenthesis(3))
    