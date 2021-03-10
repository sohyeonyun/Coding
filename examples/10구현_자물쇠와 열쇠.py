# 구현
# 자물쇠와 열쇠 -         https://programmers.co.kr/learn/courses/30/lessons/60059
'''
    자물쇠는 한 칸의 크기가 1 X 1 인 N X N 크기의 정사각 격자 형태.
    열쇠는 M X M 크기의 정사각 격자 형태. 회전과 이동이 가능
    자물쇠 영역 내에서는 열쇠의 돌기 부분과 자물쇠의 홈 부분이 정확히 일치해야 함.
    자물쇠 영역을 벗어난 부분에 있는 열쇠의 홈과 돌기는 상관X, 돌기끼리 만나면 안됨.
    자물쇠의 모든 홈을 채워 비어있는 곳이 없어야 함.
'''

import copy

key = [[0, 0, 0],
       [1, 0, 0],
       [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]


def rotate(key, m):
    new_key = []
    for i in range(m - 1, -1, -1):
        tmp = []
        for j in range(m):
            tmp.append(key[j][i])
        new_key.append(tmp)
    return new_key

# 끼웠을 때 모두 1인지 확인
def check(matrix, n):       # (확대한 매트릭스, lock 크기)
    for i in range(n, 2 * n):
        for j in range(n, 2 * n):
            if matrix[i][j] != 1:
                return False
    return True

def solution(key, lock):
    answer = False

    m = len(key)
    n = len(lock)

    # 4방향 key들 저장
    keys = []
    keys.append(key)
    for i in range(3):
        key = rotate(key, m)
        keys.append(key)

    # 자물쇠의 3배 확대
    matrix = [[0] * (3 * n) for _ in range(3 * n)]
    # 가운데 부분 lock 표시
    for i in range(n):
        for j in range(n):
            matrix[i + n][j + n] = lock[i][j]

    # 4방향 + 한 칸씩 이동하며 자물쇠에 열쇠 끼우기
    for cur_key in keys:
        # 시작점 : [x][y]
        for x in range(n * 2):
            for y in range(n * 2):
                tmp = copy.deepcopy(matrix)         # import 시간 + deepcopy 자체의 느린 시간 --> 비추. (check 후 다시 열쇠값 빼주는 것이 나음)
                # 자물쇠에 열쇠 끼우기
                for i in range(m):
                    for j in range(m):
                        tmp[x + i][y + j] += cur_key[i][j]
                print(tmp)
                # 맞는지 확인
                if check(tmp, n):
                    return True

    return answer


print(solution(key, lock))
