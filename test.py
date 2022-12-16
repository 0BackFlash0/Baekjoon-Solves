# 현재 무게가 n일때의 최대값 저장
# 그거보다 작으면 무효
# 합들보다 이전 값이 더 크면 그것도 무효

def bag_capacity(weight_value_list, max_weight):
    
    memorize = [0] * (max_weight+1)

    cur_sum_weight = 0
    cur_sum_value = 0

    for w, v in weight_value_list:
        cur_sum_weight += w
        cur_sum_value += v
        if(cur_sum_weight<max_weight):
            for i in range(cur_sum_weight, w-1, -1):
                memorize[i] = max(memorize[i], memorize[i-w]+v)
            memorize[cur_sum_weight+1:max_weight+1] = [cur_sum_value] * (max_weight-cur_sum_weight)
        else:
            for i in range(max_weight, w-1, -1):
                memorize[i] = max(memorize[i], memorize[i-w]+v)
    
    return memorize[max_weight]


n, max_weight = map(int, input().split())
weight_value_list = []
for i in range(n):
    w, v = map(int, input().split())
    weight_value_list.append((w, v))
        
print(bag_capacity(weight_value_list, max_weight))