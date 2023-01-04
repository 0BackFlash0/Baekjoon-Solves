import sys
input = sys.stdin.readline
import math


def find_prime_2n(n):

    is_prime_list = [1 for _ in range(2*n + 1)]
    is_prime_list[0] = 0
    is_prime_list[1] = 0

    for i in range(2, int(math.sqrt(2*n))+1):

        if(is_prime_list[i]==1):

            for not_prime in range(i*i, 2*n+1, i):
                is_prime_list[not_prime] = 0

    return sum(is_prime_list[n+1:2*n+1])


while True:
    n = int(input())
    if(n==0): break
    print(find_prime_2n(n))





