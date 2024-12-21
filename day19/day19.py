from functools import cache

def valid(towel, patterns):
  if towel == '': return True
  for pattern in patterns:
    v = False
    if towel[:len(pattern)] == pattern:
      if valid(towel[len(pattern):],patterns): 
        v = True
    if v: return True
  return False

def one():
  with open('input.txt','r') as f:
    data = f.readlines()
  patterns = sorted([x.strip() for x in data[0].replace('\n','').split(',')],key=len,reverse=True)
  towels = [x.replace('\n','') for x in data[2:]]
  count = sum(1 if valid(towel,patterns) else 0 for towel in towels)
  print(f'Result1: {count}')


def two():
  with open('input.txt','r') as f:
    data = f.readlines()
  patterns = sorted([x.strip() for x in data[0].replace('\n','').split(',')],key=len,reverse=True)
  towels = [x.replace('\n','') for x in data[2:]]

  @cache
  def valid2(towel):
    if towel == '': return 1
    c = 0
    nonlocal patterns
    for pattern in patterns:
      if towel[:len(pattern)] == pattern:
        c += valid2(towel[len(pattern):])
    return c

  count = sum(valid2(towel) for towel in towels)
  print(f'Result2: {count}')

if __name__ == '__main__':
  one()
  two()