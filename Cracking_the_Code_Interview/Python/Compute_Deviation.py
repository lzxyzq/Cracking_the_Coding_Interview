# Write a function that takes in a list of dictionaries with a key and list of integers and returns a dictionary with the standard deviation of each list.Note that this should be done without using the numpy built in functions.
'''
Example:

input = [
    {
        'key': 'list1',
        'values': [4,5,2,3,4,5,2,3],
    },
    {
        'key': 'list2',
        'values': [1,1,34,12,40,3,9,7],
    }
]

output -> {'list1': 1.12, 'list2': 14.19}
'''

def computeDeviation(input): 
    #Output Dictionary 
    result = {}
    for item in input:
        arr = item['values']
        sum = 0

        #Calculate sum
        for num in arr:
            sum +=num

        #Calculate mean
        mean = sum/len(arr)

        #Calculate std
        var = 0
        for num in arr:
            var += (num-mean)**2
        std = (var/len(arr))**0.5

        #append the result
        result[item['key']] = std

    return(result)