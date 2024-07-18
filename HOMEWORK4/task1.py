
def open_files():
  global lines,file_output
  try:
    lines = open("input.txt").readlines()
  except FileNotFoundError:
    print("File found Error")
    exit()
  file_output = open("output.txt","w")


def procedura(line):
  target = ""
  open_lit = "({[<"
  close_lit = ")}]>"
  perehod = {"(":")","{":"}","[":"]","<":">"}
  for litra in line:
    if litra in open_lit:
      target += perehod[litra]
    elif litra in close_lit:
      if target == "":
        return "False"
      if litra != target[-1]:
        return "False"
      else:
        target = target[:-1]
  return "True"

def data_processing():
  global answer
  answer = []
  for line in lines:
    line = line.strip().replace(" ","")
    answer.append(procedura(line))
  pass

def wright_and_close_files():
  file_output.write("\n".join(answer))
  file_output.close()


def main():
  open_files()
  data_processing()
  wright_and_close_files()

main()