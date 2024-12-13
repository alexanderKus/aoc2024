#import sys
#sys.setrecursionlimit(100_000)

def calc(m,i,j,v,d):
  inside = lambda x,y: x>=0 and x<len(m) and y>=0 and y<len(m[0])
  if (i,j) in v: return
  v.add((i,j))
  d[0] += 1 # increment area
  if not inside(i, j+1): d[1] += 1
  if not inside(i+1, j): d[1] += 1
  if not inside(i, j-1): d[1] += 1
  if not inside(i-1, j): d[1] += 1
  if inside(i, j+1) and m[i][j+1] != m[i][j]: d[1] += 1
  if inside(i+1, j) and m[i+1][j] != m[i][j]: d[1] += 1
  if inside(i, j-1) and m[i][j-1] != m[i][j]: d[1] += 1
  if inside(i-1, j) and m[i-1][j] != m[i][j]: d[1] += 1
  if inside(i, j+1) and m[i][j+1] == m[i][j]: calc(m,i,j+1,v,d) 
  if inside(i+1, j) and m[i+1][j] == m[i][j]: calc(m,i+1,j,v,d) 
  if inside(i, j-1) and m[i][j-1] == m[i][j]: calc(m,i,j-1,v,d) 
  if inside(i-1, j) and m[i-1][j] == m[i][j]: calc(m,i-1,j,v,d) 
    
def calc2(m,i,j,v,vv,d):
  pass

def one():
  m = []
  with open('input.txt', 'r') as f:
    for line in f.readlines():
      m.append([x for x in line.replace('\n', '')])
  v = set()
  result = 0
  for i in range(len(m)):
    for j in range(len(m[i])):
      d = [0,0]
      if (i,j) not in v:
        calc(m,i,j,v,d)
      #if d[0] != 0: print(m[i][j],d[0],d[1])
      result += d[0]*d[1]
  print(f'result1: {result}')

def two():
  m = []
  with open('input.txt', 'r') as f:
    for line in f.readlines():
      m.append([x for x in line.replace('\n', '')])
  v = set()
  result = 0
  for i in range(len(m)):
    for j in range(len(m[i])):
      d = [0,0]
      vv = dict()
      if (i,j) not in v:
        calc2(m,i,j,v,vv,d)
      if d[0] != 0: print(m[i][j],d[0],d[1],  vv[m[i][j]])
      result += d[0]*d[1]
  print(f'result2: {result}')

if __name__ == '__main__':
  one()
  two()