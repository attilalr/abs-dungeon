#!/usr/bin/python

import random,sys, os

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

### FUNCTIONS ###

def round_hero(hero,monster,s):
    atq_hero=hero.blow_dam(monster.lvl)
    if atq_hero==0:
      hud_fight(hero,monster,s," Hero missed the attack!")
    else:
      monster.take_dam(atq_hero)
      hud_fight(hero,monster,s," Hero inflicted "+str(atq_hero)+" damage points!")
      
def round_monster(hero,monster,s):
    atq_monster=monster.blow_dam(hero.lvl)
    if atq_monster==0:
      hud_fight(hero,monster,s," Monster missed the attack!")
    else:
      damage=hero.take_dam(atq_monster)
      if (type(damage)==type(1)):
        hud_fight(hero,monster,s," The monster inflicted "+str(atq_monster)+"-"+str(hero.armor)+"="+str(damage)+" damage points!")
      else:
        hud_fight(hero,monster,s,damage)

    
def hud_fight(hero,monster,size_screen,msg):
  print_lmr(" Hero:","","Monster:","","","",bcolors.ENDC,size_screen)
  print_lmr(" "+hero.name,msg,monster.name,"",bcolors.OKGREEN,"",bcolors.ENDC,size_screen)
  print " Lvl: "+str(hero.lvl)+str((size_screen-len(" Lvl: "+str(hero.lvl))-len("Lvl: "+str(monster.lvl)))*" ")+"Lvl: "+str(monster.lvl)
  print " HP: "+str(hero.hp)+'/'+str(hero.hp_max)+str((size_screen-len(" HP: "+str(hero.hp)+'/'+str(hero.hp_max))-len("HP: "+str(monster.hp)+'/'+str(monster.hp_max)))*" ")+"HP: "+str(monster.hp)+'/'+str(monster.hp_max)

def print_m(msg,color,colorend,s_size):
  print color+" "*(s_size/2-len(msg)/2)+msg+colorend

def print_lmr(msgl,msgm,msgr,colorl,colorm,colorr,colorend,s_size):
  print colorl+" "+msgl+" "*(s_size/2-len(msgm)/2-len(msgl)-1)+colorm+msgm+" "*(s_size/2-len(msgr)-len(msgm)/2-1)+colorend

######################## MAIN ###################
try:
  rows, columns = os.popen('stty size', 'r').read().split()
except:
  print " Something went wrong when getting terminal size."
  sys.exit(0) 
size_screen=int(columns)

print
print bcolors.FAIL+" The beginning. Bla Bla Bla everybody is counting on you"+bcolors.ENDC
print bcolors.FAIL+" to rid this evil from our village."+bcolors.ENDC
print
print " Create a hero:"
nome=raw_input(" Name: ")

scoundrel_dict={'name':'Scoundrel','description':'The scoundrel have 70% chance of fleeing a fight.','progression':['self.atk=self.atk+1; self.run_chance=0.70','self.atk=self.atk+1; self.armor=self.armor+1','self.atk=self.atk+1','self.atk=self.atk+1; self.armor=self.armor+1','self.atk=self.atk+1','self.atk=self.atk+1','self.atk=self.atk+1','self.atk=self.atk+1; self.armor=self.armor+1','self.atk=self.atk+1','self.atk=self.atk+1']}
fighter_dict={'name':'Fighter','description':'The fighter class gives 3 points of armor.','progression':['self.atk=self.atk+1; self.armor=self.armor+2','self.atk=self.atk+1; self.armor=self.armor+1','self.atk=self.atk+1','self.atk=self.atk+1; self.armor=self.armor+1','self.atk=self.atk+1','self.atk=self.atk+1','self.atk=self.atk+1','self.atk=self.atk+1; self.armor=self.armor+1']}

## CLASS SELECTION ##
class_list=[fighter_dict,scoundrel_dict]
for i,j in zip(range(len(class_list)),class_list):
  print " "+str(i)+": "+j['name']
prof=raw_input(" Choose class:")
while (prof.isdigit()==False or prof not in [str(i) for i in range(0,len(class_list))]):
  prof=raw_input(" Choose class:")
prof=int(prof)
print_m(class_list[prof]['description'],bcolors.OKBLUE,bcolors.ENDC,size_screen)

# hero instance
h=hero(nome,class_list[int(prof)])
h.show_profile()

raw_input(" (enter)")

# monster list creation
m_list=list()
for i in range(20):
  m_list.append(monster())

while (len(m_list)!=0):
  print
  print_m(" There is "+str(len(m_list))+" monsters yet in the dungeon.",bcolors.WARNING,bcolors.ENDC,size_screen)
  print
  m_idx=random.randint(0,len(m_list)-1) # pick a monster
  print bcolors.OKBLUE+" ## Hero's profile ## "+bcolors.ENDC
  h.show_profile()
  print_m(" ##### New monster approaches !!! #####",bcolors.FAIL,bcolors.ENDC,size_screen)

  m_list[m_idx].show_profile()
  # fight loop
  while (1):

    choice=raw_input(" (enter to fight, r to try to run)")
    print h.run_chance
    if (choice=='r' and random.random()<h.run_chance):
      print
      print_m(" *** Hero have sucessfully fled from battle! *** ",bcolors.OKBLUE,bcolors.ENDC,size_screen)
      print_m(" Monster's life replenished!",bcolors.OKBLUE,bcolors.ENDC,size_screen)
      m_list[m_idx].hp=m_list[m_idx].hp_max
      break
    elif (choice=='r'):
      print
      print_m(" *** Hero haven't sucessfully fled from battle! *** ",bcolors.WARNING,bcolors.ENDC,size_screen)
      print_m("Monster is attacking!",bcolors.WARNING,bcolors.ENDC,size_screen)
      round_monster(h,m_list[m_idx],size_screen)
      if (h.isalive()==0):
        print
        print " Our hero "+h.name+" is dead! Game over!"
        sys.exit(0)
      continue

    print bcolors.WARNING+" "*(size_screen/2-len(" *** New round! ***")/2)+" *** New round! ***"+bcolors.ENDC
    round_hero(h,m_list[m_idx],size_screen)
    if (m_list[m_idx].isalive()==0):
      print
      print bcolors.WARNING+" Monster "+m_list[m_idx].name+" was slain! Congratulations!"+bcolors.ENDC

      ## score update section
      if ((h.lvl-m_list[m_idx].lvl)>5):
        score_adj=(m_list[m_idx].lvl*100)*(-1)/2
      else:
        score_adj=(-h.lvl+m_list[m_idx].lvl)*(m_list[m_idx].lvl*100)/5
      score_gained=m_list[m_idx].lvl*100+score_adj
      h.score=h.score+score_gained
      print bcolors.WARNING+" Gained "+str(score_gained)+" points."+bcolors.ENDC
      if (score_adj>0):
        print bcolors.WARNING+" (Extra "+str(score_adj)+" points for the challenge!)"+bcolors.ENDC
      if (score_adj<0):
        print bcolors.WARNING+" (Penality of "+str(abs(score_adj))+" points for kicking the dead dog.)"+bcolors.ENDC

      ## healing
      healing=random.randint(8,8+h.lvl)
      print bcolors.OKBLUE+" Hero cured for "+str(healing)+" hitpoints!."+bcolors.ENDC

      h.new_lvl(1,class_list[int(prof)]['progression'])
      h.heal(healing)
      del m_list[m_idx]
      raw_input(" (enter)")
      break #sai da luta

    print " *"
    round_monster(h,m_list[m_idx],size_screen)
    if (h.isalive()==0):
      print
      print " Our hero "+h.name+" is dead! Game over!"
      print " Score: "+str(h.score)
      print
      sys.exit(0)

    raw_input(" (enter for next round!)")

print
print " You survived the dungeon! Congratulations!"
print " Score: "+str(h.score)
print 
