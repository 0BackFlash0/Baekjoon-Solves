# 현재 무게가 n일때의 최대값 저장
# 그거보다 작으면 무효
# 합들보다 이전 값이 더 크면 그것도 무효
# weight-[value] 딕셔너리

def bag_capacity(weight_value_dict, max_weight):
    
    keys = weight_value_dict.keys()
    memorize = [[0, [{key:0 for key in keys}]]]

    for i in range(1, max_weight+1):
        tmp_memorize = memorize[i-1]
        key_list = key.copy()
            if(i-key>=0):
                for memo_dict in memorize[i-key][1]:
                    if(memorize[i-key][1][key]>=len(weight_value_dict[key])):
                        continue
                    value = memorize[i-key][0] + weight_value_dict[key][memorize[i-key][1][key]]
                    if(value>tmp_memorize[0]):
                        tmp_memorize = [value, memorize[i-key][1].copy()]
                        tmp_memorize[1][key] += 1
        print(tmp_memorize)
        memorize.append(tmp_memorize)


    return memorize[max_weight][0]



    
n, max_weight = map(int, input().split())
weight_value_dict = dict()

for i in range(n):
    w, v = map(int, input().split())
    if(w not in weight_value_dict.keys()):
        weight_value_dict[w] = [v]
    else:
        idx = 0
        while(idx<len(weight_value_dict[w]) and v<weight_value_dict[w][idx]):
            idx += 1
        weight_value_dict[w].insert(idx ,v)
        

print(bag_capacity(weight_value_dict, max_weight))