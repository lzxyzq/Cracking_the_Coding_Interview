# Given an encoded string, return its decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

# You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

# Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

''' 
Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
Example 4:

Input: s = "abc3[cd]xyz"
Output: "abccdcdcdxyz" 
'''

def decodeString(s: str):
    num = 0
    string = ''
    stack = []
    for c in s:
        if c.isdigit():
            num = num*10 + int(c)
        elif c == "[":
            stack.append(string)
            stack.append(num)
            string = ''
            num = 0
        elif c.isalpha():
            string += c
        elif c == ']':
            pre_num = stack.pop()
            pre_string = stack.pop()
            string = pre_string + pre_num * string
    return string

if __name__ == '__main__':
    print(decodeString(s = "2[abc]3[cd]ef"))
    