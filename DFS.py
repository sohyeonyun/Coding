# DFS
'''
Depth-First Search 깊이 우선 탐색
스택 (-> 재귀)
탐색 수행 -> O(N)

1. 탐색 시작 노드를 스택에 삽입, 방문 처리
2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면, 그 인접 노드를 스택에 넣고 방문 처리
    방문하지 않은 인접 노드가 없으면, 스택에서 최상단 노드를 꺼냄
3. 수행할 수 없을 때까지 2번 반복
'''

def dfs(graph, v, visited):
    # 현재 노드 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 노드 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

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
dfs(graph, 1, visited)
