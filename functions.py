### FUNCTIONS ###

from classes import bcolors

# at least a or b
def min(a,b):
  if a<b:
    return b
  else:
    return a

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

