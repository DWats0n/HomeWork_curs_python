flag = False
while flag == False:
  n = input("")
  if len(n) > 3 or len(n) == 0:
    continue
  for i in n:
    if n not in "0123456789":
      continue
  if n[0] == "0":
    continue
  flag = True

#n = random.randint(1,999)
n = ["0"] * (3 - len(list(str(n)))) + list(str(n))
#print(n)
worder = {
  "1":"один",
  "2":"два",
  "3":"три",
  "4":"четыре",
  "5":"пять",
  "6":"шесть",
  "7":"семь",
  "8":"восемь",
  "9":"девять",
  "10":"десять",
  "11":"одинатсать",
  "12":"двенадцать",
  "13":"тренадцать",
  "14":"четырнадцать",
  "15":"пятнадцать",
  "16":"шестнадцать",
  "17":"семнадцать",
  "18":"восемнадцать",
  "19":"деветнадцать",
  "20":"дватцать",
  "30":"тридцать",
  "40":"сорок",
  "50":"пятьдесят",
  "60":"шестьдесять",
  "70":"семьдесать",
  "80":"восемдесят",
  "90":"девяносто",
  "100":"сто",
  "200":"двести",
  "300":"триста",
  "400":"четыресто",
  "500":"пятьсот",
  "600":"шестьсот",
  "700":"семьсот",
  "800":"восемьсот",
  "900":"девятсот"}

answer = ""

if n[0] != "0":
  answer += worder[str(n[0]+"00")] + " "

if n[1] != "0":
  if n[1] + n[2] in "10,11,12,13,14,15,16,17,18,19":
    answer += worder[n[1]+n[2]]+ " "
  else:
    answer += worder[n[1]+"0"] + " "
    if n[2] != "0":
      answer += worder[n[2]]
else:
  if n[2] != "0":
    answer += worder[n[2]]
print(answer)
