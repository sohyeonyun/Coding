# 그래프 - Union-Find 문제
# EX) 팀 결성
'''
    0번 ~ N번의 학생들이 있다. 처음에는 모두 서로 다른 N + 1 개의 팀이다.
    선생님은 '팀 합치기'와 '같은 팀 여부 확인'이 가능하다.
    선생님이 M개의 연산을 수행할 수 있을 때, '같은 팀 여부 확인'에 대한 연산 결과를 출력하시오.

    '팀 합치기'는 0 a b 형태로 주어짐. a번 학생 팀과 b번 학생 팀을 합침.
    '같은 팀 여부 확인'은 1 a b 형태로 주어짐. a번 학생과 b번 학생이 같은 팀에 속하는지 확인.
                - a, b <= N
'''
'''
입력 예시)
7 8         # N, M(입력 연산 개수)        1 <= N, M <= 100,000
0 1 3       # 각각의 연산
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1
출력 예시)
NO
NO
YES
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
    return parent

# 학생 수, 연산 수 입력 받기
n, m = map(int, input().split())

# 부모 노드 테이블 초기화
parent = [0] * (n + 1)
for i in range(n + 1) : # 학생 0번부터
    parent[i] = i

for _ in range(m) :
    oper, a, b = map(int, input().split())
    if oper == 0 :  # 팀 합치기 - union
        parent = union_parent(parent, a, b)
    else :  # 같은 팀 확인하기 - find_parent
        if find_parent(parent, a) == find_parent(parent, b) :
            print("YES")
        else :
            print("NO")
