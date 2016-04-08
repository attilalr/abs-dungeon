#!/usr/bin/python

from classes import *
from functions import *

import random,sys, os

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

# main loop
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
