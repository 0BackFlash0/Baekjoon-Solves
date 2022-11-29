import sys
sys.setrecursionlimit(9999)

def div2or3(num):
    n = num
    i = 0
    while(num%2==0):
        num /= 2
        i += 1
    while(num%3==0):
        num /= 3
        i += 1

    if(num==1):
        return i
    else:
        return 0


def min_calc(num):
    shortcut = div2or3(num)
    if(num==1):
        return 1
    elif(shortcut!=0):
        return shortcut
    
    minus_1 = min_calc(num-1)
    div_2 = min_calc(num//2) if num%2==0 else float("inf")
    div_3 = min_calc(num//3) if num%3==0 else float("inf")

    return min([minus_1, div_2, div_3])+1


num = int(input())
print(min_calc(num))
# for i in range(1, 101):
    # print(min_calc(i))