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
  pass

if __name__ == '__main__':
  one()
  two()