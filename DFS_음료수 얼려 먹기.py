# DFS 예제
# 음료수 얼려 먹기
# n * m 크기의 얼음 틀에서, 구멍이 뚫린 부분(0)의 개수는? (연결된 부분은 하나로 본다.)

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    # 맵 벗어나면 리턴
    if x <= -1 or y <= -1 or x >= n or y >= m :
        return False

    # 구멍 뚫린 부분(0) 일 때 dfs 수행
    if graph[x][y] == 0 :
        # 방문 표시
        graph[x][y] = 1
        dfs(x, y+1)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x-1, y)
        return True

    return False

count = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            count += 1

print(count)


'''
입력 예시)
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000111111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111
출력 예시)
8
'''