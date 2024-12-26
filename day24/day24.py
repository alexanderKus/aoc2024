def op(gate, w1,w2):
  if gate == 'AND': return w1 & w2
  if gate == 'OR':  return w1 | w2
  if gate == 'XOR': return w1 ^ w2

def e(lookup,name):
  value = lookup[name]
  if isinstance(value,int): return value
  w1,g,w2 = value   
  if len(w1) > 1: e(lookup,w1)
  if len(w2) > 1: e(lookup,w2)
  lookup[name] = op(g,lookup[w1],lookup[w2])

def one():
  wires_states = dict()
  with open('input.txt','r') as f:
    data = f.read()
    initial, conns = data.split('\n\n')
  for state in initial.split('\n'):
    w,s = state.strip().split(': ')
    wires_states[w] = int(s)
  for conn in conns.split('\n'):
    w1,gate,w2,_,w3 = conn.strip().split(' ')
    wires_states[w3] = (w1,gate,w2)
  for wire in wires_states:
    if wire.startswith('z'): e(wires_states,wire)
  z_states = dict()
  for k,v in wires_states.items():
    if k.startswith('z'):
      z_states[k] = v
  number = 0
  for i,(k,val) in enumerate(sorted(z_states.items())):
    number += val << i
  print(f'result1: {number}')


def two():
  ...

if __name__ == '__main__':
  one()
  two()