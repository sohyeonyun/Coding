# BFS
'''
Breadth First Search - 너비 우선 탐색
큐 -> (deque 라이브러리)
탐색 -> O(N)
일반적으로 실제 수행 시간은 DFS보다 좋은 편

1. 탐색 시작 노드를 큐에 삽입하고 방문 처리
2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않는 노드를 모두 큐에 삽입하고 방문 처리
3. 수핼할 수 없을 때까지 2 반복
'''

from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    # 큐가 빌 때까지 반복
    while queue:
        v = queue.popleft()
        print(v, end = ' ')

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 5],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9
bfs(graph, 1, visited)