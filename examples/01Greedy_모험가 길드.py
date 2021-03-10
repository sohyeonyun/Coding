# 그리디
# EX1) 모험가 길드
'''
    모험가 N 명.
    '공포도'가 높은 모험가는 위험 상황에서 제대로 대처할 능력이 떨어진다.
    공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹에 참여해야 함.
    최대 몇 개의 모험가 그룹을 만들 수 있을까?
    단, 모든 모험가를 특정 그룹에 넣을 필요는 없다.

    예) N = 5,   공포도 : 2 3 1 2 2
        --> 1, 2, 3 / 2, 2
'''
'''
입력 예시)
5               # 모험가 수 N       1 <= N <= 100,000
2 3 1 2 2       # 각 모험가의 공포도
출력 예시)
2
'''

# 내 풀이 - 오류O
n = int(input())                        # 모험가의 수
data = list(map(int, input().split()))  # 각 모험가의 공포도
data.sort(reverse=True)

result = 0      # 그룹 수

i = 0
while i < n :
    i += data[i]    # 필요한 사람 수만큼 더해주기
    result += 1

print(result)


# 책 풀이
n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0  # 총 그룹 수
count = 0   # 현재 그룹에 포함된 모험가 수

for i in data : # 공포도가 낮은 것부터 확인
    count += 1  # 현재 그룹에
    if count >= i : # 그룹 결성
        result += 1
        count = 0
print(result)


'''
    [오류점]
    
    * 모두 데려가지 않아도 된다는 점 !
    [4, 1, 1, 1, 1] 예시 생각해보면 앎.
'''