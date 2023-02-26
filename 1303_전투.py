from collections import deque

n, m = map(int,input().split())

graph = [list(input()) for _ in range(m)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y,col): #col을 매개변수로 받아와 W or B 체크
    q = deque()
    q.append((x,y))
    cnt = 0
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if graph[nx][ny] == col and graph[nx][ny] != 0: #graph[nx][ny]의 값이 매개변수로 받아온 col과 같고 이미 처리되지 않았다면 q에 추가
                    q.append((nx,ny))
                    cnt += 1
                    graph[nx][ny] = 0
    return(1 if cnt == 0 else cnt)

w_cnt = 0
b_cnt = 0
print(graph)
for i in range(m):
    for j in range(n):
        if graph[i][j] != 0:
            if graph[i][j] == 'W':
                w_cnt += bfs(i,j,graph[i][j]) ** 2
            elif graph[i][j] == 'B':
                b_cnt += bfs(i,j,graph[i][j]) ** 2

print(w_cnt, b_cnt)