# Graph
'''
Node(Vertex), Edge
Adjacent(인접) : 두 노드가 edge로 연결됨

1. Adjacency Matrix(인접 행렬)
    - 2차원 배열로 그래프 관계 표현
    - 단) 메모리 측면에서, 모든 관계를 저장하므로 노드 개수가 많을수록 메모리 낭비
2. Adjacency List(인접 리스트)
    - 리스트로 그래프 관계 표현
    - 장) 연결된 정보만 저장해서 메모리의 효율적 사용
    - 단) 특정 두 노드가 연결되었는지 정보 얻는 속도가 느림
'''

# 1. 인접 행렬
INF = 987654321
graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]
print(graph)

# 2. 인접 리스트 - (노드, 거리)
graph = [[] for _ in range(3)]

graph[0].append((1, 7))
graph[0].append((2, 5))
graph[1].append((0, 7))
graph[2].append((0, 5))

print(graph)