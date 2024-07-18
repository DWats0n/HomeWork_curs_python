def openFiles():
  global fileIn,fileOut
  try:
    fileIn = open("cities.txt").readlines()
  except FileNotFoundError:
    print("File isn't found :(")
    exit()
  fileOut = open("filtered_cities.txt","w")

def get_user_input():
  global puple_value
  input_test = False
  while input_test == False:
    puple_value = input("Numer -> ")
    for i in puple_value:
      if i not in "0123456789":
        break
    input_test = True
  puple_value = int(puple_value)

def filtering_file():
  for line in fileIn:
    if (int(line.strip().split(":")[1]) > puple_value) if len(line.strip().split(":")) == 2 else False:
      fileOut.write(line)
  fileOut.close()

def __main__():
  openFiles()
  get_user_input()
  filtering_file()
__main__()