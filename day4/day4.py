def check_row(b):
  if ((b[0] == "X" and b[1] == "M" and b[2] == "A" and b[3] == "S") or 
    (b[0] == "S" and b[1] == "A" and b[2] == "M" and b[3] == "X")):
    return 1
  return 0

def check_matrix(b):
  if ((b[0][0] == "M" and b[1][1] == "A" and b[2][2] == "S" and b[0][2] == "M" and b[1][1] == "A" and b[2][0] == "S") or
    (b[2][0] == "M" and b[1][1] == "A" and b[0][2] == "S" and b[0][0] == "M" and b[1][1] == "A" and b[2][2] == "S") or
    (b[2][2] == "M" and b[1][1] == "A" and b[0][0] == "S" and b[2][0] == "M" and b[1][1] == "A" and b[0][2] == "S") or
    (b[0][2] == "M" and b[1][1] == "A" and b[2][0] == "S" and b[2][2] == "M" and b[1][1] == "A" and b[0][0] == "S")):
    return 1
  return 0

def one():
  m = []
  result = 0
  with open('input.txt', 'r') as f:
    lines = f.readlines()
    for line in lines: m.append(line.replace('\n',''))
  for i in range(len(m)):
    for j in range(len(m[0])):
      if i < len(m) - 3 and j < len(m[i]) - 3:
        result += check_row([m[i][j],m[i+1][j+1],m[i+2][j+2],m[i+3][j+3]])
        result += check_row([m[i][j+3],m[i+1][j+2],m[i+2][j+1],m[i+3][j]])
      if i < len(m) - 3:
        result += check_row([m[i][j],m[i+1][j],m[i+2][j],m[i+3][j]])
      if j < len(m[i]) - 3:
        result += check_row([m[i][j],m[i][j+1],m[i][j+2],m[i][j+3]])
  print(result)

def two():
  m = []
  result = 0
  with open('input.txt', 'r') as f:
    lines = f.readlines()
    for line in lines: m.append(line.replace('\n',''))
  for i in range(len(m)-2):
    for j in range(len(m[0])-2):
      result += check_matrix([
        [m[i][j],  m[i][j+1],  m[i][j+2]],
        [m[i+1][j],m[i+1][j+1],m[i+1][j+2]],
        [m[i+2][j],m[i+2][j+1],m[i+2][j+2]]
      ])
  print(result)

if __name__ == '__main__':
  one()
  two()