# BFS 예시
# 미로 탈출
# N * M 크기의 미로에서 (1, 1) --> (N, M) 위치로 탈출
# 한 칸씩 이동 가능하며, 괴물이 없는 부분(1) 으로만 가야함

# BFS : 시작 지점에서 가까운 노드부터 탐색
# 모든 노드의 값을 거리 정보로 넣으면 됨
# 본 문제는 단순히 가장 오른쪽 아래로 가는 것이기 때문에 값이 변경될 여지 X

from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input()))) # 그래프 입력 주의..!

# 이동할 방향 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        print('(x, y) : ', x, y)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            print('\t', '(nx, ny)', nx, ny)
            # 맵 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 괴물인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른쪽 아래의 최단 거리 반환
    return graph[n-1][m-1]

print(bfs(0, 0))





'''
입력 예시)
5 6
101010
111111
000001
111111
111111
출력 예시)
10
'''

