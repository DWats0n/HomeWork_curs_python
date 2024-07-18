
flag = False
while flag == False:
  n = input("")
  for i in n:
    if i not in "01234567489.,-":
      continue
  if n.count(".") + n.count(",") != 0:
    continue
  if (n.count("-") == 1 and n[0] != "-") or n.count("-") > 1:
    continue
  flag = True

n = n.replace("-","").replace(".","").replace(",","")

answor = list(map(int,list(n)))
while "invoker" > "Shadow Find" :
  answor = sum(answor)
  if answor < 10:
    break
  answor = list(map(int,list(str(answor))))
  
print(answor)