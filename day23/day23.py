def one():
  conn = dict()
  with open('input.txt', 'r') as f:
    for line in f.readlines():
      x,y = line.strip().split('-')
      if x in conn: conn[x].append(y)
      else: conn[x] = [y]
      if y in conn: conn[y].append(x)
      else: conn[y] = [x]
  lans = set()
  for k,v in conn.items():
    for i in range(len(v)-1):
      for j in range(i,len(v)):
        if v[j] not in conn[v[i]]: continue
        lan = tuple(sorted([k,v[i],v[j]]))
        if lan in lans: continue
        lans.add(lan)
  count = 0
  for a,b,c in lans:
    if a[0] == 't' or b[0] == 't' or c[0] == 't': count += 1
  print(f'result1: {count}')

def two():
  conn = dict()
  with open('input.txt', 'r') as f:
    for line in f.readlines():
      x,y = line.strip().split('-')
      if x not in conn: conn[x] = set()
      if y not in conn: conn[y] = set()
      conn[y].add(x)
      conn[x].add(y)
  sets = set()
  def search(node, req):
    key = tuple(sorted(req))
    nonlocal sets
    if key in sets: return
    sets.add(key)
    nonlocal conn
    for n in conn[node]:
      if n in req: continue
      if not all(n in conn[query] for query in req): continue
      search(n, {*req, n})
  for a in conn: search(a, {a})
  print('result2: '+','.join(sorted(max(sets,key=len))))


if __name__ == '__main__':
  one()
  two()