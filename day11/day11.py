from functools import cache

def transform_stone(stone):
  if stone == 0: return 1, None
  s = str(stone)
  if len(s) % 2 == 0: return int(s[:len(s)//2]), int(s[len(s)//2:])
  return stone * 2024, None

@cache
def run(stone, n):
  if n == 0: return 1
  x, y = transform_stone(stone)
  if y is None: return run(x, n-1)
  return run(x, n-1) + run(y, n-1)

def one():
  with open('input.txt','r') as f:
    line = f.read().replace('\n','').split(' ')
  stones = [int(x) for x in line]
  l = 0
  for stone in stones:
    l += run(stone,25)
  print(f'result1: {l}')

def two():
  with open('input.txt','r') as f:
    line = f.read().replace('\n','').split(' ')
  stones = [int(x) for x in line]
  l = 0
  for stone in stones:
    l += run(stone,75)
  print(f'result2: {l}')

if __name__ == '__main__':
  one()
  two()