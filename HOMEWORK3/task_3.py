def read_file():
  global data_file
  try:
    data_file = open("input.txt").readlines()
  except FileNotFoundError:
    print("Don't finded file :(")
    exit()

def clear_items(line:str):
  line = line.strip().split(":") + line.strip().split(":")[1].split(",")
  for x in range(len(line)):
    line[x] = line[x].lower()
    if line[x] == "":
      line = line[:x:]
      continue
    for i in line[x]:
      if i not in "qwertyuiopasdfghjklzxcvbnm1234567890":
        line[x] = line[x].replace(i,"")
  return line

def date_processing():
  global stadis_name
  stadis_name = {}
  for line in data_file:
    information = clear_items(line)
    for item in range(1,len(information)):
      if information[item] in stadis_name.keys():
        stadis_name[information[item]] += \
          f", {information[0]}" \
            if information[0] not in stadis_name[information[item]] \
              else ""
      else:
        stadis_name[information[item]] = information[0]

def interaction_whis_user():
  #input_text = "Wright stude to find studentions or\n Press Enter to exit...\n"
  input_text = ""
  text = input(input_text).lower()
  while text != "":
    if text in stadis_name.keys():
      print(stadis_name[text])
    else:
      print("dosn't have this stude")
    text = input(input_text).lower()

def __main__():
  read_file()
  date_processing()
  interaction_whis_user()
__main__()