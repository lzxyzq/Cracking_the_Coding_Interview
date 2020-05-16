# A magic index in an array A[0……n-1]is defined to be an index such that A[i] = i .Given a sorted array of distinct integers,write a method to find a magic index,if one exists, in array A.
# Follow up
# What if the valuse are not distinct?
def linearSearch(arr, n): 
    for i in range(n): 
        if arr[i] is i: 
            return i 
    return -1

# ------------------------------------------------
def binarySearch(arr, low, high): 
    if high >= low: 
        mid = (low + high)//2
      
    if mid is arr[mid]: 
        return mid 
      
    if mid > arr[mid]: 
        return binarySearch(arr, (mid + 1), high) 
    else: 
        return binarySearch(arr, low, (mid -1)) 
      
    # Return -1 if there is no Fixed Point 
    return -1

# Follow up
# What if the valuse are not distinct?

def binarySearch_duplicate(arr, low, high): 
    # If No Magic Index return -1  
    if(high<low):
        return -1 
    mid = (low + high)//2
    # Magic Index Found, return it. 
    if mid is arr[mid]: 
        return mid 
    # search left 
    left_index = min(mid-1,arr[mid])
    left = binarySearch_duplicate(arr,low,left_index)
    if (left >=0 ):
        return left
    # search right 
    right_index = max(mid + 1 ,arr[mid])
    right = binarySearch_duplicate(arr,mid+1,high)
    return right 

if __name__ == '__main__':
    arr = [-10, -5, 0, 3, 7]
    print(binarySearch(arr,0,len(arr)-1))
    arr1 = [-10, -5, 2, 2, 2, 3, 4, 7, 9, 12, 13]
    print(binarySearch_duplicate(arr1,0,len(arr)-1)) 