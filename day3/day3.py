import re

def one():
  result = 0
  with open('input.txt', 'r') as f:
    text = f.read()
    muls = re.findall(r'mul\((\d+),(\d+)\)', text)
    for m in muls:
      result += int(m[0]) * int(m[1])
  print(result)

def two():
  result = 0
  is_enabled = True
  with open('input.txt', 'r') as f:
    text = f.read()
    muls = re.findall(r'(mul\((\d+),(\d+)\)|do\(\)|don\'t\(\))', text)
    for m in muls:
      if m[0] == 'don\'t()': 
        is_enabled = False
      elif m[0] == 'do()':
        is_enabled = True
      if is_enabled and 'mul' in m[0]:
        result += int(m[1]) * int(m[2])
  print(result)

if __name__ == '__main__':
  one()
  two()