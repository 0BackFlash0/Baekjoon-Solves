
def remove_neighbor(list_2div, r, c):
    # print(r, c)
    if(0<=r<len(list_2div) and 0<=c<len(list_2div[0])):
        if(list_2div[r][c]==1):
            list_2div[r][c] = 0
            remove_neighbor(list_2div, r-1, c)
            remove_neighbor(list_2div, r+1, c)
            remove_neighbor(list_2div, r, c-1)
            remove_neighbor(list_2div, r, c+1)

def check_area(list_2div):
    for row in list_2div:
        for elem in row:
            pass

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


        
