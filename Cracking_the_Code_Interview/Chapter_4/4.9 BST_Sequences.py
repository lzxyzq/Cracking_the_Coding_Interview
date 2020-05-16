# A binary search tree was created by travering through an array from left to right and inserting each element.Given a binary search tree with distinct elements,print all possible arrays that could have led to this tree.

import math 
def getPermutation(n, k):
    """
    :type n: int
    :type k: int
    :rtype: str
    """
    res = ''
    nums = [i for i in range(1,n+1)]
    for i in range(n-1,0,-1):
        base = math.factorial(i)
        current = 0
        while k > base:
            k -= base
            current += 1
        res += str(nums[current])
        nums.pop(current)
    res += str(nums[0])
    return res
            

if __name__ == '__main__':
    print(getPermutation(3,3))
