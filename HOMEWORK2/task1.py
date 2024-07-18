def read_file():
  global file_in, file_out
  try:
    file_in = open("input.txt").readlines()
  except FileNotFoundError:
    print("Dosn't find file :(")
    exit()
  file_out = open("output.txt","w")

def clear_item(line:str):
  line = line.strip().split(",")
  for x in range(1):
    for i in line[x].lower():
      if i not in "qwertyuiopasdfghjklzxcvbnm1234567890":
        line[x] = line[x].replace(i,"")
  return  line

def date_processing():
  m = [int(clear_item(x)[1])  for x in file_in]
  mid_value = sum(m)/len(m)
  for x in file_in:
    if x == "":continue
    if int(clear_item(x)[1]) > mid_value:
      file_out.write(x)

def close_file():
  file_out.close()

def __main__():
  read_file()
  date_processing()
  close_file()
__main__()