# Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

# If possible, output any possible result.  If not possible, return the empty string.

''' 
Example 1:

Input: S = "aab"
Output: "aba"
Example 2:

Input: S = "aaab"
Output: "" 
'''

class Solution:
    def reorganizeString(self, S: str) -> str:
        count = Counter(S)
        
        pq = [(-v, k) for k,v in sorted(count.items(), key=lambda item: -item[1])]
        heapq.heapify(pq)
        
        if any(-cnt > (len(S)+1)//2 for cnt,_ in pq):
            return ''
        
        res = ''
        
        while len(pq)>=2:
            cnt1, ch1 = heapq.heappop(pq)
            cnt2, ch2 = heapq.heappop(pq)
            
            res+=ch1
            res+=ch2
            if cnt1+1:
                heapq.heappush(pq, (cnt1+1, ch1))
            if cnt2+1:
                heapq.heappush(pq, (cnt2+1, ch2))
            
        return res+pq[0][1] if pq else res
    

# 这道题给了一个字符串，让我们重构这个字符串，使得相同的字符不会相邻，如果无法做到，就返回空串，题目中的例子很好的说明了这一点。如果先不考虑代码实现，让你来手动重构的话，该怎么做呢？其实就是把相同的字符分开。比如例子1中，两个a相邻了，所以把第二个a和后面的b交换位置，这样分开了相同的字符，就是最终答案了。再来看一个例子，比如 "aaabbc"，当发现第二个字符也是 ‘a’ 的时候，就需要往后遍历找到第一个不是 ‘a’ 的字符，即 ‘b’，然后交换 ‘a’ 和 ‘b’ 即可，然后继续往后面进行同样的处理，当无法找到不同的字符后就返回空串。这种方法对有序的字符串S是可以的，虽然题目给的两个例子中字符串S都是有序的，实际上不一定是有序的。所以博主最先的想法是给数组排序呗，但是博主的这个解法跪在了这个例子上 "vvvlo"，我们发现排序后就变成 "lovvv"，这样上面提到的解法就跪了。其实这里次数出现多的字符串需要在前面，这样才好交换嘛。那么还是要统计每个字符串出现的次数啊，这里使用 HashMap 来建立字母和其出现次数之间的映射。由于希望次数多的字符排前面，可以使用一个最大堆，C++ 中就是优先队列 Priority Queue，将次数当做排序的 key，把次数和其对应的字母组成一个 pair，放进最大堆中自动排序。这里其实有个剪枝的 trick，如果某个字母出现的频率大于总长度的一半了，那么必然会有两个相邻的字母出现。这里博主就不证明了，感觉有点像抽屉原理。所以在将映射对加入优先队列时，先判断下次数，超过总长度一半了的话直接返回空串就行了。

# 好，最大堆建立好以后，此时难道还是应该使用上面所说的交换的方法吗？其实直接构建新的字符串要更加简单一些。接下来，每次从优先队列中取队首的两个映射对儿处理，因为要拆开相同的字母，这两个映射对儿肯定是不同的字母，可以将其放在一起，之后需要将两个映射对儿中的次数自减1，如果还有多余的字母，即减1后的次数仍大于0的话，将其再放回最大堆。由于是两个两个取的，所以最后 while 循环退出后，有可能优先队列中还剩下了一个映射对儿，此时将其加入结果 res 即可。而且这个多余的映射对儿一定只有一个字母了，因为提前判断过各个字母的出现次数是否小于等于总长度的一半，按这种机制来取字母，不可能会剩下多余一个的相同的字母