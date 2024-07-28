from io import TextIOWrapper

def open_files():
  try:
    file_in_1 = open("input1.txt").readlines()
    file_in_2 = open("input2.txt").readlines()
  except FileNotFoundError:
    print("Find file haven't been finding :(")
    exit()
  file_out = open("output.txt","w")
  return file_in_1,file_in_2,file_out

def add_linse(file_in_1,file_in_2):
  list_out = []
  
  for id in range(len(file_in_1)):
    list_out.append( str(file_in_1[id]).strip() + " " + str(file_in_2[id]).strip() )

  return list_out

def close_file(file_out : TextIOWrapper,list_out):
  for line in list_out:
    file_out.write(line+"\n")
  file_out.close()

def __main__():
  file_in_1,file_in_2,file_out = open_files()
  list_out = add_linse(file_in_1,file_in_2)
  close_file(file_out,list_out)
  
__main__()
