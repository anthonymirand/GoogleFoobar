def is_valid(M, F):
  if M % 2 == 0 and F % 2 == 0:
    return False
  if M == F:
    return False
  if M <= 0 or F <= 0:
    return False
  if 1 < M and F % M == 0:
    return False
  if 1 < F and M % F == 0:
    return False
  return True

def answer(M, F):
  try:
    M = long(M); F = long(F)
  except:
    return "impossible"
  generations = 0

  while 1 <= M and 1 <= F:
    if M == 1 and F == 1:
      return str(generations)
    if not is_valid(M, F):
      break
    if M < F:
      if M == 1:
        return str(generations + F - 1)
      difference = F - M
      multiplier = (difference / M) + 1
      generations += multiplier
      F = F - (multiplier * M)
    else: # F <= M
      if F == 1:
        return str(generations + M - 1)
      difference = M - F
      multiplier = (difference / F) + 1
      generations += multiplier
      M = M - (multiplier * F)

  return "impossible"
