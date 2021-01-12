# 시뮬레이션 - 게임 개발
'''
    캐릭터가 맵 안에서 움직이는 시스템 개발
    캐릭터 위치(A, B) : A는 북쪽으로부터 떨어진 칸의 개수, B는 서쪽으로부터 떨어진 칸의 개수
    바다로는 못 감.
    [매뉴얼]
    1. 현재 방향 기준 왼쪽 방향부터 차례로 갈 곳 정함
    2. 아직 가보지 않은 칸 있다면, 왼쪽 방향으로 회전 후 왼쪽으로 한 칸 전진
        가보지 않은 칸이 없다면, 왼쪽 방향으로 회전 후 1단계로 돌아감
    3. 만약 네 방향 모두 이미 가본 칸이거나 바다인 경우, 방향 유지한 채로 한칸 뒤로 가고 1단계로 돌아감.
        단, 뒤쪽 방향이 바다 칸이면 멈춤.
    [바라보는 방향(d)]
        0(북쪽), 1(동쪽), 2(남쪽), 3(서쪽)
    [맵 정보]
        0(육지), 1(바다)
    [입력 예시]
    4 4     # 4 x 4 맵
    1 1 0   # (1, 1)에서 북쪽(0)을 바라보고 선 캐릭터
    1 1 1 1 # 맵
    1 0 0 1
    1 1 0 1
    1 1 1 1
'''

'''
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
'''

# 세로, 가로
n, m = map(int, input().split())
# 캐릭터 좌표(A, B), 바라보는 방향(d)
x, y, direction = map(int, input().split())
# 맵 입력
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 방문 위치 저장
d = [[0] * m for _ in range(n)]
d[x][y] = 1 # 시작 위치 방문 표시

# 북(0), 동(1), 남(2), 서(3) 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
count = 1 # 방문 횟수
turn_time = 0
while True:
    # 왼쪽 방향부터 차례로 갈 곳 정함
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 가보지 않은 칸이고 육지면 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        print(x, y)
        continue
    # 가본 칸이거나 바다인 경우
    else:
        turn_time += 1

    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dx[direction]
        # 뒤로 갈 수 있으면 이동
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다면 종료
        else:
            break
        turn_time = 0

print(count)