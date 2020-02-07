# Given a string, write a function to check if it is a permutation of a palindrome.A palindrome is a word or phrase that is the same forwards and backwards.A permutation is a rearrangement of letters.The palindrome does not need to be limited to just dictionary words.

# EXAMPLE
# Input:  Tact Coa
# Output:  True(permutation "taco cat","atco cta",etc.)

# Soving : If a string with an even length is a palindrome, every character in the string must always occur an even number of times. If the string with an odd length is a palindrome,every character except one of the characters must always occur an even number of times. Thus, in case of a palindrome, the number of characters with odd number of occurences can't exceed 1(1 in case of odd length and 0 in case of even length).

# Method 1

def is_palindrome(s):
    odd_counter = 0
    for letter in s.lower():
        if letter.isalpha():
            if s.lower().count(letter) % 2 != 0:
                odd_counter += 1
    return odd_counter < 2


# Method 2
def is_permutation_palindrome(s):
    counts = {}
for c in s.lower():
    if c.isalpha():
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1

    odd_counts = [count for count in counts.values() if count % 2 == 1]
    print(odd_counts)
    return len(odd_counts) < 2

# Driver Code 
if __name__ == '__main__': 
    s = "Tact Coa"
    s1 = is_palindrome(s)
    s2 = is_permutation_palindrome(s)
    print("Method1:",s1)
    print("Method2:",s2)