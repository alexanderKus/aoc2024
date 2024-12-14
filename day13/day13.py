def parse(line):
  import re
  found = re.findall(r'(\d+)', line)
  print(found)
  return int(found[0]), int(found[1])

v = set()
def find(ax,ay,ac,bx,by,bc,nx,ny,tx,ty,d):
  f = f'{ax},{ay},{ac},{bx},{by},{bc},{nx},{ny},{tx},{ty},{d}'
  if f in v: return 
  v.add(f)
  if nx == tx and ny == ty and ac <= 100 and bc <= 100:
    x = ac*3+bc 
    if x not in d: d.append(x)
    return
  if nx > tx or ny > ty or ac > 100 or bc > 100:
    return
  find(ax,ay,ac+1,bx,by,bc,nx+ax,ny+ay,tx,ty,d)
  find(ax,ay,ac,bx,by,bc+1,nx+bx,ny+by,tx,ty,d)

def one():
  result = 0
  with open('input.txt', 'r') as f:
    data = f.readlines()
  i = 0
  while i < len(data):
    if data[i] == '\n':
      i += 1
      continue
    ax, ay = parse(data[i])
    bx, by = parse(data[i+1])
    tx, ty = parse(data[i+2])
    d = []
    find(ax,ay,1,bx,by,0,ax,ay,tx,ty,d)
    find(ax,ay,0,bx,by,1,bx,by,tx,ty,d)
    if len(d) > 1: result += min(d)
    elif len(d) == 1: result += d[0]
    i += 3
  print(f'result1: {result}')

def two():
  pass

if __name__ == '__main__':
  one()
  two()