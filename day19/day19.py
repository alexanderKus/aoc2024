
def valid(towel, patterns):
  if towel == '': 
    #print('end')
    return True
  for pattern in patterns:
    v = False
    if towel[:len(pattern)] == pattern:
      if valid(towel[len(pattern):],patterns): 
        #print(towel[len(pattern):])
        v = True
    if v: return True
  return False

def one():
  with open('input.txt','r') as f:
    data = f.readlines()
  patterns = sorted([x.strip() for x in data[0].replace('\n','').split(',')],key=len,reverse=True)
  towels = [x.replace('\n','') for x in data[2:]]
  count = 0
  for towel in towels:
    if valid(towel, patterns): 
      #print(f'valid towel: {towel}')
      count += 1
  print(f'Result1: {count}')

def two():
  ...

if __name__ == '__main__':
  one()
  two()