from collections import deque

t = int(input())


def bfs(x, y):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):  # 상하좌우 모두 확인
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and ny >= 0 and nx < m and ny < n:  # 틀에 벗어나지않고
                if graph[nx][ny] == 1:  # 해당 위치가 1이라면
                    graph[nx][ny] = 0  # 0으로 변경한 후
                    q.append((nx, ny))  # 1이였던 위치를 deque에 추가해준다.


for i in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * n for _ in range(m)]
    for i in range(k):
        a, b = map(int, input().split())
        graph[a][b] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    cnt = 0

    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1:  # i,j의 위치 값이 1이라면
                bfs(i, j)  # 주변을 bfs함수를 사용하여 0으로 변경
                cnt += 1  # 그리고 카운트를 증가시켜준다.![]

    print(cnt)