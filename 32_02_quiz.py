from sys import stdin
from collections import deque  # 큐에서 pop 할때 시간복잡도를 낮춰줌

def bfs(graph, v):
    visit = []
    queue = deque([v])

    while queue:
        # print(queue)
        node = queue.popleft()  # 맨처음 들어온 값을 뽑아냄, 선입선출로 여기서 넓이 탐색의 특색이 나타남
        if node not in visit:  # 중복으로 큐에 들어온 노드값이 여기서 걸러짐 ex) queue = [4, 4, 4]일때 결국 다 방문한 거라서 다 popleft로 빠져나가고 종료됨
            visit.append(node)
            if node in graph:
                for v_node in sorted(list(graph[node])):
                    if v_node not in visit:
                        queue.append(v_node)

    return " ".join(str(i) for i in visit)

def dfs(graph, v):
    visit = []
    stack = [v]

    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            if node in graph:
                temp = list(set(graph[node]) - set(visit))
                temp.sort(reverse=True)
                stack += temp

    return " ".join(str(i) for i in visit)


n, m, v = map(int, stdin.readline().rstrip().split())
connect_list = [stdin.readline().rstrip().split() for _ in range(m)]
graph = {}

for x, y in connect_list:
    x = int(x)
    y = int(y)
    if x not in graph:
        graph[x] = [y]
    elif y not in graph[x]:
        graph[x].append(y)

    if y not in graph:
        graph[y] = [x]
    elif x not in graph[y]:
        graph[y].append(x)
    

print(dfs(graph, v))
print(bfs(graph, v))
