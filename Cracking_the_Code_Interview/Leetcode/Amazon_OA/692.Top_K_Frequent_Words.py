'''
@Author: your name
@Date: 2020-06-09 15:40:41
@LastEditTime: 2020-07-12 20:55:59
@LastEditors: your name
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/Amazon_OA/692.Top_K_Frequent_Words.py
'''
# Given a non-empty list of words, return the k most frequent elements.
# Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

''' Example 1:
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:
Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.
 '''
# Note:
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Input words contain only lowercase letters.
# Follow up:
# Try to solve it in O(n log k) time and O(n) extra space.



class Solution(object):
    def topKFrequent(self, words, k):
        count = collections.Counter(words)
        return [v[0] for v in sorted(count.items(),key = lambda item:(-item[1],item[0]))[:k]]

# Complexity Analysis

# Time Complexity: O(NlogN), where N is the length of words. We count the frequency of each word in O(N) time, then we sort the given words in O(NlogN) time.

# Space Complexity: O(N), the space used to store our candidates.

# --------------------------------------------------------------------------------------------

class Solution(object):
    def topKFrequent(self, words, k):
        count = collections.Counter(words)
        heap = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]

# Complexity Analysis

# Time Complexity: O(Nlogk), where N is the length of words. We count the frequency of each word in O(N) time, then we add N words to the heap, each in (logk) time. Finally, we pop from the heap up to kk times. As k≤N, this is O(Nlogk) in total.
# In Python, we improve this to O(N+klogN): our heapq.heapify operation and counting operations are O(N), and each of k heapq.heappop operations are O(logN).

# Space Complexity: O(N), the space used to store our count.