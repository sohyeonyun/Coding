# 최단 경로 알고리즘
# 1. 다익스트라 최단 경로 알고리즘
'''
    : (특정 노드 -> 다른 노트) 의 최단 경로 구함.
    - 음의 간선 X (실제 GPS에 활용)

    [동작 과정]
    1) 출발 노드 설정
    2) 최단 거리 테이블 초기화
    3) 방문하지 않은 노드 중 최단 거리가 가장 짧은 노드 선택
    4) 해당 노드를 거쳐 다른 노드로 가는 비용 계산 -> 최단 거리 테이블 갱신
    5) 3, 4 반복

    - 한 단계 당, 하나의 노드에 대한 최단 거리를 확실히 찾은 것임.

    [무한 표기]
    inf = int(1e9)
'''

### 방법 1.
### 간단한 다익스트라 알고리즘 - O(V^2)
import sys
input = sys.stdin.readline
INF = int(1e9)  # 무한 : 10억

# 노드의 개수, 간선의 개수 입력 받기
n, m = map(int, input().split())
# 시작 노드 번호 입력 받기
start = int(input())
# 각 노드의 연결 정보를 담는 리스트 생성
graph = [[] for i in range(n + 1)]
# 방문 체크 리스트
visited = [False] * (n + 1)
# 최단 거리 테이블 무한으로 초기화
distance = [INF] * (n + 1)

# 간선 정보 입력 받기
for _ in range(m) :
    a, b, c = map(int, input().split()) # (a 노드 -> b 노드) 의 비용이 c
    graph[a].append((b, c))

# 방문하지 않았던 노드 줌, 가장 최단 거리가 짧은 노드의 번호 반환
def get_smallest_node() :
    min_value = INF
    index = 0 # 가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1, n + 1) :
        if distance[i] < min_value and not visited[i] :
            min_value = distance[i]
            index = i
    return index

def dijkstra(start) :
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start] :
        distance[j[0]] = j[1]
    # 시작 노드를 제외한 전체 n - 1 개의 노드에 대해 반복
    for i in range(n - 1) :
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now] :
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐 다른 노드를 이동하는 거리가 짧은 경우
            if cost < distance[j[0]] :
                distance[j[0]] = cost

# 다익스트라 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1, n + 1) :
    if distance[i] == INF :
        print("INFINITY")
    else:
        print(distance[i])

#############################################################################
#############################################################################
### 방법 2.
### 개선된 다익스트라 알고리즘 - O(ElogV)
'''
    현재 가장 가까운 노드를 저장하기 위해, 우선순위 큐를 추가로 이용 !!
                                    이전엔, 선형 탐색했었음 = O(V)
    
    [우선순위 큐(Priority Queue)]
    := 우선순위가 가장 높은 데이터를 가장 먼저 삭제함.
    - PriorityQueue or heapq 라이브러리 사용 (heapq 더 빠름)
    - (가치, 물건) 튜플로 묶어 넣음.
    - 파이썬은 최소 힙(Min Heap) --> 값이 낮은 데이터 먼저 삭제
            - 최대 힙(Max Heap)은 음수 부호(-) 붙여 넣어 구현
    - 구현 방식
            - 힙 : 삽입, 삭제에 O(logN)
            - 리스트 : 삽입 O(1), 삭제 O(N)
'''

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수 입력 받기
n, m = map(int, input().split())
# 시작 노드 번호 입력 받기
start = int(input())
# 각 노드의 연결 정보를 담는 리스트 생성
graph = [[] for i in range(n + 1)]
# 최단 거리 테이블 무한으로 초기화
distance = [INF] * (n + 1)

# 간선 정보 입력 받기
for _ in range(m):
    a, b, c = map(int, input().split())  # (a 노드 -> b 노드) 의 비용이 c
    graph[a].append((b, c))

def dijkstra(start) :
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q : # 큐가 비어있지 않다면
        # 가장 짧은 최단 거리의 노드 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 노드면 무시
        if distance[now] < dist :
            continue
        # 현재 노드와 연결된 다른 인접 노드 확인
        for i in graph[now] :
            cost = dist + i[1]
            # 현재 노드 거쳐, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


# 다익스트라 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1, n + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])

'''
    입력 예시)
    6 11
    1
    1 2 2
    1 3 5
    1 4 1
    2 3 3
    2 4 2
    3 2 3
    3 6 5
    4 3 3
    4 5 1
    5 3 1
    5 6 2
    출력 예시)
    0 2 3 1 2 4
'''