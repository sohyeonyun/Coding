# 서로소 집합 알고리즘을 통한, 무방향 그래프 내에서의 사이클 판별
'''
    - 서로소 집합 알고리즘 사용

    [사이클 판별 과정]
    1. 각 간선 확인하며 두 노드의 루트 노드 확인
        - 루트 노드 다르다면, 두 노드에 union 연산 수행
        - 루트 노드 같다면, 사이클 발생한 것
    2. 모든 간선에 대해 1 반복
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

v, e = map(int, input().split())
parent = [0] * (v + 1)

for i in range(1, v + 1) :
    parent[i] = i

# 사이클 발생 여부
cycle = False

for i in range(e) :
    a, b = map(int, input().split())
    # 사이클 발생 시 종료
    if find_parent(parent, a) == find_parent(parent, b) :
        cycle = True
        break
    # 사이클 발생하지 않았다면, 합집합 연산 수행
    else :
        union_parent(parent, a, b)

if cycle :
    print("사이클 발생")
else :
    print("사이클 발생 X")

'''
입력 예시)
3 3
1 2
1 3
2 3
출력 예시)
사이클 발생
'''