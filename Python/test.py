import sys
import math
input = sys.stdin.readline

# 벡터 : (x2 - x1), (y2 - y1)
# 완전 탐색
# nCn/2

def vector_matching(length, x_list, y_list):

    weight_map = [1] * length

    def recursive_matching(remain_length, pos):
        
        if(remain_length>=1):

            min_vector = float("inf")

            for i in range(pos, length - remain_length + 1):
                weight_map[i] = -1

                recursive_result = recursive_matching(remain_length-1, i+1)
                if(recursive_result<min_vector):
                    min_vector = recursive_result
                
                weight_map[i] = 1
            
            return min_vector
        else:
            x_sum = 0
            y_sum = 0

            for i in range(length):
                x_sum += weight_map[i] * x_list[i]
                y_sum += weight_map[i] * y_list[i]

            return math.sqrt(math.pow(x_sum, 2) + math.pow(y_sum, 2))

    return recursive_matching(length, 0) 

test_case = int(input())

for _ in range(test_case):
    length = int(input())
    x_list = [0] * length
    y_list = [0] * length

    for idx in range(length):
        x, y = map(int, input().split())

        x_list[idx] = x
        y_list[idx] = y

    print(vector_matching(length, x_list, y_list))
