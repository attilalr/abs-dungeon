#!/usr/bin/python

import random,sys

# at least a or b
def min(a,b):
  if a<b:
    return b
  else:
    return a

# the MONSTER classss !
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
    self.lvl=random.randint(1,8)
    self.name=''.join([random.choice(cons)+random.choice(vog) for n in range(3)])+'-'+str(self.lvl)
    self.atk=self.lvl+random.randint(0,2)
    self.hp=min(10+self.lvl*random.randint(0,3),10)
    self.hp_max=self.hp

  # calculate the damage from monster
  def blow_dam(self,lvl_hero):
    blow_damage=self.atk+random.randint(0,3)
    if (blow_damage<0):
      blow_damage=0
    return blow_damage

  # show monster profile and stats
  def show_profile(self):
    print " Monster profile:"
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
  def __init__(self,name):
    self.name=''
    self.profession='fighter'
    self.lvl=1
    self.hp=100
    self.hp_max=self.hp
    self.mp=0
    self.xp=0
    self.atk=0

    self.init_hero(name)

  def init_hero(self,name):
    self.name=name
    self.atk=self.lvl

  # hero take damage
  def take_dam(self,dano):
    self.hp=self.hp-dano

  # calculate hero dam to the monster
  def blow_dam(self,lvl_monster):
    blow_damage=self.atk
    if (blow_damage<0):
      blow_damage=0
    return blow_damage

  # show profile and stats
  def show_profile(self):
    print " Hero's profile:"
    print " Name: "+self.name
    print " Class: "+self.profession
    print " Lvl: "+str(self.lvl)
    print " ATK: "+str(self.atk)
    print " HP: "+str(self.hp)+"/"+str(self.hp_max)

  # check if it is alive
  def isalive(self):
    if self.hp>0:
      return 1
    else:
      return 0

  # new level, add n levels, update other stats
  def new_lvl(self,n):
    self.lvl=self.lvl+n
    print " Hero "+self.name+" passed to "+str(self.lvl)+" level!"
    self.atk=self.atk+random.randint(1,3)

def round_hero(hero,monster):
    print " *** New round! ***"
    atq_hero=hero.blow_dam(monster.lvl)
    if atq_hero==0:
      hud_fight(hero,monster,60," Hero missed the attack!")
    else:
      monster.take_dam(atq_hero)
      hud_fight(hero,monster,60," Hero inflicted "+str(atq_hero)+" damage points!")
      
def round_monster(hero,monster):
    atq_monster=monster.blow_dam(hero.lvl)
    if atq_monster==0:
      hud_fight(hero,monster,60," Monster missed the attack!")
    else:
      hero.take_dam(atq_monster)
      hud_fight(hero,monster,60," The monster inflicted "+str(atq_monster)+" damage points!")
    
def hud_fight(hero,monster,size_screen,msg):
  print " Hero:"+(size_screen-len(" Hero:")-len("Monster:"))*" "+"Monster:"
  print " "+hero.name+(size_screen-len(msg)-2*len(hero.name+" ")+2)/2*" "+msg+(size_screen-len(msg)-2*len(monster.name))/2*" "+monster.name
  print " Lvl: "+str(hero.lvl)+str((size_screen-len(" Lvl: "+str(hero.lvl))-len("Lvl: "+str(monster.lvl)))*" ")+"Lvl: "+str(monster.lvl)
  print " HP: "+str(hero.hp)+'/'+str(hero.hp_max)+str((size_screen-len(" HP: "+str(hero.hp)+'/'+str(hero.hp_max))-len("HP: "+str(monster.hp)+'/'+str(monster.hp_max)))*" ")+"HP: "+str(monster.hp)+'/'+str(monster.hp_max)


######################## MAIN ###################
print
print " The beginning. Bla Bla Bla everybody is counting on you"
print " to rid this evil from our village."
print
print " Create a hero:"
nome=raw_input(" Name: ")

size_screen=60

# hero instance
h=hero(nome)
h.show_profile()

# monster list creation
m_list=list()
for i in range(10):
  m_list.append(monster())

while (len(m_list)!=0):
  print
  print " There is "+str(len(m_list))+" monsters yet in the dungeon."
  print
  m_idx=random.randint(0,len(m_list)-1) # pick a monster
  print " ## Hero's profile ## "
  h.show_profile()
  print " ##### New monster approaches !!! #####"
  m_list[m_idx].show_profile()
  # fight loop
  while (1):

    if (raw_input(" (enter to fight, r to try to run)")=='r' and random.random()<0.5):
      print " *** Hero have sucessfully fled from battle! *** "
      print " Monster's life replenished!"
      print
      m_list[m_idx].hp=m_list[m_idx].hp_max
      break

    round_hero(h,m_list[m_idx])
    if (m_list[m_idx].isalive()==0):
      print
      print " Monster "+m_list[m_idx].name+" was slain! Congratulations!"
      h.new_lvl(1)
      del m_list[m_idx]
      raw_input(" (enter)")
      break #sai da luta

    print " *"
    round_monster(h,m_list[m_idx])
    if (h.isalive()==0):
      print
      print " Our hero "+h.name+" is dead! Game over!"
      sys.exit(0)

    raw_input(" (enter for next round!)")

print
print " You survived the dungeon! Congratulations!"
print 
