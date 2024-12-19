import re

def one():
  with open('input.txt','r') as f:
    numbers = re.findall('(\d+)',f.read())
  A,B,C,I = int(numbers[0]),int(numbers[1]),int(numbers[2]),numbers[3:]
  out = []
  i = 0
  while i < len(I)-1:
    print(i, A,B,C)
    opcode = int(I[i])
    operand = int(I[i+1])
    i += 2
    if opcode == 0:
      if operand >= 0 and operand <= 4: A //= 2 ** operand
      if operand == 4: A //= 2 ** A
      if operand == 5: A //= 2 ** B
      if operand == 6: A //= 2 ** C
      continue
    if opcode == 1:
      B ^= operand
      continue
    if opcode == 2:
      if operand >= 0 and operand <= 3: B = operand%8
      if operand == 4: B = A%8
      if operand == 5: B = B%8
      if operand == 6: B = C%8
      continue
    if opcode == 3:
      if A == 0: continue
      i = operand
      continue
    if opcode == 4:
      B ^= C
      continue
    if opcode == 5:
      if operand >= 0 and operand <= 3: out.append(operand%8)
      if operand == 4: out.append(A%8)
      if operand == 5: out.append(B%8)
      if operand == 6: out.append(C%8)
      continue
    if opcode == 6:
      if operand >= 0 and operand <= 3: B = A // 2 ** operand
      if operand == 4: B = A // 2 ** A
      if operand == 5: B = A // 2 ** B
      if operand == 6: B = A // 2 ** C
      continue
    if opcode == 7:
      if operand >= 0 and operand <= 3: C = A // 2 ** operand
      if operand == 4: C = A // 2 ** A
      if operand == 5: C = A // 2 ** B
      if operand == 6: C = A // 2 ** C
      continue
  print()
  print(','.join([str(x) for x in out]))

def two():
  pass

if __name__ == '__main__':
  one()
  two()