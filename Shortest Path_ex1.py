# 최단 경로 문제
# EX1) 미래 도시
'''
    ( 1번 회사 -> K번 회사 -> X번 회사 ) 사이로 이동하는 최소 시간은?
    각 회사간 이동 시간은 1이고, 각 도로는 양방향이다.

    모든 노드에 대한 최단 거리 --> 플로이드 워셜 !!
    * N 범위가 100 이하이므로 OK
'''

import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 대각선 0
for a in range(n + 1) :
    for b in range(n + 1) :
        if a == b :
            graph[a][b] = 0

# 그래프 입력 받기
for _ in range(m) :
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 거쳐갈 노드 K, 최종 목적지 X 입력 받기
x, k = map(int, input().split())

# 플로이드 워셜 수행
for k in range(1, n + 1) :
    for a in range(1, n + 1) :
        for b in range(1, n + 1) :
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 1 -> K -> X 최소 거리 합
result = graph[1][k] + graph[k][x]

if result >= INF :
    print(-1)
else :
    print(result)


'''
    입력 예시1)
    5 7         1 <= N, M <= 100    전체 회사 수, 경로 수
    1 2         연결된 두 회사 번호
    1 3
    1 4
    2 4
    3 4
    3 5
    4 5
    4 5         X, K
    출력 예시1)
    3           최소 시간 출력
    입력 예시2)
    4 2
    1 3
    2 4
    3 4
    출력 예시2)
    -1          X번 회사에 도달할 수 없을 시
'''

