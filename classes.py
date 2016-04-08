# the MONSTER classss !

import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''


class monster():
  def __init__(self,init='random'):
    self.name=''
    self.atk=0
    self.lvl=0
    self.hp=0
    self.hp_max=0

    if (init=='random'):
      self.init_random()

  # random monster stats generator
  def init_random(self):
    vog=['a','e','i','o','u','']
    cons=['b','c','d','f','g','h','j','l','m','x','w','z','']
    adj=['adorable','huggable','flirty','dainty','fuzzy','cutesy','charming','Fluffy','Shiny','Sparkly','Poofy','Lulzy','Chu']
    enemies=['rabbit','lizard','Cthulhu offspring','goblin','Magic Player','Skeleton','Vampire','Ghoul','Ghost','?','Dragon','Fallen Elf','Slime','worm','ice man','fire man','ant','mad time traveler','']
    self.lvl=random.randint(1,7)
    self.name=''.join([random.choice(cons)+random.choice(vog) for n in range(3)])
    self.name=self.name.capitalize()
    if (self.lvl==1 or self.lvl==2 or self.lvl==3):
      self.name=random.choice(adj).capitalize()+" "+random.choice(enemies).capitalize()
    self.atk=self.lvl+random.randint(0,2)
    self.hp=10*self.lvl+random.randint(-self.lvl,2*self.lvl)
    self.hp_max=self.hp

  # calculate the damage from monster
  def blow_dam(self,lvl_hero):
    blow_damage=self.atk+random.randint(0,3)
    if (blow_damage<0):
      blow_damage=0
    return blow_damage

  # show monster profile and stats
  def show_profile(self):
    print " Nome: "+self.name
    print " Lvl: "+str(self.lvl)
    print " ATK: "+str(self.atk)
    print " HP: "+str(self.hp)+"/"+str(self.hp_max)

  # method to take damage
  def take_dam(self,dano):
    self.hp=self.hp-dano

  # check if it is alive
  def isalive(self):
    if self.hp>0:
      return 1
    else:
      return 0

# hero class!
class hero:
  def __init__(self,name,prof_dict):
    self.name=name
    self.profession=prof_dict['name']
    self.lvl=1
    self.lvl_max=len(prof_dict['progression'])
    self.hp=100
    self.hp_max=self.hp
    self.mp=0
    self.xp=0
    self.score=0
    self.atk=0
    self.armor=0
    self.run_chance=0.40
    self.atk=self.lvl+2

    # ugly and dangerous
    exec compile(prof_dict['progression'][0],'<string>','exec')

  # hero take damage
  def take_dam(self,dano):
    if ((dano-self.armor)>0):
      self.hp=self.hp-(dano-self.armor)
      return (dano-self.armor)
    else:
      return "The Hero's armor absorbed the blow!"

  # calculate hero dam to the monster
  def blow_dam(self,lvl_monster):
    blow_damage=self.atk+random.randint(0,3)+random.randint(0,self.lvl/4)
    if (blow_damage<0):
      blow_damage=0
    return blow_damage

  # show profile and stats
  def show_profile(self):
    print " Name: "+self.name
    print " Class: "+self.profession
    print " Lvl: "+str(self.lvl)
    print " ATK: "+str(self.atk)
    print " ARMOR: "+str(self.armor)
    print " RUN%: "+str(self.run_chance)
    print " HP: "+str(self.hp)+"/"+str(self.hp_max)

  # check if it is alive
  def isalive(self):
    if self.hp>0:
      return 1
    else:
      return 0

  # new level, add n levels, update other stats
  def new_lvl(self,n,prog):
    if (self.lvl<self.lvl_max):
      exec compile(prog[self.lvl-1],'<string>','exec')
      self.lvl=self.lvl+n
      print " Hero "+self.name+" passed to level "+str(self.lvl)+"!"
    else:
      print " Hero are already in max level "+str(self.lvl)+"!"
    raw_input(" (enter)")

  def heal(self,p):
    self.hp=self.hp+p
    if (self.hp>self.hp_max):
      self.hp=self.hp_max


