def answer(l):
  return sorted(l, key=lambda x: [ int(part) for part in x.split('.') ])
