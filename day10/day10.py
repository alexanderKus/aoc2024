def search(m,i,j,v,r):
  inside = lambda x,y: x>=0 and x<len(m) and y>=0 and y<len(m[0])
  if (i,j) in v: return
  v.add((i,j))
  if m[i][j] == 9:
    r[0] += 1
    return
  if inside(i,j+1) and m[i][j] == m[i][j+1] - 1: search(m,i,j+1,v,r)
  if inside(i+1,j) and m[i][j] == m[i+1][j] - 1: search(m,i+1,j,v,r)
  if inside(i,j-1) and m[i][j] == m[i][j-1] - 1: search(m,i,j-1,v,r)
  if inside(i-1,j) and m[i][j] == m[i-1][j] - 1: search(m,i-1,j,v,r)

def search2(m,i,j,r):
  inside = lambda x,y: x>=0 and x<len(m) and y>=0 and y<len(m[0])
  if m[i][j] == 9:
    r[0] += 1
    return
  if inside(i,j+1) and m[i][j] == m[i][j+1] - 1: search2(m,i,j+1,r)
  if inside(i+1,j) and m[i][j] == m[i+1][j] - 1: search2(m,i+1,j,r)
  if inside(i,j-1) and m[i][j] == m[i][j-1] - 1: search2(m,i,j-1,r)
  if inside(i-1,j) and m[i][j] == m[i-1][j] - 1: search2(m,i-1,j,r)

def one():
  m = []
  with open('input.txt', 'r') as f:
    for line in f.readlines():
      m.append([int(x) for x in line.replace('\n', '')])
  r = [0]
  for i in range(len(m)):
    for j in range(len(m[i])):
      if m[i][j] == 0:
        v = set()
        search(m,i,j,v,r)
  print(f'result1: {r[0]}')

def two():
  m = []
  with open('input.txt', 'r') as f:
    for line in f.readlines():
      m.append([int(x) for x in line.replace('\n', '')])
  r = [0]
  for i in range(len(m)):
    for j in range(len(m[i])):
      if m[i][j] == 0:
        search2(m,i,j,r)
  print(f'result2: {r[0]}')

if __name__ == '__main__':
  one()
  two()