import re

def one():
  W,H = 101,103
  #W,H = 11,7
  robots = []
  floor = [[0 for b in range(W)] for a in range(H)]
  with open('input.txt', 'r') as f:
    for line in f.readlines():
      px,py,x,y = re.findall(r'(\-*\d+)', line)
      print(px,py,x,y)
      robots.append((int(x),int(y),int(px),int(py)))
  for r in robots:
    px,py = r[2],r[3]
    floor[py][px] += 1
  #for f in floor: print(f)
  for _ in range(100):
    new_robots = []
    for r in robots:
      print(f)
      px,py,x,y = r[2],r[3],r[0],r[1]
      floor[py][px] -= 1
      floor[(py+y)%H][(px+x)%W] += 1
      new_robots.append((x,y,(px+x)%W,(py+y)%H))
    robots = new_robots
  #for f in floor: print(f)

  s = 0
  h,w = H//2,W//2
  for i in range(h):
    for j in range(w):
      s += floor[i][j]
  result = s
  s = 0
  for i in range(h):
    for j in range(w+1,W):
      s += floor[i][j]
  result *= s
  s = 0
  for i in range(h+1,H):
    for j in range(w):
      s += floor[i][j]
  result *= s
  s = 0
  for i in range(h+1,H):
    for j in range(w+1,W):
      s += floor[i][j]
  result *= s
  print(f'result1: {result}')

def two():
  pass

if __name__ == '__main__':
  one()
  two()