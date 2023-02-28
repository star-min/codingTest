n = int(input())
graph = []
num = []
count = 0
result = 0
for i in range(n):
  graph.append(list(map(int,input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x, y):
  global count
  if x < 0 or y < 0 or x >= n or y >= n:
    return False
  if graph[x][y] == 1:
    count += 1
    graph[x][y] = 0
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      dfs(nx, ny)
    return True
  return False

for i in range(n):
  for j in range(n):
    if dfs(i,j) == True:
      num.append(count)
      result += 1
      count = 0

print(result)
num.sort()
for i in num:
  print(i)