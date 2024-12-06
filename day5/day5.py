def one():
  d = {}
  result = 0
  with open('input.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
      if '|' in line:
        l, r = line.replace('\n','').split('|')
        if l in d:
          d[l].append(r)
        else:
          d[l] = [r]
      if ',' in line:
        numbers = line.replace('\n', '').split(',')
        done = set()
        good = True
        for x in numbers:
          if x in d:
            for after in d[x]:
              if after in done:
                good = False
          done.add(x)
        if good:
          result += int(numbers[len(numbers)//2])
  print(result)

def two():
  from functools import cmp_to_key
  def compare(x, y):
    if (x,y) in dd: return -1
    if (y,x) in dd: return 1
    return 0

  d = {}
  dd = set()
  result = 0
  with open('input.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
      if '|' in line:
        l, r = [x for x in line.replace('\n','').split('|')]
        if l in d:
          d[l].append(r)
        else:
          d[l] = [r]
        dd.add((l, r))
      if ',' in line:
        numbers = line.replace('\n', '').split(',')
        done = set()
        good = True
        for x in numbers:
          if x in d:
            for after in d[x]:
              if after in done:
                good = False
          done.add(x)
        if not good:
          numbers.sort(key=cmp_to_key(compare))
          result += int(numbers[len(numbers)//2])
  print(result)
  pass

if __name__ == '__main__':
  one()
  two()