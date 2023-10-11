import sys
input = sys.stdin.readline

def nge(num_list):

    length = len(num_list)
    results = [0] * length
    stack = []
    #stack에 저장 : (i, val)

    for i in range(length):
        
        n = num_list[i]
        
        while(len(stack)!=0 and stack[-1][1]<n):
            idx, v = stack.pop()
            results[idx] = n
        
        stack.append((i, n))

    while(len(stack)>0):
        idx, v = stack.pop()
        results[idx] = -1

    return results

        

n = int(input())
num_list = list(map(int, input().split()))

results = nge(num_list)

print(" ".join(map(str, results)))

