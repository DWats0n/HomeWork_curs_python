def step(x,n):
  if x == n:return 1
  if x > n:return 0
  return sum([step(x+1,n),step(x+2,n)])
