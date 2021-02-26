def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

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

dfs(graph,1,visited)
