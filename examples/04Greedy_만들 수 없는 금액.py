# 그리디
# EX4) 만들 수 없는 금액
'''
    N개의 동전을 이용하여 만들 수 없는 양의 정수 금액 중 최솟값?
    예) N = 5, 3원, 2원, 1원, 1원, 9원 --> 8원은 만들 수 없다.
    예2) N = 3, 3원, 5원, 7원 --> 1원은 만들 수 없다.
'''
'''
    입력 예시)
    5           # 1 <= N <= 1,000
    3 2 1 1 9   # 각 단위 <= 1,000,000
    출력 예시) 8
'''

n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data :
    # print('x: ', x, '    target: ', target)
    # 만들 수 없는 금액 찾았을 때 종료
    if target < x :
        break
    target += x # target 이전까지의 수는 다 만들 수 있다는 의미


print(target)

'''
    [피드백]
    아예 접근법을 못찾음...
    - 소팅 후 앞 숫자들을 다 더했을때도 뒷숫자보다 작으면 그 숫자는 생성 불가    
'''