import sys
input = sys.stdin.readline

def gcd(_a, _b):

    a = _a
    b = _b

    if(b>a):
        b = _a
        a = _b

    if(a%b==0):
        return b
    else:
        return gcd(b, a%b)

def get_div(n):
    divisors = []
    divisors_back = []

    for i in range(1, int(n**(1/2))+1):
        if(n%i == 0):
            divisors.append(i)
            if(i!=n//i):
                divisors_back.append(n//i)

    return divisors + divisors_back[::-1]


n = int(input())

# 초기 2개값에 대해 계산
nums = []
nums.append(int(input()))
nums.append(int(input()))
available_gcd = abs(nums[-2]-nums[-1])

for _ in range(n-2):
    nums.append(int(input()))
    available_gcd = gcd(available_gcd, abs(nums[-2]-nums[-1]))
    # print(available_gcd, abs(nums[-2]-nums[-1]))
        

divs = get_div(available_gcd)

print(" ".join(map(str, divs[1:])))

