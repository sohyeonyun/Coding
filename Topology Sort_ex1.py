# 그래프 - Topology Sort 문제
# EX) 커리큘럼
'''
    1번 ~ N번의 번호를 갖는 N개의 강의가 있다.
    각 강의는 선수 강의를 가지며 동시에 여러 강의를 들을 수 있다.
    N개의 강의를 수강하기까지 걸리는 최소 시간을 각각 출력하시오.
    예) 1번 강의(30시간)  ----> 3번 강의(40시간)           3번 강의까지 최소 시간은 70시간.
        2번 강의(20시간)  --|


'''
'''
입력 예시)
5           듣고자 하는 강의 수 N       1 <= N <= 500
10 -1       강의 시간, 선수 강의들의 번호, -1(각 줄 끝 표시)     1 <= 강의 시간 <= 100,000
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1
출력 예시)
10
20
14
18
17
'''

from collections import deque
import copy # deep copy

# 듣고자 하는 강의 수 N
n = int(input())
# 진입 차수
indegree = [0] * (n + 1)
# 선수 강의 정보
graph = [[] for _ in range(n + 1)]
# 강의 시간 정보
time = [0] * (n + 1)
# 모든 간선 정보 입력 받기
for i in range(1, n + 1) :
    data = list(map(int, input().split()))      # [map()] 안됨..
    time[i] = data[0]
    for x in data[1:-1] :   # 첫 번째 원소 ~ 마지막 -1 전까지
        graph[x].append(i)  # 수강순서 x -> i
        indegree[i] += 1    # i로 들어오는 간선 개수

# 위상 정렬
result = copy.deepcopy(time)
q = deque()

# 진입 차수가 0인 노드 큐에 삽입
for i in range(1, n + 1) :
    if indegree[i] == 0 :
        q.append(i)

# 큐가 빌 때까지
while q :
    now = q.popleft()
    for i in graph[now] :
        result[i] = max(result[i], result[now] + time[i])   # 이전 시간 + 현재 시간
        indegree[i] -= 1
        if indegree[i] == 0 :   # 진입 차수 0이면 큐에 삽입
            q.append(i)

# 최소 시간 결과 출력
for i in range(1, n + 1) :
    print(result[i])