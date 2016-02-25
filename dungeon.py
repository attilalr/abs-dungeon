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

    if (init=='random'):
      self.init_random()

  # random monster stats generator
  def init_random(self):
    vog=['a','e','i','o','u','']
    cons=['b','c','d','f','g','h','j','l','m','x','w','z','']
    self.lvl=random.randint(1,8)
    self.name=''.join([random.choice(cons)+random.choice(vog) for n in range(3)])+'-'+str(self.lvl)
    self.atk=self.lvl+random.randint(0,2)
    self.hp=min(self.lvl*random.randint(0,3),1)

  # calculate the damage from monster
  def blow_dam(self,lvl_hero):
    blow_damage=self.atk
    if (blow_damage<0):
      blow_damage=0
    return blow_damage

  # show monster profile and stats
  def show_profile(self):
    print " Ficha do monstro:"
    print " Nome: "+self.name
    print " Lvl: "+str(self.lvl)
    print " ATK: "+str(self.atk)
    print " HP: "+str(self.hp)

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
    print " Ficha:"
    print " Nome: "+self.name
    print " Classe: "+self.profession
    print " Lvl: "+str(self.lvl)
    print " ATK: "+str(self.atk)
    print " HP: "+str(self.hp)

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
    print " *** Novo round! ***"
    atq_hero=hero.blow_dam(monster.lvl)
    if atq_hero==0:
      hud_fight(hero,monster,60," O heroi errou o ataque!")
      #print " O heroi errou o ataque!"
    else:
      #print " O heroi provocou "+str(atq_hero)+" pontos de dano!"
      monster.take_dam(atq_hero)
      hud_fight(hero,monster,60," O heroi provocou "+str(atq_hero)+" pontos de dano!")
      
def round_monster(hero,monster):
    atq_monster=monster.blow_dam(hero.lvl)
    if atq_monster==0:
      hud_fight(hero,monster,60," O monstro errou o ataque!")
    else:
      hero.take_dam(atq_monster)
      hud_fight(hero,monster,60," O monstro provocou "+str(atq_monster)+" pontos de dano!")
    
def hud_fight(hero,monster,size_screen,msg):
  print " Hero:"+(size_screen-len(" Hero:")-len("Monster:"))*" "+"Monster:"
  print " "+hero.name+(size_screen-len(msg)-2*len(hero.name+" ")+2)/2*" "+msg+(size_screen-len(msg)-2*len(monster.name))/2*" "+monster.name
  print " Lvl: "+str(hero.lvl)+str((size_screen-len(" Lvl: "+str(hero.lvl))-len("Lvl: "+str(monster.lvl)))*" ")+"Lvl: "+str(monster.lvl)
  print " HP: "+str(hero.hp)+str((size_screen-len(" HP: "+str(hero.hp))-len("HP: "+str(monster.hp)))*" ")+"HP: "+str(monster.hp)


######################## MAIN ###################
print
print "Comeco. Create a hero:"
nome=raw_input("Name: ")

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
  m_idx=random.randint(0,len(m_list)-1) # monstro sorteado
  print " ## Hero's profile ## "
  h.show_profile()
  print " ##### New monster approaches !!! #####"
  m_list[m_idx].show_profile()
  raw_input("(enter)")
  # laco da luta
  while (1):

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

    #print " Hero's HP: "+str(h.hp)
    #print " Monters's HP: "+str(m_list[m_idx].hp)
    raw_input(" (enter for next round!)")

print
print " You survived the dungeon! Congratulations!"
print 
