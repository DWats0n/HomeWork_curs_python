

def open_files():
  global file_in_1, file_in_2, file_out
  try:
    file_in_1 = open("input1.txt").readlines()
    file_in_2 = open("input2.txt").readlines()
  except FileNotFoundError:
    print("Find file haven't been finding :(")
    exit()
  file_out = open("output.txt","w")

def add_linse():
  pass

def close_file():
  pass

def __main__():
  open_files()
  add_linse()
  close_file()
  
__main__()