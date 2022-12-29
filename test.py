def step_num(n):
    num_list = [0]*n
    num_list[0] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    
    for i in range(1, n):
        temp_num_list = [0]*10

        for j in range(0, 10):
            if (j>0):
                temp_num_list[j] += num_list[i-1][j-1]
            if (j<9):
                temp_num_list[j] += num_list[i-1][j+1]
            temp_num_list[j] %= 1000000000
        num_list[i] = temp_num_list

    return sum(num_list[n-1])%1000000000



n = int(input())
print(step_num(n))