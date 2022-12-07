import math
# import sys
# input = sys.stdin.buffer.readline

##평균 길이 구하기.

##모자란 길이 구하기.

def div_lan(lan_list, n, k):
    lan_list.sort(reverse=True)

    start_divisor = math.ceil(k/n)
    #현재까지 가능한 pivot값들 중 가장 큰 값
    start_pivot = lan_list[0]//math.ceil(k/n)
    max_pivot = 0
    for lan in lan_list:
        #start_divisor에서부터 k+1까지 반복한다.
        if(lan//start_pivot==0):
            break
        for div in range(lan//start_pivot, k+1):
            pivot = lan//div
            total_lan = sum(map(lambda s : s//pivot, lan_list))
            if(total_lan==k):
                return pivot
            elif(total_lan>k):
                if(max_pivot<pivot):
                    max_pivot = pivot
                    start_pivot = max_pivot
                break
    return max_pivot
    
    

n, k = map(int, input().split())
lan_list = [int(input()) for _ in range(n)]

print(div_lan(lan_list, n, k))
