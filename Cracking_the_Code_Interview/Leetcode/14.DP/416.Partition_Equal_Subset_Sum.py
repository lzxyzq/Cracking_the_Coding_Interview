def canPartition(nums) :
    def dfs(nums, target, cache):
        if target < 0: 
            return False
        if target == 0: return True
        if target in cache: return False
        cache.add(target)
        for i, n in enumerate(nums):
            if dfs(nums[i+1:], target-n, cache): 
                return True
        return False

    s = sum(nums)
    if s % 2 != 0: 
        return False
    return dfs(nums, s//2, set())

if __name__ == '__main__':
    canPartition([1,1,100])
    

