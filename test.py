import sys
input = sys.stdin.readline

def room_assign(time_tables):
    #저장된 정보 : key : 끝나는 시간 / val : 시작 시간 list (dict형태)
    #동적 계획법 - 저장하는 정보 : 1. 끝난 시간 (인덱스) 2. 지금까지 한 회의 수

    best_table = [0] * len(time_tables)

    for time in range(1, len(time_tables)):
        best_table[time] = max(best_table[time-1], best_table[time_tables[time][0]] + time_tables[time][1])
        best_table[time] += time_tables[time][2]

    # print(best_table)
    return best_table[len(time_tables)-1]



def preprocessing(input_times, uniques):
    unique_dict = { val : idx for idx, val in enumerate(uniques)}
    time_tables = [[0, 0, 0] for _ in range(len(uniques))]
    # 0 : 가장 짧은 회의 시작시간
    # 1 : 가장 짧은 회의 시작 시간 존재 여부 (존재 하면 1)
    # 2 : 시간이 0인 회의 개수
    for i, o in input_times:
        key = unique_dict[o]
        val = unique_dict[i]
        if(i==o):
            time_tables[key][2] += 1
        elif(time_tables[key][0] < val):
            time_tables[key][0] = val
            time_tables[key][1] = 1

    return time_tables



n = int(input())
input_times = dict()
for _ in range(n):
    i, o = map(int, input().split())

    if(o not in input_times.keys()):
        input_times[o] = [0, 0]
    
    if(o==i):
        input_times[0][1] += 1
    elif(input_times[o][0]<i):
        input_times[0][0] = i


    

time_tables = preprocessing(input_times)
# print(time_tables)

print(room_assign(time_tables))
