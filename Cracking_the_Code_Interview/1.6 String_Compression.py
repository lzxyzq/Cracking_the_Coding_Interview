# Implement a method to perform basic string compression using the counts of repeated charaters.For example,the string aabcccccaaa would become a2b1c5a3.If the "compressed" string would not become smaller than the original string,your method should return the origin string.You can assume the string has only uppercase and lowercase letters(a-z)

def string_compress(input_str):
    comp_str = ""
    count = 1 
    for i in range(len(input_str)-1):
        if input_str[i] == input_str[i+1]:
            count += 1
        else:
            comp_str += input_str[i] + str(count)
            count = 1
    comp_str += input_str[i] + str(count)

    if len(comp_str) >= len(input_str):
        return input_str
    else:
        return comp_str
    

# Driver Code 
if __name__ == '__main__': 
    input_str_1 = "aabcccccaaa"
    input_str_2 = "aaaaaabbccbcaabb"
    s1 = string_compress(input_str_1)
    s2 = string_compress(input_str_2)
    print("string_compress:",s1)
    print("string_compress:",s2)