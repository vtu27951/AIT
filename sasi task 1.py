from collections import deque

graph = {
    0: [1],
    1: [0],
    2: [3],
    3: [2]
}

visited = []


def bfs(start):
    q = deque([start])
    visited.append(start)

    while q:
        v = q.popleft()
        print(v, end=" ")

        for i in graph[v]:
            if i not in visited:
                visited.append(i)
                q.append(i)


print("Connected components:")

for v in graph:
    if v not in visited:
        bfs(v)
        print()
