def algoritm_evklid(a,b):
  if a==b:
    #print("yes",a)
    return a
  if a < b:
    return algoritm_evklid(a, b-a)
  if a > b:
    return algoritm_evklid(b,a-b)


a = algoritm_evklid(int(input()),int(input()))
print(a)