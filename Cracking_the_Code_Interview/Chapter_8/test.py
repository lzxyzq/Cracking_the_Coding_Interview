def combine(n, k):
    output = []
    def backtrack(start, curr = []):
        if len(curr) == k:
            output.append(curr[:])
            return 
        for i in range(start, n+1):
            curr.append(i)
            backtrack(i+1,curr)
            curr.pop()
    backtrack(1, [])
    return output


if __name__ == '__main__':
    print(combine(4,2))