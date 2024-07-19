import random
import math


class settings:
  eatWay = ["Hunter","Peaceful"]
  group = {
    "1":"Earth",
    "2":"Earth",
    "3":"Earth",
    "4":"Earth",
    "5":"Water",
    "6":"Water",
    "7":"Water",
    "8":"Air",
    "9":"Air",
    "10":"Air",
    "11":"Air",
    "12":"Air"}
  sex = ["male", "female"]
  size = (1,5)
  liveTime = (15,50)

class World:
  
  def __init__(self, countOfOrganicEat):
    self.listOfAnimal = []
    self.countOfOrganicEat = countOfOrganicEat
    pass

  def getEat(self,nameOfEat):
    if nameOfEat == "OrganicEat":
      return self.countOfOrganicEat
    elif nameOfEat in settings.group:
      for animel in self.listOfAnimal:
        animel:Animale
        if animel.getName():
          return animel
      return 0
    else:
      return 0

  def addOrganicEat(self, count):
    self.countOfOrganicEat += count

  def getCountOfAnimalse(self):
    return len(self.listOfAnimal)
  
  def addNewAnimal(self):
    animal:Animale
    eatWay = random.choice(settings.eatWay)
    group_id = random.randint(0,len(settings.group)-1)
    grope = (list(settings.group.keys())[group_id],list(settings.group.values())[group_id])
    if eatWay == settings.eatWay[0]:
      animal = Hunter(
        grope[0],
        random.randint(settings.size[0],settings.size[1]),
        random.choice(settings.sex),
        random.choice(list(settings.group.keys())),
        grope[1],
        random.randint(settings.liveTime[0],settings.liveTime[1]),
        100)
    else:
      animal = Peaceful(
        grope[0],
        random.randint(settings.size[0],settings.size[1]),
        random.choice(settings.sex),
        "OrganicEat",
        grope[1],
        random.randint(settings.liveTime[0],settings.liveTime[1]),
        100)
    self.listOfAnimal.append(animal)

  def addAnumalWithSetting(self, name,size, livingPlace,hunger):

    if livingPlace == settings.eatWay[0]:
      animal = Hunter(
        name,
        random.randint(1,size),
        random.choice(settings.sex),
        random.choice(list(settings.group.keys())),
        livingPlace,
        random.randint(settings.liveTime[0],settings.liveTime[1]),
        hunger)
    else:
      animal = Peaceful(
        name,
        random.randint(1,size),
        random.choice(settings.sex),
        "OrganicEat",
        livingPlace,
        random.randint(settings.liveTime[0],settings.liveTime[1]),
        hunger)
    self.listOfAnimal.append(animal)

  def getCountOfOrganikFood(self):
    return self.countOfOrganicEat
  
  def doMultiplay(self):
    partners = {}
    maxN = 0
    print("Ruler:\nfor Earth - hunger >= 20%, age >= 5\nfor Air - hunger >= 40%, age >= 3\nfor Water - hunger >= 10")
    for i in range(len(self.listOfAnimal)):
      partners[i+1] = self.listOfAnimal[i]
      animal = self.listOfAnimal[i]
      animal:Animale
      print(f"{i+1})Name:{animal.getName()},Age: {animal.getAge()},Livilng Place: {animal.getLivingPlace()},Sex: {animal.getSex()},Hunger:{animal.getHunger()}")
      maxN = i+1
    flag = False
    while flag == False:
      user_text = input("print number of animals (in format - NNxNN)\n-> ")
      numbres = user_text.split("x")
      if len(numbres) != 2:
        continue
      for number in numbres:
        for litra in number:
          if litra not in "0123456789":
            continue
      if max(list(map(int,numbres))) > maxN+1:
        continue
      flag=True
    numbres = list(map(int,numbres))
    p1, p2 = partners[numbres[0]],partners[numbres[1]]
    p1:Animale
    p2:Animale
    if numbres[0] == numbres[1]:
      print("animal did very strange fap :)")
    elif p1.getSex() == p2.getSex():
      print("there are only two genders -_-")
    elif p1.getLivingPlace() != p2.getLivingPlace():
      print("they belong to different worlds")
    elif p1.getName() != p2.getName():
      print("they try, but nothing went wrong.")
    elif p1.getLivingPlace() == "Earth":
      if p1.getHunger() >= 20 and p2.getHunger()>= 20 and p1.getAge() >= 5 and p2.getAge() >= 5:
        for i in range(2):
          self.addAnumalWithSetting(p1.getName(),max(p1.getSize(),p2.getSize()),p1.getLivingPlace(),73)
      else:
        print("Rules don't have been ready")

    elif p1.getLivingPlace() == "Water":
      if p1.getHunger() >= 10 and p2.getHunger()>= 10:
        for i in range(10):
          self.addAnumalWithSetting(p1.getName(),max(p1.getSize(),p2.getSize()),p1.getLivingPlace(),23)
      else:
        print("Rules don't have been ready")
    elif p1.getLivingPlace() == "Air":
      if p1.getHunger() >= 40 and p2.getHunger()>= 40 and p1.getAge() >= 3 and p2.getAge() >= 3:
        for i in range(4):
          self.addAnumalWithSetting(p1.getName(),max(p1.getSize(),p2.getSize()),p1.getLivingPlace(),64)
      else:
        print("Rules don't have been ready")
  
  def animeDead(self, animel):
    for anime_id in range(len(self.listOfAnimal)):
      if self.listOfAnimal[anime_id] == animel:
        animel:Animale
        self.countOfOrganicEat += animel.getSize()
        self.listOfAnimal = self.listOfAnimal[:anime_id]+self.listOfAnimal[anime_id+1:]
        break

  def animelWasEating(self, animel):
    
    for anime_id in range(len(self.listOfAnimal)):
      if self.listOfAnimal[anime_id] == animel:
        self.listOfAnimal = self.listOfAnimal[:anime_id]+self.listOfAnimal[anime_id+1:]
        break

  def getListOfAnimal(self):
    return self.listOfAnimal

class Animale:

  def __init__(self, name,size, sex, typeOfeat, livingPlace, liveTime,hunger):
    self.name = name
    self.size = size
    self.typeOfeat = typeOfeat
    self.livingPlace = livingPlace
    self.liveTime = liveTime
    self.hunger = hunger
    self.sex = sex
    self.age = 0
    
  def getHunger(self):
    return self.hunger
  
  def getAge(self):
    return self.age
  
  def getInfo(self):
    return f"name: {self.name},age:{self.age}, hunger:{self.hunger}, eat:{self.typeOfeat}"
  
  def getName(self):
    return self.name
  
  def getSize(self):
    return self.size
  
  def _addHunger(self,hunger):
    self.hunger = self.hunger + hunger if self.hunger + hunger <= 100 else 100

  def stepLive(self, world:World):
    self.age += 1
    if self.age == self.liveTime:
      world.animeDead(self)
    if self.hunger < 10:
      world.animeDead(self)

  def getLivingPlace(self):
    return self.livingPlace

  def getSex(self):
    return self.sex

class Hunter(Animale):
  def stepLive(self, world:World):
    eat = world.getEat(self.typeOfeat)
    if eat != 0:
      eat : Animale
      if random.randint(0,1) >= 0.5:
        self._addHunger(53)
        world.animelWasEating(eat)
      else:
        self._addHunger(-16)
    else:
      self._addHunger(-9)
    
    super().stepLive(world)
    
class Peaceful(Animale):
  def stepLive(self, world:World):
    if world.getEat(self.typeOfeat) != 0:
      self._addHunger(26)
      world.addOrganicEat(-1)
    else:
      self._addHunger(-9)

    super().stepLive(world)

def spawnFirstAnimals(world : World ,count):
  for i in range(count):
    world.addNewAnimal()
  watchInfoByAllAnimals(world)

def addAnime(world : World):
  world.addNewAnimal()
  pass

def increaseCountOfEat(world : World):
  flag = False
  while flag == False:
    count = input("How mach add -> ")
    if count == "":
      continue
    flag = True
    for i in count:
      if i not in "0123456789":
        flag = False
  count = int(count)
  world.addOrganicEat(count)

def watchInfoByAllAnimals(world : World):
  worder = {"Earth":0, "Water":1, "Air":2}
  itmes = [[],[],[]]
  for animal in world.getListOfAnimal():
    animal:Animale
    itmes[worder[animal.getLivingPlace()]].append(animal)
  for place in worder.keys():
    print( "-----"+place + "-----")
    for animal in itmes[worder[place]]:
      animal:Animale
      print(animal.getInfo())
  print("-------------")
  print(f"All animals:{world.getCountOfAnimalse()}\nCount of organik food: {world.getCountOfOrganikFood()}" )

def modelingProcassOfMultiply(world : World):
  world.doMultiplay()
  print()

def playerMove(world : World, text):
  startNextDay = False
  while startNextDay == False:
    move = input(text)
    if move == "1": #1)Add new animal
      addAnime(world)
    elif move == "2":#2)increase count of eat
      increaseCountOfEat(world)
    elif move == "3":#3)Watch info by all animals
      watchInfoByAllAnimals(world)
    elif move == "4":#4)Modeling procass of multiply
      modelingProcassOfMultiply(world)
    elif move == "5":
      startNextDay = True
      break
    elif move == "6":
      exit()
    else:
      print("\n-----------------\nComanda not found\n-----------------\n")
  pass

def AddstepLive(world:World):
  for animal in world.getListOfAnimal():
    animal:Animale
    animal.stepLive(world)
  
def main():

  world = World(10)
  spawnFirstAnimals(world,10)
  while True:
    playerMove(world,"what do you want to do?\n1)Add new animal\n2)increase count of eat\n3)watch info by all animals\n4)Modeling procass of multiply\n5)Go to next day\n6)Exit\n-> ")
    AddstepLive(world)

main()
