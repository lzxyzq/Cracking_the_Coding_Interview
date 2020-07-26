'''
@Author: your name
@Date: 2020-06-18 14:26:04
@LastEditTime: 2020-06-18 14:57:55
@LastEditors: your name
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/Stack/150.Evaluate_Reverse_Polish_Notation.py
'''
# Evaluate the value of an arithmetic expression in Reverse Polish Notation.

# Valid operators are +, -, *, /. Each operand may be an integer or another expression.

# Note:
# Division between two integers should truncate toward zero.
# The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.

""" Example 1:

Input: ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: ["4", "13", "5", "/", "+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
Output: 22
Explanation: 
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
"""
class Solution:
    def evalRPN(self, tokens: List[str]) :
        stack = []
        for t in tokens:
            if t not in ["+", "-", "*", "/"]:
                stack.append(int(t))
            else:
                r, l = stack.pop(), stack.pop()
                if t == "+":
                    stack.append(l+r)
                elif t == "-":
                    stack.append(l-r)
                elif t == "*":
                    stack.append(l*r)
                # here take care of the case like "1/-22",
                # in Python 2.x, it returns -1, while in 
                # Leetcode it should return 0
                else:
                    if l*r < 0 and l % r != 0:
                        stack.append(l//r+1)
                    else:
                        stack.append(l//r)
        return stack.pop()
