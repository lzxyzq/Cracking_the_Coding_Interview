# Given two strings, write a method to decide if one is a permutation of the other.

# Method 1 (Use Sorting)

def arePermutation(str1, str2):
    n1 = len(str1)
    n2 = len(str2)

    if (n1 != n2):
        return False
# Sort both strings
    a = sorted(str1)
    b = sorted(str2)

# Compare sorted strings 
    for i in range(0, n1): 
        if (a[i] != b[i]): 
            return False
    return True

#  -------------------------------------------------------------------------
# Method 2 (Count characters)
# It is assumed that the characters are stored using 8 bit and there can be 256 possible characters.
# 1) Create count arrays of size 256 for both strings. Initialize all values in count arrays as 0.
# 2) Iterate through every character of both strings and increment the count of character in the corresponding count arrays.
# 3) Compare count arrays. If both count arrays are same, then return true.

NO_OF_CHARS = 256
def arePermutation2(str1, str2): 
    count1 = [0] * NO_OF_CHARS 
    count2 = [0] * NO_OF_CHARS 

    for i in str1:
        count1[ord(i)]+=1

    for i in str2:
        count2[ord(i)]+=1
    
    if len(str1) != len(str2) :
        return False

    for i in range(NO_OF_CHARS):
        if count1[i] != count2[i]:
            return False
    return True

#------------------------------------------------------------------------------------------------

# Driver Code 
if __name__ == '__main__': 
    str1 = "test"
    str2 = "tes"
    if (arePermutation(str1, str2)): 
        print("Yes") 
    else: 
        print("No")
