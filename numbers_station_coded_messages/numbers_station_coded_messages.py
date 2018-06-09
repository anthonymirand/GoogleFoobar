def answer(l, t):
  for start in xrange(len(l)):
    end = start
    while sum(l[start : end]) < t and end <= len(l):
      end += 1

    if sum(l[start : end]) == t:
      return [ start, end - 1 ]

  return [ -1, -1 ]
