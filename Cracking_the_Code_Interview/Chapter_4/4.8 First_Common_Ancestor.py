# Design an algorithm and write code to find the first common ancestor of two nodes in a binary tree,Avoid Storing additional nodes in a data structure.Note:This is not necessarily a binary search tree.

def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    # find the length of the strings 
        # find the length of the strings 
        m = len(text1) 
        n = len(text2) 
        # declaring the array for storing the dp values 
        L = [[0]*(n+1) for i in range(m+1)] 
        """Following steps build L[m+1][n+1] in bottom up fashion 
        Note: L[i][j] contains length of LCS of X[0..i-1] 
        and Y[0..j-1]"""
        for i in range(m+1): 
            for j in range(n+1): 
                if i == 0 or j == 0 : 
                    L[i][j] = 0
                elif text1[i-1] == text2[j-1]: 
                    L[i][j] = L[i-1][j-1]+1
                else: 
                    L[i][j] = max(L[i-1][j] , L[i][j-1]) 
        # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1] 
        return L[m][n] 
        #end of function lcs 

