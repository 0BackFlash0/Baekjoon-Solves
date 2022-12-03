def calc_friend(matrix, r):

    check_col = matrix[r].copy()
    check_col[r] = True

    friend_col = [False for _ in matrix]

    for i, is_friend in enumerate(check_col):
        if(is_friend):
            for j, elem in enumerate(matrix[i]):
                friend_col[j] = friend_col[j] or elem

    return sum(friend_col) - 1


len_n = int(input())

matrix = [[(True if tf == "Y" else False) for c, tf in enumerate(input())] for _ in range(len_n)]

max_friend = 0
for r in range(len_n):
    
    num_friend = calc_friend(matrix, r)
    if(num_friend > max_friend):
        max_friend = num_friend

print(max_friend)

