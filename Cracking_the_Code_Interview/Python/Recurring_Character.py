# Given a string, return the first recurring character in it, or None if there is no recurring chracter.

'''
Example:

input = "interviewquery"
output = "i"

input = "interv"
output = None
'''

def rec_char(strings):
    for i, string in enumerate(strings):
        if string in strings[i+1:]:
            return string
    return None

input = "interviewquery"
print(rec_char(input))