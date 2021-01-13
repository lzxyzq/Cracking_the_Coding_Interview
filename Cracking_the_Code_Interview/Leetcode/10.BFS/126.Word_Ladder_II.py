
# Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

# Only one letter can be changed at a time
# Each transformed word must exist in the word list. Note that beginWord is not a transformed word.

# Note:

# Return an empty list if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.

from collections import defaultdict
import string
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList):

        level = {beginWord}
        parent = defaultdict(set) #key: word value:parent
        wordList = set(wordList)
        # BFS 分层遍历
        while level and endWord not in parent:
            next_level = defaultdict(set)
            for node in level:
                for char in string.ascii_lowercase:
                    for i in range(len(beginWord)):
                        n = node[:i]+char+node[i+1:]
                        if n in wordList and n not in parent:
                            next_level[n].add(node)
            level = next_level
            parent.update(next_level) # set add 多个用 update
            
        res = [[endWord]]
        while res and res[0][0] != beginWord:
            res = [[p] + r for r in res for p in parent[r[0]]]
        return res
