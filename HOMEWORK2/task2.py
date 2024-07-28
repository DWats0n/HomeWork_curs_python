from io import TextIOWrapper

def open_files():
  try:
    file_in = open("input.txt").readlines()
  except FileNotFoundError:
    print("Faile not found")
    exit()
  file_out = open("output.txt","w")
  return file_in, file_out

def get_user_input():
  text = input("wright litras to replace\n->")
  return text

def processing_data(file_in,litras):
  data_out = []
  for line in file_in:
    line = str(line).split(" ")
    text = line[0]
    data_out.append(text)
  return data_out

def wright_in_file_out(file_out : TextIOWrapper,data_out):
  for line in data_out:
    file_out.write(line+"\n")
  file_out.close()

def main():
  file_in, file_out = open_files()
  litras = get_user_input()
  data_out = processing_data(file_in,litras)
  wright_in_file_out(file_out,data_out)
main()
