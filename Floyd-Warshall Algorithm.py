# 최단 경로 알고리즘
# 2. 플로이드 워셜 알고리즘 (Floyd-Warshall)
'''
    모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구해야 하는 경우

    [동작 과정]
    - 3중 반복문 사용해 점화식 따라 최단 거리 테이블 갱신
    - A에서 B로 가는 최소 비용 vs. A에서 K를 거쳐 B로 가는 비용

    [점화식(다이나믹)]             <-> 다익스트라 : 그리디
    Dab = min(Dab, Dak + Dkb)

    O(N^3)
    - N개의 단계마다 O(N^2)의 연산
    - 최단 거리 테이블 : 2차원 리스트

'''

INF = int(1e9)

n = int(input())    # 노드 개수
m = int(input())    # 간선 개수

# 2차원 리스트(그래프), 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신으로 가는 비용 == 0
for a in range(1, n + 1) :
    for b in range(1, n + 1) :
        if a == b :
            graph[a][b] = 0

# 각 간선에 대한 정보 입력받아 초기화
for _ in range(m) :
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 점화식 따라 플로이드 워셜 수행
for k in range(1, n + 1) :
    for a in range(1, n + 1) :
        for b in range(1, n + 1) :
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 결과 출력
for a in range(1, n + 1) :
    for b in range(1, n + 1) :
        if graph[a][b] == INF :
            print("INFINITY", end=' ')
        else :
            print(graph[a][b], end=' ')
    print()

'''
입력 예시)
4
7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2
출력 예시)
0 4 8 6
3 0 7 9
5 9 0 4
7 11 2 0
'''