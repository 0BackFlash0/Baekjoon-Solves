import sys
from heapq import heappush, heappop

input = sys.stdin.readline

class depq:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

        self.removed_max = []
        self.removed_min = []

    def insert(self, x):
        heappush(self.max_heap, -x)
        heappush(self.min_heap, x)

    def get_min(self):
        if(len(self.min_heap)>0):
            while(len(self.removed_min)>0 and self.removed_min[0]==self.min_heap[0]):
                heappop(self.min_heap)
                heappop(self.removed_min)
            if(len(self.min_heap)>0):
                return self.min_heap[0]
        return False

    def get_max(self):
        if(len(self.max_heap)>0):
            while(len(self.removed_max)>0 and self.removed_max[0]==self.max_heap[0]):
                heappop(self.max_heap)
                heappop(self.removed_max)
            if(len(self.max_heap)>0):
                return self.max_heap[0]
        return False

    def remove_min(self):
        if(self.get_min()):
            heappush(self.removed_max, -heappop(self.min_heap))

    def remove_max(self):
        if(self.get_max()):
            heappush(self.removed_min, -heappop(self.max_heap))

    def print_result(self):
        if(self.get_min()):
            return f"{-self.get_max()} {self.get_min()}"
        return "EMPTY"


for _ in range(int(input())):

    double_ended_pq = depq()
    for _ in range(int(input())):
        func, num = map(str, input().split())
        num = int(num)

        if(func=="I"):
            double_ended_pq.insert(num)
        else:
            if(num==1):
                double_ended_pq.remove_max()
            else:
                double_ended_pq.remove_min()

    print(double_ended_pq.print_result())

    

