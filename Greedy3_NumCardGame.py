# 숫자 카드 게임
'''
    각 행마다 가장 작은 수를 찾은 뒤,
    그 수 중에서 가장 큰 수를 찾기
'''

n, m = map(int, input().split())
result = 0
for i in range(n):
    line = list(map(int, input().split()))
    min_value = min(line)
    result = max(result, min_value)

print(result)