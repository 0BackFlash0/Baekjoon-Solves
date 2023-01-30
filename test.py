import sys
input = sys.stdin.readline

def available_set(r, c, sq):

    r_set = groups["row"][r].leak
    c_set = groups["row"][c].leak
    sq_set = groups["row"][sq].leak

    result = r_set.intersection(c_set).intersection(sq_set)

    return result

class sudoku_node:
    
    def __init__(self, value, r, c):
        self.r = r
        self.c = c

class sudoku_group:
    
    def __init__(self):
        self.leak = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        self.empties = []

    def add_empty(self, r, c, sq):
        self.empties.append((r, c, sq))

    def add_available(self, num):
        self.leak.remove(num)


    

# 각 클래스에서 부족한 수 목록
# 노드 - 각 클래스 연결

# 클래스 -> 부족한 요소들 + 노드들
# 노드 -> 클래스

empties = []

groups = {"row" : [], "col" : [], "sq" : []}

for r in range(9):
    for c, num in enumerate(map(int, input().split())):
        sq = 3*(r//3) + c//3
        
        if(num!=0):
            groups["row"][r].add_available(num)
            groups["col"][c].add_available(num)
            groups["sq"][sq].add_available(num)
        else:
            groups["row"][r].add_empty(num)
            groups["col"][c].add_empty(num)
            groups["sq"][sq].add_empty(num)
            empties.append((r, c, sq))


while empties:

    empty = empties.pop()
    empty_set = available_set(**empty)

    if(len(empty_set)==1):
        val = tuple(empty_set)[0]
        groups["row"][empty[0]].add_available(val)
        groups["col"][empty[1]].add_available(val)
        groups["sq"][empty[2]].add_available(val)

    elif(len(empty_set)>2):
        

