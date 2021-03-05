# Kruskal Algorithm
# Minimum Spanning Tree Algorithm
'''
    Spanning Tree(신장 트리) : 하나의 그래프가 있을 때 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프

    Kruskal Algorithm : 최소 비용으로 만들 수 있는 신장 트리를 찾음.
    * O(ElogE) - 간선 정렬 부분에서 오래 걸림.

    [진행 과정]
    1. 간선 데이터를 비용에 따라 오름차순 정렬
    2. 간선 하나씩 확인하며, 현재 간선이 사이클 발생시키는지 확인
        - 사이클 발생 X, 최소 신장 트리에 포함시킴
        - 사이클 발생 O, 최소 신장 트리에 포함 안시킴.
    3. 모든 간선에 대해 2 반복

    * 가장 거리가 짧은 간선부터 차례대로 집합에 추가 !
        단, 사이클 발생시키는 간선 제외.
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

# 노드 수, 간선 수 입력 받기
v, e = map(int, input().split())

parent = [0] * (v + 1)  # 부모 테이블
edges = []  # 간선 담을 리스트
result = 0  # 최종 비용

# 부모 테이블 초기화
for i in range(1, v + 1) :
    parent[i] = i

# 간선 입력받기
for i in range(e) :
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))  # (비용 순 정렬 위해 cost를 첫 번째 원소로 설정

# 간선 비용 순 정렬
edges.sort()

# 간선 하나씩 확인
for edge in edges :
    cost, a, b = edge
    # 사이클 확인 -> union-find
    if find_parent(parent, a) != find_parent(parent, b) :
        union_parent(parent, a, b)
        result += cost

print(result)



'''
입력 예시)
7 9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25
출력 예시)
159
'''