# Dynamic Programming
# EX4) 효율적인 화폐 구성
'''
    N가지 종류의 화폐.
    이 화폐들의 개수를 최소한으로 이용해 그 가치의 합이 M원이 되도록 함.
    순서 상관X
    예) 2원, 3원 단위의 화폐가 있을 때, 15원 == 3원 X 5개

    입력 예시1)
    2 15            (1 <= N <= 100, 1 <= M <= 10,000)
    2               (각 화폐의 가치 <= 10,000)
    3
    출력 예시1) 5       (최소한의 화폐 개수)
    입력 예시2)
    3 4
    3
    5
    7
    출력 예시2) -1      (불가능할 시 -1)
'''

# N : 화폐 종류 개수, M : 가치의 합
n, m = map(int, input().split())
# 화폐 단위들
coin = []
for i in range(n) :
    coin.append(int(input()))

# DP 테이블 초기화
d = [10001] * (m + 1)

# 다이나믹 프로그래밍(보텀업)
d[0] = 0
for i in range(n) :
    for j in range(coin[i], m + 1) :
        if d[j - coin[i]] != 10001 : # (i - k) 원을 만드는 방법이 존재하는 경우.. 없어도 됨.
            d[j] = min(d[j], d[j - coin[i]] + 1)

print(d)
if d[m] == 10001 :
    print(-1)
else:
    print(d[m])