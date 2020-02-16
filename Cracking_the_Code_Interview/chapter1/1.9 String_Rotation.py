# Assume you have a method is Substring which check if one word is substring of another. Given two strings,s1 and s2, write code to check if s2 is a roration of s1 using only one call to isSubtring(e.g."waterbottle" is a rotation of "erbottlewat").

def is_substring(string, sub):
    return string.find(sub) != -1


def string_rotation(s1, s2):
    if len(s1) == len(s2) != 0:
        return is_substring(s1 + s1, s2)
    return False


# Driver Code 
if __name__ == '__main__': 
    input_str_1 = "erbottlewat"
    input_str_2 = "waterbottle"
    s1 = is_substring(input_str_1,input_str_2)
    s2 = string_rotation(input_str_2,input_str_1)
    print("string_compress:",s1)
    print("string_compress:",s2)