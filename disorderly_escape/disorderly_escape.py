# Using the Polya enumeration theorem, we cam use a formula depending only on
# the size of cycles in permutations of rows or columns:
# https://en.wikipedia.org/wiki/P%C3%B3lya_enumeration_theorem

from operator import mul
from math import factorial
from fractions import gcd
from decimal import Decimal, getcontext
getcontext().prec = 100 # a large number to increase Decimal precision

def successor(values):
  if values[-1] == 1:
    values[:] = [0] * len(values)
    values[0] = len(values)
  else:
    k = values[0]
    i = 1
    while i + 1 > k:
      k += values[i] * (i + 1)
      i += 1
    values[i] += 1
    values[:] = ([0] * i) + values[i:]
    values[0] = k - i - 1
  return None

def sum_gcd(cycle_w, cycle_h):
  return sum(w * h * gcd(i + 1, j + 1)
             for i, w in enumerate(cycle_w) for j, h in enumerate(cycle_h))

def denominator(cycle_w, cycle_h):
  w_part = [ factorial(w) * ((i + 1) ** w) for i, w in enumerate(cycle_w) ]
  h_part = [ factorial(h) * ((j + 1) ** h) for j, h in enumerate(cycle_h) ]
  return reduce(mul, w_part + h_part, 1)

def answer(w, h, s):
  cycle_w = [0] * w; cycle_w[0] = w
  cycle_h = [0] * h; cycle_h[0] = h
  ans = Decimal(0)
  while True:
    G = denominator(cycle_w, cycle_h)
    c_g = sum_gcd(cycle_w, cycle_h)
    ans += Decimal(s ** c_g) / Decimal(G)
    if cycle_w[-1] == 1 and cycle_h[-1] == 1: break
    if cycle_w[-1] == 1: successor(cycle_h)
    successor(cycle_w)
  return str(int(ans))
