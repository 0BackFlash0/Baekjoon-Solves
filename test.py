import sys
input = sys.stdin.readline


v, e = map(int. input().split())
start = int(input())

class node:

    def __init__(self):
        self.parent = None

    def setParent(self, parent):
        self.parent = parent

    def checkRoot(self):

        if(self.parent == None):
            return self

        root = self.checkRoot(self.parent)
        self.parent = root

        return root

    
