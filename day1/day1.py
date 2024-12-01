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
  pass

if __name__ == '__main__':
  one()
  two()