from sys import stdin
from collections import deque  # 큐에서 pop 할때 시간복잡도를 낮춰줌

def bfs(graph, v):
    visit = []
    queue = deque([v])

    while queue:
        node = queue.popleft()  # 맨처음 들어온 값을 뽑아냄, 선입선출로 여기서 넓이 탐색의 특색이 나타남
        if node not in visit:  # 중복으로 큐에 들어온 노드값이 여기서 걸러짐 ex) queue = [4, 4, 4]일때 결국 다 방문한 거라서 다 popleft로 빠져나가고 종료됨
            visit.append(node)
            if node in graph:  # 이 부분 없으면 key error 발생함.
                temp = list(set(graph[node]) - set(visit))  # graph의 value인 리스트가 정렬되지 않은 상태이므로 정렬 후 이미 검토한 내용을 빼줌
                temp.sort()  # set은 순서가 없어서 위에 리스트로 만든걸 다시 정렬 해줘야 함. 참고로 셋은 정렬도 못함 리스트만 가능. 순서대로 큐에 더해져야 넓이 탐색 순서를 제대로 지킬 수 있음
                queue += temp

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
                temp.sort(reverse=True)  # 스택은 뒤에서 마지막에 넣은게 빠지기 때문에 리버스해줘야 순서대로 잘 찾을 수 있음
                stack += temp  # 가장 최근에 탐색한 노드의 인접한 노드가 스택 뒤에 다시 들어가게 됨

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
