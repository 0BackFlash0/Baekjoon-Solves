
import sys
input = sys.stdin.readline

class depq_node:
    def __init__(self, value, link=0):
        self.value = value
        self.link_index = link

    def link(self, index):
        self.link_index = index

class depq:
    def __init__(self):
        self.buffer = []

        self.max_heap = [None]
        self.min_heap = [None]
        self.size = 0

        return

    def isempty(self):
        return len(self.buffer) + len(self.max_heap) - 1 == 0


    def insertMax(self, node):
        self.max_heap.append(node)

        idx = self.size
        result = idx

        while idx>1 and self.max_heap[idx//2].value<self.max_heap[idx].value:
            tmp = self.max_heap[idx//2]
            self.max_heap[idx//2] = self.max_heap[idx]
            self.max_heap[idx] = tmp

            self.min_heap[self.max_heap[idx].link_index].link_index = idx

            result = idx

            idx //= 2

        return result


    def insertMin(self, node):
        self.min_heap.append(node)

        idx = self.size
        result = idx

        while idx>1 and self.min_heap[idx//2].value>self.min_heap[idx].value:
            tmp = self.min_heap[idx//2]
            self.min_heap[idx//2] = self.min_heap[idx]
            self.min_heap[idx] = tmp

            self.max_heap[self.min_heap[idx].link_index].link_index = idx

            result = idx

            idx //= 2

        return result


    def insert(self, x):
        if(len(self.buffer)==1):
            large, small = (x, self.buffer[0]) if x > self.buffer[0] else (self.buffer[0], x)
            self.size += 1
            large_idx = self.insertMax(depq_node(large))
            small_idx = self.insertMin(depq_node(small))

            self.max_heap[large_idx].link(small_idx)
            self.min_heap[small_idx].link(large_idx)

            self.buffer.clear()

        else:
            self.buffer.append(x)

        return


    def maxheap_remove(self):
        result = self.max_heap.pop()
        self.max_heap[1] = result
        self.min_heap[self.max_heap[1].link_index].link_index = 1

        idx = 1

        ## max_heap에서 제거
        while idx*2<self.size:
            if(idx*2+1<self.size):
                target_idx = idx*2 if self.max_heap[idx*2].value > self.max_heap[idx*2+1].value else idx*2+1
            else:
                target_idx = idx*2

            if(self.max_heap[target_idx].value>self.max_heap[idx].value):
                tmp = self.max_heap[target_idx]
                self.max_heap[target_idx] = self.max_heap[idx]
                self.max_heap[idx] = tmp

                self.min_heap[self.max_heap[target_idx].link_index].link_index = target_idx
                self.min_heap[self.max_heap[idx].link_index].link_index = idx

                idx = target_idx
            else:
                break
        
        return result

    def minheap_remove(self):
        result = self.min_heap.pop()
        self.min_heap[1] = result
        self.max_heap[self.min_heap[1].link_index].link_index = 1

        idx = 1

        ## max_heap에서 제거
        while idx*2<self.size:
            if(idx*2+1<self.size):
                target_idx = idx*2 if self.min_heap[idx*2].value < self.min_heap[idx*2+1].value else idx*2+1
            else:
                target_idx = idx*2

            if(self.min_heap[target_idx].value<self.min_heap[idx].value):
                tmp = self.min_heap[target_idx]
                self.min_heap[target_idx] = self.min_heap[idx]
                self.min_heap[idx] = tmp

                self.max_heap[self.min_heap[target_idx].link_index].link_index = target_idx
                self.max_heap[self.min_heap[idx].link_index].link_index = idx

                idx = target_idx
            else:
                break
        
        return result

    def removeMax(self):
        if(self.isempty()):
            return

        heap_max = self.max_heap[1] if len(self.max_heap)>1 else None
        buffer = self.buffer[0] if len(self.buffer)>0 else None

        if (heap_max==None or buffer != None and buffer>heap_max.value):
            self.buffer.clear()
            return buffer

        elif (buffer==None or heap_max != None and heap_max.value>buffer):
            
            self.size -= 1

            if(self.size==0):
                self.max_heap.pop()
                self.insert(self.min_heap.pop().value)
                return heap_max.value
            
            self.maxheap_remove()

            min_idx = heap_max.link_index

            while min_idx>1:
                tmp = self.min_heap[min_idx//2]
                self.min_heap[min_idx//2] = self.min_heap[min_idx]
                self.min_heap[min_idx] = tmp

                self.max_heap[self.min_heap[min_idx//2].link_index].link_index = min_idx//2
                self.max_heap[self.min_heap[min_idx].link_index].link_index = min_idx
                
            self.insert(self.minheap_remove().value)
            return heap_max


    def removeMin(self):
        if(self.isempty()):
            return

        heap_min = self.min_heap[1] if len(self.min_heap)>1 else None
        buffer = self.buffer[0] if len(self.buffer)>0 else None


        if (heap_min==None or buffer != None and buffer<heap_min.value):
            self.buffer.clear()
            return buffer

        elif (buffer==None or heap_min != None and heap_min.value<buffer):
            
            self.size -= 1
            
            if(self.size==0):
                self.min_heap.pop()
                self.insert(self.max_heap.pop().value)
                return heap_min.value
            
            self.minheap_remove()

            max_idx = heap_min.link_index

            while max_idx>1:
                tmp = self.max_heap[max_idx//2]
                self.max_heap[max_idx//2] = self.max_heap[max_idx]
                self.max_heap[max_idx] = tmp

                self.min_heap[self.max_heap[max_idx//2].link_index].link_index = max_idx//2
                self.min_heap[self.max_heap[max_idx].link_index].link_index = max_idx
                
            self.insert(self.maxheap_remove().value)
            return heap_min

    def getMinMax(self):
        if(self.isempty()):
            return "EMPTY"
        
        if(self.size==0):
            return f"{self.buffer[0]} {self.buffer[0]}"
        elif(len(self.buffer)==0):
            return f"{self.max_heap[1].value} {self.min_heap[1].value}"
        else:
            buffer_val = self.buffer[0]
            min_val = buffer_val if buffer_val < self.min_heap[1].value else self.min_heap[1].value
            max_val = buffer_val if buffer_val < self.max_heap[1].value else self.max_heap[1].value

            return f"{max_val} {min_val}"
        
for _ in range(int(input())):

    double_ended_pq = depq()
    for _ in range(int(input())):
        func, num = map(str, input().split())
        num = int(num)

        if(func=="I"):
            double_ended_pq.insert(num)
        else:
            if(num==1):
                double_ended_pq.removeMax()
            else:
                double_ended_pq.removeMin()
        
        print(double_ended_pq.buffer)
        print(double_ended_pq.getMinMax())