import math
def finalInstances(instances, averageUtil):
    """
    :type instances: int
    :type averageUtil: List[int]
    :rtype: int
    """
    i = 0
    while(i < len(averageUtil)):
        if i < len(averageUtil) and averageUtil[i] < 25 and instances>1:
            instances = math.ceil(instances / 2)
            i = i + 10
        elif i < len(averageUtil) and averageUtil[i] > 60 and instances < 200000000:
            instances = instances*2
            i = i + 10
        i += 1
    return instances 

if __name__ == '__main__':
    instances = 1
    # averageUtil=[25, 23, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 76, 80]
    # averageUtil=[5,10,80]
    averageUtil=[30, 15, 18, 18, 19, 89, 15, 18, 18, 19, 89, 15, 18, 18, 19, 89, 15, 18, 18, 19, 89, 15, 18, 18, 19, 89]
    print(finalInstances(instances,averageUtil))
