# 구현 - 상하좌우

# sol 1
n = int(input())
moves = list(input().split())

current = [1, 1]
temp = [0, 0]
for move in moves:
    temp[0] = current[0]
    temp[1] = current[1]
    if move == 'R':
        temp[1] += 1
    elif move == 'L':
        temp[1] -= 1
    elif move == 'U':
        temp[0] -= 1
    else: # Down
        temp[0] += 1

    if (1 <= temp[0] <= n) and (1 <= temp[1] <= n):
        current[0] = temp[0]
        current[1] = temp[1]
        # current = temp  # 같은 오브젝트라서 안됨~! 아예 덮여버림 !!!

print(current[0], current[1])

# sol 2
n = int(input())
x, y = 1, 1
plans = input().split() # 리스트 반환

# L, R, U, D
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue

    x, y = nx, ny

print(x, y)