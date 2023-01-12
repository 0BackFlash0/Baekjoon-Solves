import sys
input = sys.stdin.readline

class Node:
    def __init__(self):

        self.parent = None

    def setParent(self, parent):
        self.parent = parent
    
    def getRoot(self, compress=True):
        if(self.parent==None):
            return self
        
        result = self.parent.getRoot()
        if(compress):
            self.setParent(result)

        return result



n, m = map(int, input().split())

nodes = [Node() for i in range(n+1)]

for _ in range(m):
    oper, a, b = map(int, input().split())

    a_root = nodes[a].getRoot()
    b_root = nodes[b].getRoot()
    is_union = b_root == a_root
    if(oper==0):
        if(not is_union): 
            b_root.setParent(a_root)
    else:
        print("YES" if is_union else "NO")
    