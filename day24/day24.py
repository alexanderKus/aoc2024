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
  file = open('input.txt','r')

  for line in file: 
     if line.isspace(): break
  formulas = {}

  for line in file:
    x, op, y, z = line.replace(' -> ', ' ').split()
    formulas[z] = (op, x, y)
  def make_wire(char, num): return char + str(num).rjust(2, '0')

  def verify_z(wire, num):
    nonlocal formulas
    if wire not in formulas: return False
    op, x, y = formulas[wire]
    if op != 'XOR': return False
    if num == 0: return sorted([x, y]) == ['x00', 'y00']
    return verify_intermediate_xor(x, num) and verify_carry_bit(y, num) or verify_intermediate_xor(y, num) and verify_carry_bit(x, num)

  def verify_intermediate_xor(wire, num):
    nonlocal formulas
    if wire not in formulas: return False
    op, x, y = formulas[wire]
    if op != 'XOR': return False
    return sorted([x, y]) == [make_wire('x', num), make_wire('y', num)]

  def verify_carry_bit(wire, num):
    nonlocal formulas
    if wire not in formulas: return False
    op, x, y = formulas[wire]
    if num == 1:
      if op != 'AND': return False
      return sorted([x, y]) == ['x00', 'y00']
    if op != 'OR': return False
    return verify_direct_carry(x, num - 1) and verify_recarry(y, num - 1) or verify_direct_carry(y, num - 1) and verify_recarry(x, num - 1)

  def verify_direct_carry(wire, num):
    nonlocal formulas
    if wire not in formulas: return False
    op, x, y = formulas[wire]
    if op != 'AND': return False
    return sorted([x, y]) == [make_wire('x', num), make_wire('y', num)]

  def verify_recarry(wire, num):
    nonlocal formulas
    if wire not in formulas: return False
    op, x, y = formulas[wire]
    if op != 'AND': return False
    return verify_intermediate_xor(x, num) and verify_carry_bit(y, num) or verify_intermediate_xor(y, num) and verify_carry_bit(x, num)

  def verify(num): return verify_z(make_wire('z', num), num)
  def progress():
    i = 0
    while True:
      if not verify(i): break
      i += 1
    return i

  swaps = []
  for _ in range(4):
    baseline = progress()
    for x in formulas:
      for y in formulas:
        if x == y: continue
        formulas[x], formulas[y] = formulas[y], formulas[x]
        if progress() > baseline:
            break
        formulas[x], formulas[y] = formulas[y], formulas[x]
      else:
          continue
      break
    swaps += [x, y]
  print('result2: ' + ','.join(sorted(swaps)))

if __name__ == '__main__':
  one()
  two()