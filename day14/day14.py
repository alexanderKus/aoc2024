import re

def one():
  W,H = 101,103
  #W,H = 11,7
  robots = []
  floor = [[0 for b in range(W)] for a in range(H)]
  with open('input.txt', 'r') as f:
    for line in f.readlines():
      px,py,x,y = re.findall(r'(\-*\d+)', line)
      robots.append((int(x),int(y),int(px),int(py)))
  for r in robots:
    px,py = r[2],r[3]
    floor[py][px] += 1
  #for f in floor: print(f)
  for _ in range(100):
    new_robots = []
    for r in robots:
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
  W,H = 101,103
  #W,H = 11,7
  robots = []
  floor = [[0 for b in range(W)] for a in range(H)]
  with open('input.txt', 'r') as f:
    for line in f.readlines():
      px,py,x,y = re.findall(r'(\-*\d+)', line)
      robots.append((int(x),int(y),int(px),int(py)))
  for r in robots:
    px,py = r[2],r[3]
    floor[py][px] += 1
  #for f in floor: print(f)
  idx = 0
  while True:
    idx += 1
    new_robots = []
    for r in robots:
      px,py,x,y = r[2],r[3],r[0],r[1]
      floor[py][px] -= 1
      floor[(py+y)%H][(px+x)%W] += 1
      new_robots.append((x,y,(px+x)%W,(py+y)%H))
    robots = new_robots
    if christmas_tree(floor,H,W): 
      print(f'result2: {idx}')
      for f in floor: print(['#' if x != 0 else '.' for x in f])
      break

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

def christmas_tree(m,h,w):
  for i in range(3,h-3):
    for j in range(3,w-3):
      if (m[i][j] != 0 and
           m[i+1][j-1] != 0 and m[i+1][j] != 0 and m[i+1][j+1] != 0 and
          m[i+2][j-2] != 0 and m[i+2][j-1] != 0 and m[i+2][j] != 0 and m[i+2][j+1] != 0 and m[i+2][j+2] != 0
      ):
        return True
  return False


if __name__ == '__main__':
  one()
  two()