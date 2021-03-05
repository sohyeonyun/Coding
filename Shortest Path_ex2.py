# 최단 경로 문제
# EX2) 전보

'''
    N개의 도시는 통로가 연결된 다른 나라 도시에게 메시지를 보낼 수 있다.
    통로는 단방향이다.
    (도시 C -> 다른 도시들) 로 보낼 때, 메시지를 받을 수 있는 도시 수와 걸리는 시간은?

    --> 다익스트라
'''
'''
    입력 예시)
    3 2 1       도시 수 N, 통로 수 M, 메세지 보내는 도시 번호 C   ( 1 <= N <= 30,000  1 <= M <= 200,000  1 <= C <= N  )
    1 2 4       통로 정보 : (X -> Y)의 비용 Z                  ( 1 <= X, Y <= N    1 <= Z <= 1,000 )
    1 3 2
    출력 예시)
    2 4         보낸 메시지를 받는 도시 수, 총 시간         
'''

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m, c = map(int, input().split())

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m) :
    x, y, z = map(int, input().split())
    graph[x].append((y, z)) # (x -> y) 비용 z

def dijkstra(start) :
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q :
        dist, now = heapq.heappop(q)
        if distance[now] < dist :
            continue
        for i in graph[now] :   # 그래프 꺼!! (노드, 비용)
            cost = dist + i[1]  # 현재 노드까지의 비용 + 다음 노드까지의 비용
            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0])) # 힙 !! (비용, 노드)

dijkstra(c)

count = 0           # 도달 가능한 노드 수
max_distance = 0    # 가장 비용이 큰 노드
for d in distance :
    if d != INF :
        count += 1
        max_distance = max(max_distance, d)
print(count - 1, max_distance)  # 시작 노드 제외 -1
