from queue import PriorityQueue 

def one():
  lq = PriorityQueue() 
  rq = PriorityQueue() 
  with open('input.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
      ll = line.split()
      l, r = ll[0], ll[1]
      lq.put(l, l)
      rq.put(r,r)
  result = 0
  for _ in range(lq.qsize()):
    result += abs(int(lq.get()) - int(rq.get()))
  print(result)

def two():
  left = []
  right = {}
  with open('input.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
      ll = line.split()
      l, r = int(ll[0]), int(ll[1])
      left.append(l)
      if r in right: right[r] += 1
      else: right[r] = 1
  result = 0
  for l in left:
    if l in right:
      result += l * right[l]
  print(result)

if __name__ == '__main__':
  one()
  two()