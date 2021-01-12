# 구현 - 왕실의 나이트
'''
    입력한 위치에 대하여 아래 두 경우에 대해 이동할 수 있는 경우의 수 출력
    1. 수형 두 칸 이동 -> 수직 한 칸 이동
    2. 수직 두 칸 이동 -> 수평 한 칸 이동
    행 : 1 ~ 8
    열 : a ~ h
    이동 예) a1 => c2 or b3 이동
    예시) 입력 a1 -> 출력 2
    예시2) 입력 c2 -> 출력 6
'''

input_data = input() # type : str
row = int(input_data[1])
col = int(ord(input_data[0])) - int(ord('a')) + 1

result = 0
steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]
for step in steps:
    next_row = row + step[0]
    next_col = col + step[1]
    if 1 <= next_row <= 8 and 1 <= next_col <= 8:
        result += 1

print(result)