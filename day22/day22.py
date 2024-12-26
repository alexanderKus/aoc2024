def secret(secret):
  mix = lambda x,y: x^y
  prune = lambda x: x%16777216
  step1 = prune(mix(secret*64, secret))
  step2 = prune(mix(step1//32,step1))
  step3 = prune(mix(step2*2048,step2))
  return step3

def one():
  numbers = []
  with open('input.txt','r') as f:
    for line in f.readlines():
      numbers.append(int(line.strip()))
  result = 0
  for number in numbers:
    s = number
    for _ in range(2000):
      s = secret(s)
    result += s
  print(f'result1: {result}')

def two():
  numbers = []
  with open('input.txt','r') as f:
    for line in f.readlines():
      numbers.append(int(line.strip()))
  seqs = dict()
  for number in numbers:
    s = number
    buyer = [s % 10]
    for _ in range(2000):
      s = secret(s)
      buyer.append(s%10)
    seen = set()
    for i in range(len(buyer)-4):
      a,b,c,d,e = buyer[i:i+5]
      seq = (b-a,c-b,d-c,e-d)
      if seq in seen: continue
      seen.add(seq)
      if seq not in seqs: seqs[seq] = 0
      seqs[seq] += e
  print(f'result2: {max(seqs.values())}')

if __name__ == '__main__':
  one()
  two()