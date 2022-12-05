def step_map(maze):
    max_r = len(maze)
    max_c = len(maze[0])

    step_matrix = [[0 if maze[r][c] == 1 else -1 for c in range(max_c)] for r in range(max_r)]
    step_matrix[0][0] = 1
    pos = [(0, 0)]

    while(len(pos)>0):
        r, c = pos.pop(0)

        close_pos = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]

        for _r, _c in close_pos:
            if(0<=_r<max_r and 0<=_c<max_c and step_matrix[_r][_c]==0):
                pos.append((_r, _c))
                step_matrix[_r][_c] = step_matrix[r][c] + 1
        
            # print("\n".join(list(map(str, step_matrix))))
            # print()
    
    return step_matrix



row, column = map(int, input().split())
maze = []
for _ in range(row):
    maze.append(list(map(int, input())))

# print("\n".join(list(map(str, maze))))
# print()
# print(step_map(maze))
print(step_map(maze)[row-1][column-1])
