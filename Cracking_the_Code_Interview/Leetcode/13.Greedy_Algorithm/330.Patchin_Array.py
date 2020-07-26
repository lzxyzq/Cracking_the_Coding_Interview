# Given a sorted positive integer array nums and an integer n, add/patch elements to the array such that any number in range [1, n] inclusive can be formed by the sum of some elements in the array. Return the minimum number of patches required.

""" Example 1:
Input: nums = [1,3], n = 6
Output: 1 
Explanation:
Combinations of nums are [1], [3], [1,3], which form possible sums of: 1, 3, 4.
Now if we add/patch 2 to nums, the combinations are: [1], [2], [3], [1,3], [2,3], [1,2,3].
Possible sums are 1, 2, 3, 4, 5, 6, which now covers the range [1, 6].
So we only need 1 patch.
Example 2:

Input: nums = [1,5,10], n = 20
Output: 2
Explanation: The two patches can be [2, 4].
Example 3:

Input: nums = [1,2,2], n = 5
Output: 0 
"""
# 首先可以确定的是，
# nums中必然包含1，如果不包含1，那么[1,n]这个范围中的1就没法实现
# 其次数组中的元素不能重复使用，如果允许重复使用，那么把1重复多次，就可以组成任意整数。
# 令miss为[0,n]中缺少的最小整数，意味着我们可以实现[0,miss)范围内的任意整数。
# 如果数组中有某个整数x<=miss, 那么我们可以把[0,miss)区间的所有整数加上x，区间变成了[x, miss+x)，由于区间[0,miss)和[x, miss+x)重叠，两个区间可以无缝连接起来，意味着我们可以把区间[0,miss)扩展到[0, miss+x)。
# 如果数组中不存在小于或等于miss的元素，则区间[0,miss)和[x, miss+x) 脱节了，连不起来。此时我们需要添加一个数，最大限度的扩展区间[0, miss)。那添加哪个数呢？当然是添加miss本身，这样区间[0,miss)和[miss, miss+miss)恰好可以无缝拼接。
# 举个例子，令nums=[1, 2, 4, 13, 43], n=100，我们需要让[1,100]内的数都能够组合出来。
# 使用数字1,2,4，我们可以组合出[0, 8)内的所有数，但无法组合出8，由于下一个数是13，比8大，根据规则2，我们添加8，把区间从[0,8)扩展到[0,16)。
# 下一个数是13，比16小，根据规则1，我们可以把区间从[0,16)扩展到[0,29)。
# 下一个数是43，比29大，根据规则2，添加29，把区间从[0,29)扩大到[0,58)。
# 由于43比58小，根据规则1，可以把区间从[0,58)扩展到[0,101)，刚好覆盖了[1,100]内的所有数。
# 最终结果是添加2个数，8和29，就可以组合出[1,100]内的所有整数。

# 1. 遇到的第一个无法拼成的数字, 记为 x，一定需要加入数字来解决, 
#    我们可以贪心的加入 x
# 2. 由于前面数字组合以及可以组成 1 到 (x-1) 的数字，当加入 x 后，
#    我们就可以直接跟之前的数字组合成 x 到 2x-1, 所以我们就可以直接
#    从 2x 开始找第一个无法拼成的数字
# 3. 如果 nums 没有用完，如果可以，我们需要跳到 nums 的下一个。这样
#    才能更多的使用 nums




