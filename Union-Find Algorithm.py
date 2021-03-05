# 서로소 집합 자료구조
# Union-Find 자료구조
'''
    서로소 집합 자료구조(union-find 자료구조) : 서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조
    - union, find 연산

    [진행 과정]
    * 부모 노드 저정할 테이블 필요
    1. union(합집합) 연산 확인, 서로 연결된 두 노드 A, B 확인
        - A와 B의 루트 노드 A', B' 찾음
        - A'를 B' 부모 노드로 설정(번호가 더 작은 원소가 부모 노드가 되도록 설정)
    2. 모든 union 처리 때까지 1 반복

    ==> 무방향 그래프 내에서 사이클 판별 가능 !!
'''

# 특정 원소 x가 속한 집합 찾기 - 경로 압축(Path Compression) 기법 적용
def find_parent(parent, x) :
    if parent[x] != x : # 루트 노드가 아니라면, 루트 노드 찾을 때까지 재귀 호출
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소 a, b가 속한 집합 찾기
def union_parent(parent, a, b) :
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b :
        parent[b] = a
    else :
        parent[a] = b

# 노드 개수, 간선 수 입력 받기
v, e = map(int, input().split())
parent = [0] * (v + 1)  # 부모 테이블 초기화

# 부모 테이블 자기 자신으로 초기화
for i in range(1, v + 1) :
    parent[i] = i

# union 연산 수행
for i in range(e) :
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력
print('각 원소가 속한 집합: ', end=' ')
for i in range(1, v + 1) :
    print(find_parent(parent, i), end=' ')
print()

# 부모 테이블 출력
print('부모 테이블: ', end=' ')
for i in range(1, v + 1) :
    print(parent[i], end=' ')



'''
입력 예시)
6 4         # 노드 개수, 간선 수
1 4
2 3
2 4
5 6
출력 예시)
1 1 1 1 5 5
1 1 1 1 5 5
'''
