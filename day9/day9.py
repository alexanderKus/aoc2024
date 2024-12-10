def build(x):
  out = []
  index = 0
  for i in range(len(x)):
    if i % 2 == 0: 
      for _ in range(int(x[i])): out.append(str(index))
      index += 1
    elif x[i] != '0':
      for _ in range(int(x[i])): out.append('.')
  return out

def valid(s):
  for i in range(len(s)-1):
    if s[i] == '.' and s[i+1] != '.': return False
  return True

def rearrange(x):
  l,r = 0,len(x)-1
  while not valid(x):
    while x[r] != '.':
      if x[l] == '.':
        #print(f'swap l{l} r{r} x[l]{x[l]} x[r]{x[r]}')
        x[l] = x[r]
        x[r] = '.'
        if valid(x): return
        if l < len(x)-1: l+=1
        if r > 0: r-=1
      if l >= len(x)-1: return
      while x[l] != '.': 
        if l >= len(x)-1: return
        l+=1
    while x[r] == '.': r -= 1

def one():
  with open('input.txt', 'r') as f:
    lines = f.read().replace('\n','')
  b = build(lines)
  rearrange(b)
  result = 0
  for i in range(len(b)):
    if b[i] != '.': result += i * int(b[i])
  print('result1: ', result)

def two():
  with open('input.txt', 'r') as f:
  #with open('sample.txt', 'r') as f:
    lines = f.read().replace('\n','')
  f = {}
  b = []
  fid = 0
  pos = 0 
  for i, char in enumerate(lines):
    x = int(char)
    if i % 2 == 0:
      if x == 0:
        raise ValueError("xd")
      f[fid] = (pos,x)
      fid += 1
    else:
      if x != 0: b.append((pos,x))
    pos += x

  while fid > 0:
    fid -=1
    pos, size = f[fid]
    for i, (s, l) in enumerate(b):
      if s >= pos:
        b = b[:i]
        break
      if size <= l:
        f[fid] = (s, size)
        if s == l: b.pop(i)
        else: b[i] = (s+size,l-size)
        break
  result = 0
  for fid, (pos, size) in f.items():
    for x in range(pos, pos+size):
      result += fid*x
  print('result2: ', result)

if __name__ == '__main__':
  one()
  two()