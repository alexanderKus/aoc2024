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
        print(f'swap l{l} r{r} x[l]{x[l]} x[r]{x[r]}')
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
  pass

if __name__ == '__main__':
  one()
  two()