
import sys
input = sys.stdin.readline

def partial_sum(n, s, num_list):
    
    num_list = num_list
    num_list.sort(reverse=True)

    sum = 0
    l = 0

    while(l<n):
        sum += num_list[l]
        l += 1

        if(sum>=s):
            return l
    
    return 0


n,s = map(int, input().split())

num_list = list(map(int, input().split()))
print(partial_sum(n, s, num_list))