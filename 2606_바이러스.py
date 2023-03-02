n = int(input())
m = int(input())
visited = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
  x, y = map(int,input().split())
  graph[x].append(y)
  graph[y].append(x)
def dfs(graph, i, visited):
  visited[i] = 1
  for j in graph[i]:
    if visited[j] == 0:
      dfs(graph,j,visited)
  return True
dfs(graph,1,visited)

print(sum(visited)-1)