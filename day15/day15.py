def inside(m,i,j):
  return i>=0 and i<len(m) and j>=0 and j<len(m[0])

def one():
  warehouse = []
  moves = []
  dirs = {'>':(0,1), 'v':(1,0), '<':(0,-1), '^':(-1,0)}
  with open('input.txt', 'r') as f:
    m = False
    for line in f.readlines():
      if line == '\n': 
        m = True
        continue
      if m: 
        for move in line.replace('\n',''):
          moves.append(move)
      else: warehouse.append([x for x in line.replace('\n','')])
  rx, ry = -1,-1
  for i in range(len(warehouse)):
    for j in range(len(warehouse[i])):
      if warehouse[i][j] == '@':
        rx,ry = i,j
  for index, move in enumerate(moves):
    print(f'index: {index}, move: {move}')
    dx, dy = dirs[move]
    if warehouse[rx+dx][ry+dy] == '#':
      print(f'hit the wall {warehouse[rx+dx][ry+dy]}')
      continue
    if warehouse[rx+dx][ry+dy] == 'O':
      boxes = -1
      i = 2
      nx,ny = rx+dx*i,ry+dy*i
      while inside(warehouse,nx,ny):
        if warehouse[nx][ny] == '#':
          break
        if warehouse[nx][ny] == '.':
          boxes = i
          break
        i += 1
        nx,ny = rx+dx*i,ry+dy*i
      if boxes == -1:
        print(f'cannot move any boxes{boxes}')
        continue
      for j in range(1,boxes):
        nx,ny = rx+dx*i,ry+dy*i
        warehouse[nx][ny] = 'O'
    warehouse[rx][ry] = '.'
    rx,ry = rx+dx,ry+dy
    warehouse[rx][ry] = '@'
    for w in warehouse: print(''.join(w))
  result = 0
  for i in range(len(warehouse)):
    for j in range(len(warehouse[i])):
      if warehouse[i][j] == 'O':
        result += 100*i+j
  print(f'result1: {result}')

def two():
  warehouse = []
  moves = []
  dirs = {'>':(0,1), 'v':(1,0), '<':(0,-1), '^':(-1,0)}
if __name__ == '__main__':
  one()
  two()