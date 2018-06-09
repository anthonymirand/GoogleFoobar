def answer(n):
  fuel = int(n)
  total = 0

  while 1 < fuel:
    if fuel % 2 == 0:
      fuel //= 2
    # 3 can be hard-coded to go to 2 instead of 4
    elif fuel == 3:
      fuel -= 1
    # change current value to nearest power of two
    elif (fuel >> 1) & 1 == 0:
      fuel -= 1
    else:
      fuel += 1
    total += 1

  return total
