def valid(x, y, s, v):
  if len(s) == 0 and x == y: v[0] = True
  if len(s) == 0: return
  if len(s) > 1:
    if y == 0:
      valid(x, s[0], s[1:], v)
      valid(x, s[0], s[1:], v)
    else:
      valid(x, y+s[0], s[1:], v)
      valid(x, y*s[0], s[1:], v)
  else:
    valid(x, y+s[0], [], v)
    valid(x, y*s[0], [], v)

def valid2(x, y, s, v):
  concat = lambda x,y: int(str(x)+str(y))
  if len(s) == 0 and x == y: v[0] = True
  if len(s) == 0: return
  if len(s) > 1:
    if y == 0:
      valid2(x, s[0], s[1:], v)
      valid2(x, s[0], s[1:], v)
    else:
      valid2(x, y+s[0], s[1:], v)
      valid2(x, y*s[0], s[1:], v)
      valid2(x, concat(y,s[0]), s[1:], v)
  else:
    valid2(x, y+s[0], [], v)
    valid2(x, y*s[0], [], v)
    valid2(x, concat(y,s[0]), [], v)

def one():
  result = 0
  with open('input.txt', 'r') as f:
    for line in f.readlines():
      l = line.split(':')
      n, s = int(l[0]), [int(x) for x in l[1].split()]
      v = [False]
      valid(n,0,s,v)
      if v[0]: 
        #print(n, s)
        result += n
  print('result: ',result)

def two():
  # Take time to run (up to 5s)
  result = 0
  with open('input.txt', 'r') as f:
    for line in f.readlines():
      l = line.split(':')
      n, s = int(l[0]), [int(x) for x in l[1].split()]
      v = [False]
      valid2(n,0,s,v)
      if v[0]: 
        #print(n, s)
        result += n
  print('result2: ',result)

if __name__ == '__main__':
  one()
  two()