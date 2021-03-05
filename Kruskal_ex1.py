# 그래프 문제 - MST 찾기( Kruskal Algorithm )
# EX) 도시 분할 계획
'''
    한 마을에 N개의 집, 그 집들을 연결하는 M개의 길이 있다.
    이 마을을 2개의 분리된 마을로 분할할 계획이다.
    그 분리된 마을 사이의 길을 없애고 각 분리된 마을 내에서도 두 집 사이의 경로가 항상 존재하게 하면서 길을 더 없앨 수 있다.
    위 조건대로 길을 모두 없애고 나머지 길의 유지비의 합을 최소로 하고 싶다.
    --> Kruskal Algorithm

    1. MST 찾기 --> Kruskal Algorithm
    2. 두 개의 MST --> 전체 비용에서, 가장 비용이 큰 간선(마지막 간선)의 비용 빼기

'''
'''
입력 예시)
7 12        # 집 개수 N, 길 개수 M        2 <= N <= 100,000   1 <= M <= 1,000,000
1 2 3       # 길 정보      A - B 유지비: C        1 <= C <= 1,000
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4
출력 예시)
8           # 길을 없애고 남은 유지비의 합의 최솟값
'''

def find_parent(parent, x) :
    if parent[x] != x :
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b) :
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b :
        parent[b] = a
    else :
        parent[a] = b

# 집 개수, 길 개수
n, m = map(int, input().split())

# 부모 테이블
parent = [0] * (n + 1)
for i in range(1, n + 1) :
    parent[i] = i

# 간선 정보
edges = []
for _ in range(m) :
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

# 유지비 기준 정렬
edges.sort()

# MST에 포함되는 간선 중 가장 비용이 큰 간선(== 마지막 추가 간선)
last = 0
# 최종 비용
result = 0

# Kruskal
for edge in edges :
    cost, a, b = edge
    # 사이클 발생하지 않았을 때만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b) :
        union_parent(parent, a, b)
        result += cost
        last = cost

print(result - last)
