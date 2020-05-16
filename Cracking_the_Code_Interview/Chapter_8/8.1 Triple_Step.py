# A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time.Implement a method to count how many possible ways the child can run up the stairs.

def Triple_Step(n):
    if(n<0):
        return 0
    if(n==0):
        return 1
    else:
        return Triple_Step(n-1) + Triple_Step(n-2) + Triple_Step(n-3)

# Memoization Solution
def Triple_Step_1(n):
    memo = {}
    if(n<0):
        return 0
    if(n==0):
        return 1
    else:
        memo[n] = Triple_Step(n-1) + Triple_Step(n-2) + Triple_Step(n-3)
    return memo[n]

if __name__ == '__main__':
    print(Triple_Step_1(4))
    