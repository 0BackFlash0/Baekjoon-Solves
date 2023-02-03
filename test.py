import sys
input = sys.stdin.readline

def available_set(r, c, box):

    r_set = groups["row"][r].leak
    c_set = groups["row"][c].leak
    box_set = groups["row"][box].leak

    result = r_set.intersection(c_set).intersection(box_set)

    return result

class sudoku_node:
    
    def __init__(self, r_group, c_group, box_group):
        self.r = r_group
        self.c = c_group
        self.box = box_group

    def get_available_list(self, target="all"):
        if(target=="row"):
            return self.r.numbers
        elif(target=="col"):
            return self.c.numbers
        elif(target=="box"):
            return self.box.numbers
        elif(target=="all"):
            return [r_bool and c_bool and box_bool for r_bool, c_bool, box_bool in zip(self.r, self.c, self.box)]

class sudoku_group:
    
    def __init__(self):
        self.numbers = [True, True, True, True, True, True, True, True, True]
        self.empties = []

    def add_empty(self, node):
        self.empties.append(node)

    def add_available(self, num):
        self.numbers[num-1] = False


    

# 각 클래스에서 부족한 수 목록
# 노드 - 각 클래스 연결

# 클래스 -> 부족한 요소들 + 노드들
# 노드 -> 클래스

empties = []

groups = {"row" : [], "col" : [], "box" : []}

for r in range(9):
    for c, num in enumerate(map(int, input().split())):
        box = 3*(r//3) + c//3
        
        if(num!=0):
            groups["row"][r].add_available(num)
            groups["col"][c].add_available(num)
            groups["box"][box].add_available(num)
        else:
            groups["row"][r].add_empty(num)
            groups["col"][c].add_empty(num)
            groups["box"][box].add_empty(num)
            empties.append((r, c, box))


while empties:

    empty = empties.pop()
    empty_set = available_set(**empty)

    if(len(empty_set)==1):
        val = tuple(empty_set)[0]
        groups["row"][empty[0]].add_available(val)
        groups["col"][empty[1]].add_available(val)
        groups["box"][empty[2]].add_available(val)

    elif(len(empty_set)>2):
        

