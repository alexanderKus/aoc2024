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
        if not good:
          ...
          result += int(numbers[len(numbers)//2])
  print(result)
  pass

if __name__ == '__main__':
  one()
  two()