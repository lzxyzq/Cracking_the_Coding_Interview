# Write a method to replace all spaces in a string with "%20".You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the "true" length of the string.
# Example 
# input   "Mr John Smith  ",  13
# output  "Mr%20John%20Smith"

MAX = 1000; 
def replaceSpaces(string):
    # Remove leading and trailing spaces 
    string = string.strip() 
    i = len(string)
    space_count = string.count(' ')

    new_length = i + space_count * 2
    if new_length > MAX:
        return -1
    
    # Fill string array
    index = new_length - 1
    string = list(string) 

    for f in range(i, new_length): 
        string.append('0') 

    for j in range(i-1,0,-1):
        if string[j] == ' ':
            string[index] = '0'
            string[index-1] = '2'
            string[index-2] = '%'
            index = index -3
        else:
            string[index] = string[j]
            index -= 1
    return ''.join(string)
# Method2

# Driver Code 
if __name__ == '__main__': 
    s = "Mr John Smith "
    s = replaceSpaces(s)
    print(s)