from collections import deque
import heapq

def one():
  maze = []
  with open('input.txt', 'r') as f:
    for line in f.readlines():
      maze.append(list(line.replace('\n','')))
  sx,sy,ex,ey = -1,-1,-1,-1
  for i in range(len(maze)):
    for j in range(len(maze[i])):
      if maze[i][j] == 'S': sx,sy = i,j
      if maze[i][j] == 'E': ex,ey = i,j
  pq = [(0,sx,sy,0,1)]
  visited = {(sx,sy,0,1)}
  while pq:
    cost,row,col,dx,dy = heapq.heappop(pq)
    visited.add((row,col,dx,dy))
    if (row,col) == (ex,ey):
      print(cost)
      break
    for new_cost, nx, ny, ndx, ndy in [(cost+1, row+dx, col+dy, dx,dy),(cost+1000, row, col, dy,-dx), (cost+1000, row, col, -dy,dx)]:
      if maze[nx][ny] == '#' or (nx,ny,ndx,ndy) in visited: continue
      heapq.heappush(pq,(new_cost,nx,ny,ndx,ndy))
  
def two():
  maze = []
  with open('input.txt', 'r') as f:
    for line in f.readlines():
      maze.append(list(line.replace('\n','')))
  sx,sy,ex,ey = -1,-1,-1,-1
  for i in range(len(maze)):
    for j in range(len(maze[i])):
      if maze[i][j] == 'S': sx,sy = i,j
      if maze[i][j] == 'E': ex,ey = i,j
  pq = [(0,sx,sy,0,1)]
  lowest_cost = {(sx,sy,0,1):0}
  backtrack = {}
  best_cost = float('inf')
  end_states = set()

  while pq:
    cost,row,col,dx,dy = heapq.heappop(pq)
    if cost > lowest_cost.get((row,col,dx,dy), float('inf')): continue
    if (row,col) == (ex,ey):
      if cost > best_cost: break
      best_cost = cost
      end_states.add((row,col,dx,dy)) 
    for new_cost, nx, ny, ndx, ndy in [(cost+1, row+dx, col+dy, dx,dy),(cost+1000, row, col, dy,-dx), (cost+1000, row, col, -dy,dx)]:
      if maze[nx][ny] == '#': continue
      lowest = lowest_cost.get((nx,ny,ndx,ndy),float('inf'))
      if new_cost > lowest: continue
      if new_cost < lowest:
        backtrack[(nx,ny,ndx,ndy)] = set()
        lowest_cost[(nx,ny,ndx,ndy)] = new_cost
      backtrack[(nx,ny,ndx,ndy)].add((row,col,dx,dy))
      heapq.heappush(pq,(new_cost,nx,ny,ndx,ndy))
  states = deque(end_states)
  visited = set(end_states)
  while states:
    key = states.popleft()
    for l in backtrack.get(key,[]):
      if l in visited: continue
      visited.add(l)
      states.append(l)
  points = set((r,c)for r,c,_,_ in visited)
  print(len(points))

if __name__ == '__main__':
  one()
  two()