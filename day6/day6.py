import sys
sys.setrecursionlimit(100_000)

def count(map, c, i, j, maxi, maxj, s):
  # print(c, i, j, maxi, maxj)

  def inc(x, y):
    if (x, y) in s: return 0
    else:
      s.add((x,y))
      return 1

  if i >= maxi or i <= 0 or j >= maxj or j <= 0: 
    return inc(i,j)
  if c == '^':
    if map[i+1][j] == '#': return inc(i,j) + count(map, '>', i, j+1, maxi, maxj, s)
    else: return inc(i,j) + count(map, '^', i+1, j, maxi, maxj, s)
  if c == '>':
    if map[i][j+1] == '#': return inc(i,j) + count(map, 'V', i-1, j, maxi, maxj, s)
    else: return inc(i,j) + count(map, '>', i, j+1, maxi, maxj, s)
  if c == 'V':
    if map[i-1][j] == '#': return inc(i,j) + count(map, '<', i, j-1, maxi, maxj, s)
    else: return inc(i,j) + count(map, 'V', i-1, j, maxi, maxj, s)
  if c == '<':
    if map[i][j-1] == '#': return inc(i,j) + count(map, '^', i+1, j, maxi, maxj, s)
    else: return inc(i,j) + count(map, '<', i, j-1, maxi, maxj, s)
  raise Exception("How?")

def check(map, c, i, j, maxi, maxj, s, t):
  s.add((i,j))
  t+=1
  if i >= maxi or i <= 0 or j >= maxj or j <= 0: 
    return False
  if t >= maxi*maxj*2+1:
    return True
  if c == '^':
    if map[i+1][j] == '#': return check(map, '>', i, j+1, maxi, maxj, s,t)
    else: return check(map, '^', i+1, j, maxi, maxj, s,t)
  if c == '>':
    if map[i][j+1] == '#': return check(map, 'V', i-1, j, maxi, maxj, s,t)
    else: return check(map, '>', i, j+1, maxi, maxj, s,t)
  if c == 'V':
    if map[i-1][j] == '#': return check(map, '<', i, j-1, maxi, maxj, s,t)
    else: return check(map, 'V', i-1, j, maxi, maxj, s,t)
  if c == '<':
    if map[i][j-1] == '#': return check(map, '^', i+1, j, maxi, maxj, s,t)
    else: return check(map, '<', i, j-1, maxi, maxj, s,t)
  raise Exception("How?")


def one():
  map = []
  result = 0
  with open('input.txt', 'r') as f:
    for line in f.readlines():
      map.append([x for x in line.replace('\n','')])
  map.reverse()
  i, j = 0, 0
  for ii in range(len(map)):
    for jj in range(len(map[i])):
      if map[ii][jj] == '^':
        i, j = ii, jj
  result += count(map, '^', i, j, len(map)-1, len(map[0])-1, set())
  print(result)

def two():
  # Brute force solution. Takes time!
  map = []
  result = 0
  with open('input.txt', 'r') as f:
    for line in f.readlines():
      map.append([x for x in line.replace('\n','')])
  map.reverse()
  i, j = 0, 0
  for ii in range(len(map)):
    for jj in range(len(map[i])):
      if map[ii][jj] == '^':
        i, j = ii, jj
  for ii in range(len(map)):
    for jj in range(len(map[i])):
      if map[ii][jj] == '.':
        map[ii][jj] = '#'
        print(f'i: {ii}, j: {jj}')
        result += 1 if check(map, '^', i, j, len(map)-1, len(map[0])-1, set(), 0) else 0
        map[ii][jj] = '.'
  print(result)

if __name__ == '__main__':
  one()
  two()