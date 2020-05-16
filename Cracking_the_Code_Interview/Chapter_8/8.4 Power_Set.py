# Write a method to return all subsets of a set.


#Solution using recursion
def subsets(nums):
    output = [[]]
    for num in nums:
        output += [curr + [num] for curr in output]
    return output


# Combinatorics Solution
def getSubsets2(aset):
    allSubsets = []
    max = 1 << len(aset)
    for k in range(max):
        subset = convertIntToSet(k, aset)
        allSubsets.append(subset)
    return allSubsets

def convertIntToSet(x, aset):
    subset = []
    index = 0
    k = x
    while k > 0:
        if k & 1 == 1 and aset[index] not in subset:
            subset.append(aset[index])
        index += 1
        k >>= 1
    return subset

if __name__ == '__main__':
    nums = [1,2,3]
    print(subsets(nums))
    print(getSubsets2(nums))