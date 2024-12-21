from collections import deque

#N = 7
N = 71
grid = [['.' for _ in range(N)] for _ in range(N)]
dirs = [(0,1),(1,0),(0,-1),(-1,0)]

def inside(x,y): return x>= 0 and x<N and y>=0 and y<N and grid[x][y] != '#'

def bfs(show=False):
  visited = set()
  q = deque([(0,0,0)])
  while q:
    x,y,cost = q.popleft()
    if x == 70 and y == 70:
      if show: print(cost)
      return True
    for (i,j) in dirs:
      dx,dy = x+i,y+j
      if inside(dx,dy) and (dx,dy) not in visited:
        visited.add((dx,dy))
        q.append((dx,dy,cost+1))
  return False

def one():
  b = []
  with open('input.txt','r') as f:
    for line in f.readlines():
      n = line.replace('\n','').split(',')
      b.append((int(n[0]), int(n[1])))
  for i,c in enumerate(b):
    if i == 1024: break 
    y,x = c[0],c[1]
    grid[x][y] = '#'
  bfs(True)

def two():
  b = []
  with open('input.txt','r') as f:
    for line in f.readlines():
      n = line.replace('\n','').split(',')
      b.append((int(n[0]), int(n[1])))
  for i,c in enumerate(b):
    if i == 1024: break 
    y,x = c[0],c[1]
    grid[x][y] = '#'
  for i,c in enumerate(b[1024:]):
    y,x = c[0],c[1]
    grid[x][y] = '#'
    reachable = bfs()
    if not reachable: 
      print(f'{y},{x}')
      return

if __name__ == '__main__':
  one()
  two()