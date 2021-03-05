# 위상 정렬 (Topology Sort)
'''
    위상 정렬 : 방향 그래프의 모든 노드를 '방향성에 거스르지 않도록 순서대로 나열하는 것'
    예) 선수과목 고려한 학습 순서 결정
    * O(V + E) : 모든 노드, 간선 확인

    진입 차수(Indegree) : 특정 노드로 '들어오는' 간선의 개수

    [진행 과정]
    1. 진입 차수가 0인 노드를 큐에 삽입
    2. 큐가 빌 때까지 아래 반복
        - 큐에서 원소 꺼내 해당 노드에서 출발하는 간선 제거
        - 진입 차수가 0이 된 노드 삽입

    * 모든 원소를 방문하기 전에 큐가 빈다면, 사이클 존재한다.
        - 보통 사이클 없는 문제
'''

from collections import deque

# 노드 수, 간선 수 입력 받기
v, e = map(int, input().split())
# 진입 차수
indegree = [0] * (v + 1)
# 그래프
graph = [[] for i in range(v + 1)]
# 모든 간선 정보 입력 받기
for _ in range(e) :
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort() :
    result = [] # 수행 결과 담을 리스트
    q = deque()

    # 진입차수가 0인 노드 삽입
    for i in range(1, v + 1) :
        if indegree[i] == 0 :
            q.append(i)

    while q :
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드의 진입차수 - 1
        for i in graph[now] :
            indegree[i] -= 1
            if indegree[i] == 0 :   # 새로 진입차수가 0이 되면 큐에 삽입
                q.append(i)

    # 출력
    for i in result :
        print(i, end=' ')

topology_sort()


'''
입력 예시)
7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4
출력 예시)
1 2 5 3 6 4 7
'''