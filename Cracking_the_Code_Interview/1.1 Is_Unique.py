# Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structure?


# Approach 1 – Brute Force technique
def uniqueCharacters(str):
    for i in range(len(str)):
        for j in range(i + 1,len(str)):
            if(str[i]==str[j]):
                return False
    return True

#Driver Code
str = "asdfgety"
if(uniqueCharacters(str)):
    print("The String ", str," has all unique characters")
else:
    print("The String ", str," has duplicate characters")

# Time Complexity: O(n2)

#--------------------------------------------------------------------------------------
# Approach 2  -Use of Extra Data Structure: This approach assumes ASCII char set. The idea is to maintain a boolean array for the characters. The 128 indices represent 128 characters. All the array elements are initially set to false. As we iterate over the string, set true at the index equal to the int value of the character. If at any time, we encounter that the array value is already true, it means the character with that int value is repeated.

def uniqueCharacters2(str):
    # Assuming character set is ASCII (128 characters)
    if len(str) > 128:
        return False

    char_set = [False for _ in range(128)]
    # char_set = [False] * 128
    # The _ represents a throwaway value (a value which is created by the range()        function, but that the program does not need to do anything with. 
    for char in str:
        val = ord(char)
        # Inbuilt ord() function in Python return an integer representing the Unicode code point of the character
        if char_set[val]:
            # Char already found in string
            return False
        char_set[val] = True

    return True

#Driver Code
str = "asdfgety"
print(uniqueCharacters2(str))

# Time Complexity: O(n)

#--------------------------------------------------------------------------------------
# Approach 3 Hashtable and Array

def uniqueCharacters3(str):
    char_seen = []
    for char in str:
        if char in char_seen:
            return False
    char_seen.append(char)
    return True

#Driver Code
str = "asdfgety"
print(uniqueCharacters3(str))

# Time Complexity: O(n)

#--------------------------------------------------------------------------------------
# Approach 4 Using Set()

def uniqueCharacters4(str):
    if len(str) == len(set(str)):
        return True 
    return False

#Driver Code
str = "asdfgkty"
print(uniqueCharacters4(str))

#--------------------------------------------------------------------------------------
#Approach 5 – Without Extra Data Structure

def uniqueCharacters5(str):
    checker = 0
    for char in str:
        val = ord(char)- ord('a')
        if (checker & (1 << val)) > 0:
            return False
        checker |= (1 << val)
    return True

str = "asdfgty"
print(uniqueCharacters5(str))