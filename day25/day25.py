def one():
  locks = []
  keys =[]
  with open('input.txt', 'r') as f:
    blocks = f.read().split('\n\n')
    for block in blocks:
      grid = [list(b.strip()) for b in block.split('\n')]
      if grid[0][0] == '#':
        x = []
        for r in range(len(grid[0])):
          count = 0
          for c in range(1,len(grid)):
            if grid[c][r] == '#': count += 1
          x.append(count)
        locks.append(tuple(x)) 
      else:
        x = []
        for r in range(len(grid[0])):
          count = 0
          for c in range(1,len(grid)):
            if grid[c][r] == '.': count += 1
          x.append(5-count)
        keys.append(tuple(x)) 
  print(locks)
  print(keys)
  count = 0
  pairs = set()
  for lock in locks:
    for key in keys:
      valid = True
      for i in range(5):
        if lock[i] + key[i] > 5: valid = False
      if valid and (lock,key) not in pairs: pairs.add((lock,key))
  print(f'result1: {len(pairs)}')

if __name__ == '__main__':
  one()