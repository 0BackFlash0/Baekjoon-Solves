import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000)



def sudoku(input_list, r_group, c_group, b_group):

    result_list = []
    input_list = input_list
    r_group = r_group
    c_group = c_group
    b_group = b_group

    def check_availbable():
        if(len(input_list)==0):
            return True

        r, c, b = input_list[-1]

        for i in range(9):

            if(r_group[r][i] and c_group[c][i] and b_group[b][i]):

                r_group[r][i] = False
                c_group[c][i] = False
                b_group[b][i] = False
                input_list.pop()

                if(check_availbable()):
                    result_list.append((r, c, i))
                    return True

                r_group[r][i] = True
                c_group[c][i] = True
                b_group[b][i] = True
                input_list.append((r, c, b))

        return False

    check_availbable()
    return result_list


r_group = [[True for _ in range(9)] for _ in range(9)]
c_group = [[True for _ in range(9)] for _ in range(9)]
b_group = [[True for _ in range(9)] for _ in range(9)]

result_matrix = [[0 for _ in range(9)] for _ in range(9)]
input_list = []

for r in range(9):
    for c, n in enumerate(map(int, input().split())):
        b = 3 * (r//3) + c//3
        
        result_matrix[r][c] = n
        if(n==0):
            input_list.append((r, c, b))
        else:
            r_group[r][n-1] = False
            c_group[c][n-1] = False
            b_group[b][n-1] = False

results = sudoku(input_list, r_group, c_group, b_group)

for result in results:
    r, c, n = result

    result_matrix[r][c] = n+1

for r in result_matrix:
    print(" ".join(map(str, r)))
