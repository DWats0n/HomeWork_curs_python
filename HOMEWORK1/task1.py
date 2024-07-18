def get_user_in():
  global n
  flag = False
  while flag == False:
    n = input()
    flag = True
    for i in n:
      if i not in "0123456789":
        flag == False
        break
  n = int(n)
  
def user_in_procassing():
  for i in range(n-1):
    print(" " * (n-i) + "*" * (i * 2 + 1) )

def __main__():
  get_user_in()
  user_in_procassing()

__main__()