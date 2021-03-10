# 그리디
# EX5) 볼링공 고르기
'''
    두 사람이 서로 무게가 다른 볼링공을 고르려 할 때의 경우의 수?
    N개의 볼링공마다 무게가 같을 수 있지만 다른 공으로 간주한다. 공 번호는 1번부터이다.
    볼링공 무게는 1부터 M까지 자연수다.
    예) N = 5, M = 3     무게는 1, 3, 2, 3, 2 이다.
        --> (1번, 2번), (1, 3), (1, 4), (1, 5), (2, 3), (2, 5), (3, 4), (4, 5) => 8가지
'''
'''
    입력 예시)
    5 3             1 <= N <= 1,000     1 <= M <= 10
    1 3 2 3 2       1 <= 각 무게 <= M
    출력 예시) 8
    입력2)
    8 5
    1 5 4 3 2 4 5 2
    출력2) 25
'''

n, ball_max = map(int, input().split())
balls = list(map(int, input().split()))

balls.sort()    # 1 2 2 3 3

result = 0  # 경우의 수

same = 1 # 같은 숫자 카운트

for i in range(n - 1) :
    print(i, i + 1)
    if balls[i] == balls[i + 1] :
        same += 1
        continue
    if same == 1 :
        result += (n - i - 1)
    else :
        result += (n - i - 1) * same
        same = 1
    print(result)

print(result)


# 책 풀이
n, m = map(int, input().split())
data = list(map(int, input().split()))

array = [0] * 11    # 0~10까지의 무게 담을 리스트
for x in data :
    array[x] += 1

result = 0
# 1부터 m까지의 각 무게에 대하여 처리
for i in range(1, m + 1) :
    n -= array[i]   # 무게가 i인 볼링공의 개수 제외
    result += array[i] * n  # A 선택 수 * B 선택 수
print(result)

'''
    [피드백]
    - 리스트에 각 무게의 개수를 미리 계산
    - 전체 공 개수에서 특정 무게의 공 수를 빼서 경우의 수 계산
'''