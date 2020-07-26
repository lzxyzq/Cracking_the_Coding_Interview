'''
@Author: your name
@Date: 2020-06-10 11:19:32
@LastEditTime: 2020-06-10 12:12:02
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/String/71.Simplify_Path.py
'''
# Given an absolute path for a file (Unix-style), simplify it. Or in other words, convert it to the canonical path.

# In a UNIX-style file system, a period . refers to the current directory. Furthermore, a double period .. moves the directory up a level.

# Note that the returned canonical path must always begin with a slash /, and there must be only a single slash / between two directory names. The last directory name (if it exists) must not end with a trailing /. Also, the canonical path must be the shortest string representing the absolute path.

''' 
Example 1:

Input: "/home/"
Output: "/home"
Explanation: Note that there is no trailing slash after the last directory name.
Example 2:

Input: "/../"
Output: "/"
Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.
Example 3:

Input: "/home//foo/"
Output: "/home/foo"
Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.
Example 4:

Input: "/a/./b/../../c/"
Output: "/c"
Example 5:

Input: "/a/../../b/../c//.//"
Output: "/c"
Example 6:

Input: "/a//b////c/d//././/.."
Output: "/a/b/c" 
'''

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(set(s)) == len(set(t)):
            m = {}
            for i in range(len(s)):
                if s[i] not in m:
                    m[s[i]] = t[i]
                else:
                    if t[i] != m[s[i]]:
                        return False
            return True
        return False
