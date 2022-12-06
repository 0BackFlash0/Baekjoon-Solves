
from copy import deepcopy

def DFS(_graph_list, start):
    graph_list = deepcopy(_graph_list)

    search_list = [start]
    result = []
    while(len(search_list)>0):
        current = search_list.pop()
        current_node = graph_list[current]
        if(not current_node[0]):
            current_node[0] = True
            result.append(current+1)
            for next_node in sorted(current_node[1], reverse=True):
                if(graph_list[next_node][0]==False):
                    search_list.append(next_node)

    return result

def BFS(_graph_list, start):
    graph_list = deepcopy(_graph_list)
    search_list = [start]
    result = []
    while(len(search_list)>0):
        current = search_list.pop(0)
        current_node = graph_list[current]
        if(not current_node[0]):
            current_node[0] = True
            result.append(current+1)
            for next_node in sorted(current_node[1]):
                if(graph_list[next_node][0]==False):
                    search_list.append(next_node)

    return result


n, m, start = map(int, input().split())

graph_list = [[False, []] for _ in range(n)]
# 현재 값 (인덱스)
# 방문 여부 (True/False)
# 다음 방문 (인덱스들)

for _ in range(m):
    s, e = map(int, input().split())

    graph_list[s-1][1].append(e-1)
    graph_list[e-1][1].append(s-1)
    # 인덱스로 계산하기 때문에 1씩 제외하고 

print(" ".join(map(str, DFS(graph_list, start-1))))
print(" ".join(map(str, BFS(graph_list, start-1))))
