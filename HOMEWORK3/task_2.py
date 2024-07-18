def open_file():
  global fileIn, fileOut
  try:
    fileIn = open("input.txt").readlines()
  except FileNotFoundError:
    print("File isn't found :(")
    exit()
  fileOut = open("output.txt","w")

def get_itmes_from_line(line : str):
  line = line.strip().split(":")
  for x in range(len(line)):
    line[x] = line[x].lower()
    for i in line[x]:
      if i not in "qwertyuiopasdfghjklzxcvbnm1234567890":
        line[x] = line[x].replace(i,"")
  return  line

def do_math_on_numbers():
  global items_sell
  items_sell = {}
  for line in fileIn:
    line_items = get_itmes_from_line(line)
    if (len(line_items) == 2):
      if line_items[0] in items_sell.keys():
        items_sell[line_items[0]] += int(line_items[1])
      else:
        items_sell[line_items[0]] = int(line_items[1])
      
def wright_in_file():
  fileOut.write(str(sum(items_sell.values())))


def __main__():
  open_file()
  do_math_on_numbers()
  wright_in_file()
__main__()