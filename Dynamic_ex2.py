# Dynamic Programming
# EX2) 개미 전사
'''
    일직선의 식량창고 약탈. 최소한 한 칸 이상 떨어진 식량창고여야 함.
    예) {1, 3, 1, 5} --> 최대 8(3 + 5)개 약탈 가능

    3 <= N(식량 창고 수) <= 100
    0 <= K(각 창고에 저장된 식량 수) <= 1,000

    입력)
    4
    1 3 1 5
    출력)
    8
'''
'''
    i 번째 선택 O --> i 번째 값 + (i - 2) 번째까지 선택한 값
    i 번째 선택 X --> (i - 1) 번째까지 선택한 값
'''

n = int(input())
array = list(map(int, input().split()))

d = [0] * 100

d[0] = array[0]
d[1] = max(array[1], array[0])
for i in range(3, n) :
    d[i] = max(array[i] + d[i - 2], d[i - 1])

print(d[n - 1])