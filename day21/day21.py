from collections import deque
from itertools import product
from functools import cache

num_keypad = [
    ['7','8','9'],
    ['4','5','6'],
    ['1','2','3'],
    [None,'0','A']
]

dir_keypad = [
    [None,'^','A'],
    ['<','v','>']
]

def compute_seqs(keypad):
  pos = {}
  for r in range(len(keypad)):
    for c in range(len(keypad[r])):
      if keypad[r][c] is not None: pos[keypad[r][c]] = (r,c)
  seqs = {}
  for x in pos:
    for y in pos:
      if x == y:
        seqs[(x,y)] = ['A']
        continue
      possibilities = []
      q = deque([(pos[x],'')])
      optimal = float('inf')
      while q:
        (r,c),moves = q.popleft()
        for nr,nc,nm in [(r - 1,c,'^'),(r + 1,c,'v'),(r,c - 1,'<'),(r,c + 1,'>')]:
          if nr < 0 or nc < 0 or nr >= len(keypad) or nc >= len(keypad[0]): continue
          if keypad[nr][nc] is None: continue
          if keypad[nr][nc] == y:
            if optimal < len(moves) + 1: break
            optimal = len(moves) + 1
            possibilities.append(moves + nm + 'A')
          else:
            q.append(((nr,nc),moves + nm))
        else:
          continue
        break
      seqs[(x,y)] = possibilities
  return seqs

def solve(string,seqs):
  options = [seqs[(x,y)] for x,y in zip('A' + string,string)]
  return [''.join(x) for x in product(*options)]

num_seqs = compute_seqs(num_keypad)
dir_seqs = compute_seqs(dir_keypad)
dir_lengths = {key: len(value[0]) for key, value in dir_seqs.items()}

@cache
def compute_length(seq, depth=25):
  if depth == 1:
    return sum(dir_lengths[(x, y)] for x, y in zip("A" + seq, seq))
  length = 0
  for x, y in zip("A" + seq, seq):
    length += min(compute_length(subseq, depth - 1) for subseq in dir_seqs[(x, y)])
  return length

def one():
  codes = []
  with open('input.txt','r') as f: 
    for line in f.readlines():
      codes.append(line.strip())
  total = 0
  for code in codes:
    next = solve(code,num_seqs)
    for _ in range(2):
        possible_next = []
        for seq in next:
            possible_next += solve(seq,dir_seqs)
        minlen = min(map(len,possible_next))
        next = [seq for seq in possible_next if len(seq) == minlen]
    total += len(next[0]) * int(code[:-1])
  print(f'result1: {total}')

def two():
  codes = []
  with open('input.txt','r') as f: 
    for line in f.readlines():
      codes.append(line.strip())
  total = 0
  for code in codes:
    inputs = solve(code, num_seqs)
    length = min(map(compute_length, inputs))
    total += length * int(code[:-1])
  print(f'result2: {total}')

if __name__ == '__main__':
  one()
  two()