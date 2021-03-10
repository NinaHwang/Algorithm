import sys

total = int(sys.stdin.readline())
graph = []
for i in range(total):
    data = list(map(str, sys.stdin.readline().split()))
    graph.append(list(map(int, data[0])))
print(graph)

size = 0
lst = []
def dfs(y, x):
    global size
    target = graph[y][x]
    if target == 1:
        size += 1
    elif target == 0:
        if size != 0:
            lst.append(size)
        size = 0
    graph[y][x] = -1

    if y+1 > total and x+1 > total:
        # return lst
        for i in sorted(lst):
            print(i)
    elif y+1 >= total:
        dfs(y, x+1)
    elif x+1 >= total:

        dfs(y+1, x)
    else:
        dfs(y, x+1)
        dfs(y+1, x)

dfs(0,0)

# for i in sorted(lst):
#     print(i)