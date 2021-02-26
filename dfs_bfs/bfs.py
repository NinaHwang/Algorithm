from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [
    [],
    [3,6],
    [6,8,11],
    [1,5],
    [5],
    [3,4,10],
    [1,2,7],
    [6,9],
    [2],
    [7],
    [5],
    [2]
]

visited = [False] * 12

bfs(graph, 1, visited)
