# import sys
# input = sys.stdin.buffer.readline


def mergeSort(sort_list):
    
    def divide(start, end):
        if(end-start<2):
            return
        
        mid = (start+end)//2

        divide(start, mid)
        divide(mid, end)

        merge(start, mid, end)
    
    
    def merge (start, mid, end):
        temp_list = []
        i = start
        j = mid

        while(i<mid and j<end):
            if(sort_list[i]<sort_list[j]):
                temp_list.append(sort_list[i])
                i += 1
            else:
                temp_list.append(sort_list[j])
                j += 1

        while (i<mid):
            temp_list.append(sort_list[i])
            i += 1
        while (j<end):
            temp_list.append(sort_list[j])
            j += 1

        for k in range(0, len(temp_list)):
            sort_list[start+k] = temp_list[k]
            
            
    return divide(0, len(sort_list))


def statistics(sorted_list):
    # 순회를 하지 않고 구할 수 있는 중앙값, 범위
    median = sorted_list[len(sorted_list)//2]
    radius = sorted_list[-1] - sorted_list[0]

    # 빈도를 계산하기 위해 첫번째 항목은 외부에서 계산
    first_obj = sorted_list[0]

    avg = first_obj
    mode_list = [first_obj]
    max_frequency = 0
    frequency = 1
    pre_elem = first_obj

    for e in sorted_list[1:]:
        avg += e

        if(pre_elem==e):
            frequency += 1
        else:
            if(frequency>max_frequency):
                mode_list = [pre_elem]
                max_frequency=frequency
            elif(frequency==max_frequency):
                mode_list.append(pre_elem)
            frequency = 1
            pre_elem = e

    
    if(frequency>max_frequency):
        mode_list = [pre_elem]
        max_frequency=frequency
    elif(frequency==max_frequency):
        mode_list.append(pre_elem)
    
    avg = round(avg/len(sorted_list))
    mode = mode_list[0] if len(mode_list)==1 else mode_list[1]

    return avg, median, mode, radius


import sys

n = int(sys.stdin.readline())

num_list = []
for _ in range(n):
    num_list.append(int(sys.stdin.readline()))

mergeSort(num_list)

print(*statistics(num_list), sep="\n")
# 산술 평균
# 중앙값
# 최빈값
# 범위

# 정렬 -> 범위, 중앙값 해결
