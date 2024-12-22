from collections import deque, Counter

dirs = [(0,1),(1,0),(0,-1),(-1,0)]

def inside(grid,x,y): return x>=1 and x<len(grid)-1 and y>=1 and y<len(grid[0])-1 and grid[x][y] != "#"

def one():
  grid = []
  with open('input.txt', 'r') as f:
    for line in f.readlines(): grid.append(list(line.replace('\n','')))
  
  init_cost = -1
  costs = []
  sx,sy = -1,-1
  for i in range(len(grid)):
    for j in range(len(grid[i])):
      if grid[i][j] == 'S': sx,sy = i,j

  q = deque([(sx,sy,0)])
  visited = set()
  while q:
    x,y,cost = q.popleft()
    visited.add((x,y))
    if grid[x][y] == 'E':
      init_cost = cost
      break
    for (i,j) in dirs:
      dx,dy = x+i,y+j
      if inside(grid,dx,dy) and (dx,dy) not in visited:
        q.append((dx,dy,cost+1))
  
  def bfs():
    q = deque([(sx,sy,0)])
    visited = set()
    while q:
      x,y,cost = q.popleft()
      visited.add((x,y))
      if grid[x][y] == 'E':
        nonlocal costs
        nonlocal init_cost
        print(init_cost - cost)
        costs.append(init_cost - cost)
        break
      for (i,j) in dirs:
        dx,dy = x+i,y+j
        if inside(grid,dx,dy) and (dx,dy) not in visited:
          q.append((dx,dy,cost+1))

  for i in range(1,len(grid)-1):
    for j in range(1,len(grid[i])-1):
      if grid[i][j] == 'S' or grid[i][j] == 'E': continue
      if j < len(grid[i])-2 and grid[i][j] == '#' and grid[i][j+1] == '.':
        grid[i][j] = '.'
        bfs()
        grid[i][j] = '#'
      if i < len(grid)-2 and  grid[i][j] == '#' and grid[i+1][j] == '.':
        grid[i][j] = '.'
        bfs()
        grid[i][j] = '#'
  
  #sorted_costs = dict(sorted(costs.items(), key=lambda item: item[1]))
  sorted_costs = dict(sorted((Counter(costs).most_common()), reverse=True))
  print(sorted_costs)
  result = 0
  for cost, x in sorted_costs.items():
    if cost >= 100:
      result += x
  print(f'result1: {result}')


def two():
  ...

if __name__ == '__main__':
  one()
  two()