
def remove_neighbor(list_2div, r, c):
    # print(r, c)
    list_2div[r][c] = 0
    height = len(list_2div)
    length = len(list_2div[0])

    if(r-1>=0 and list_2div[r-1][c]==1):
        remove_neighbor(list_2div, r-1, c)
    if(r+1<height and list_2div[r+1][c]==1):
        remove_neighbor(list_2div, r+1, c)
    if(c-1>=0 and list_2div[r][c-1]==1):
        remove_neighbor(list_2div, r, c-1)
    if(c+1<length and list_2div[r][c+1]==1):
        remove_neighbor(list_2div, r, c+1)

# def check_area(list_2div, height, length):
#     result = 0
#     for row in range(height):
#         for col in range(length):
#             area = []
#             if(list_2div[row][col]==1):
#                 result += 1
#                 area.append((col, row))

#                 while(len(area)>0):
#                     x, y = area.pop()
#                     if(y>=height or x>=length or y<0 or x<0):
#                         continue

#                     if(list_2div[y][x]==1):
#                         list_2div[y][x] = 0

#                         area.insert(0, (x+1, y))
#                         area.insert(0, (x-1, y))
#                         area.insert(0, (x, y+1))
#                         area.insert(0, (x, y-1))
#     return result


if(__name__=="__main__"):
    test_case = int(input())
    for _ in range(test_case):
        x_len, y_len, num = map(int, input().split())

        farm = [[0 for _ in range(x_len)] for _ in range(y_len)]
        for _ in range(num):
            x, y = map(int, input().split())
            farm[y][x] = 1

        
        result = 0
        for y in range(y_len):
            for x in range(x_len):
                if(farm[y][x]==1):
                    result += 1
                    remove_neighbor(farm, y, x)

        print(result)
        # print(check_area(farm, y_len, x_len))


        
