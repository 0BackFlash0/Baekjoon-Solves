import sys
input = sys.stdin.readline

def N_queen(n):
    
    board = [0] * n
    result_list = [0 for _ in range((n-1)//2+1)]
    idx = 0

    def recursive_queen(level):
        if(level==n):
            result_list[idx] += 1
            return


        for row in range(n):
            board[level] = row
            is_available = True

            for lv in range(level):
                if(board[level] == board[lv] or abs(board[level] - board[lv]) == level - lv):
                    is_available = False
                    break
            
            if(is_available):
                recursive_queen(level+1)
    
    # 절반만 계산한 뒤, 나머지는 곱해서 계산
    #체스판의 절반만큼 순회
    for x in range((n-1)//2+1):
        idx = x
        board[0] = x
        recursive_queen(1)

    if(n%2==0):
        return sum(result_list) * 2
    else:
        return sum(result_list[:-1]) * 2 + result_list[-1]



n = int(input())
print(N_queen(n))
        


