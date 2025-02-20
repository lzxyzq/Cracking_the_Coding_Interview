# Given an int array nums and an int target, find how many unique pairs in the array such that their sum is equal to target. Return the number of pairs.
''' 
Example 1:

Input: nums = [1, 1, 2, 45, 46, 46], target = 47
Output: 2
Explanation:
1 + 46 = 47
2 + 45 = 47
Example 2:

Input: nums = [1, 1], target = 2
Output: 1
Explanation:
1 + 1 = 2
Example 3:

Input: nums = [1, 5, 1, 5], target = 6
Output: 1
Explanation:
[1, 5] and [5, 1] are considered the same. 
'''

def uniqueTwoSum(nums, target):
    ans = set()
    for n in nums:
        c = target-n
        if c in nums and c >= n:
            ans.add((n, c))
    return len(ans)

if __name__ == '__main__':
    print(uniqueTwoSum([1, 1],2))
    