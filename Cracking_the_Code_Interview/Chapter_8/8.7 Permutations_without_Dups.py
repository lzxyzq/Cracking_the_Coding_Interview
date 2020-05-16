# Write a method to compute all permutations of a string of unique characters.
#46 Permutations

class Solution:
    def permute(self, nums):
        if len(nums) == 1:
            return [nums]
        result = []
        for i in range(len(nums)):
            others = nums[:i] + nums[i+1:]
            other_permutations = self.permute(others)
            for permutation in other_permutations:
                result.append([nums[i]] + permutation)
        return result

if __name__ == '__main__':
    print(Solution().permute(nums=[1,2,3]))