class Solution:

    def preimageSizeFZF(self, K):
        return self.right_bound(K) - self.left_bound(K) + 1

    def trailingZeroes(self, n):
        cnt = 0
        while n != 0:
            n = n // 5
            cnt += n
        return cnt

# search trailingZeroes(n) == K left bound 
    def left_bound(self,target):
        lo = 0
        hi = 50
        while (lo < hi) :
            mid = lo + (hi - lo) // 2
            if (self.trailingZeroes(mid) < target):
                lo = mid + 1
            elif (self.trailingZeroes(mid) > target):
                hi = mid
            else:
                hi = mid
        return lo


    # 搜索 trailingZeroes(n) == K 的右侧边界 */
    def right_bound(self,target):
        lo = 0 
        hi = 50
        while (lo < hi) :
            mid = lo + (hi - lo) // 2
            if (self.trailingZeroes(mid) < target):
                lo = mid + 1
            elif (self.trailingZeroes(mid) > target):
                hi = mid
            else:
                lo = mid + 1
        return lo - 1
if __name__ == '__main__':
    print(2**63 - 1)
    