
def is_row_safe(row):
  is_safe = True
  is_up = True if row[0] - row[1] < 0 else False
  for i in range(len(row)-1):
    diff = row[i] - row[i+1]
    if is_up and diff > 0:
      is_safe = False
    if not is_up and diff < 0:
      is_safe = False
    if abs(diff) < 1 or abs(diff) > 3:
      is_safe = False
  return is_safe

def one():
  m = []
  with open('input.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
      row = [int(x) for x in line.split()]
      m.append(row)
  result = 0
  for row in m:
    is_safe = is_row_safe(row)
    if is_safe:
      result += 1
  print(result)

def two():
  m = []
  with open('input.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
      row = [int(x) for x in line.split()]
      m.append(row)
  result = 0
  for row in m:
    is_safe = is_row_safe(row)
    if is_safe:
      result += 1
      continue
    if not is_safe:
      nrow = row[1:]
      is_safe = is_row_safe(nrow)
      if is_safe:
        result += 1
        continue
      nrow = row[:len(row)-1]
      is_safe = is_row_safe(nrow)
      if is_safe:
        result += 1
        continue
      for i in range(1,len(row)-1):
        nrow = row[:i] + row[i+1:]
        is_safe = is_row_safe(nrow)
        if is_safe:
          result += 1
          break

  print(result)

if __name__ == '__main__':
  one()
  two()