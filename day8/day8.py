def find_antinodes(m, nodes, ul):
  valid = lambda x,y: x>=0 and x<len(m) and y>=0 and y<len(m[0])
  if len(nodes) == 1: return
  for i in range(1,len(nodes)):
    dx = nodes[i][0] - nodes[0][0]
    dy = nodes[i][1] - nodes[0][1]
    nx, ny = nodes[0][0]-dx, nodes[0][1]-dy
    nx2, ny2 = nodes[i][0]+dx, nodes[i][1]+dy
    if valid(nx, ny): ul.add((nx, ny))
    if valid(nx2, ny2): ul.add((nx2, ny2))
  find_antinodes(m, nodes[1:], ul)

def one():
  m = []
  ul = set()
  antennas = {}
  #with open('sample.txt', 'r') as f:
  with open('input.txt', 'r') as f:
    for line in f.readlines():
      m.append(line.replace('\n', ''))
  for i in range(len(m)):
    for j in range(len(m[i])):
      if m[i][j] != '.':
        if m[i][j] in antennas: antennas[m[i][j]].append((i,j))
        else: antennas[m[i][j]] = [(i,j)]
  for a in antennas:
    #if a == '#': continue
    find_antinodes(m, antennas[a], ul)
  print(len(ul))

def two():
  pass

if __name__ == '__main__':
  one()
  two()