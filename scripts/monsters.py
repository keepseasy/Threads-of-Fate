import math, glob, os
from genLib import getName as sortKey
from genLib import genProps
from genLib import genSize
from genLib import bookmark
from genLib import makelink
from genLib import pureGen
#from monsters_weapons import genLine
from genLib import getDict

def genPimaryMod(val):
 mod=math.floor((val-10)/2)
 outStr='('
 if mod>=0:
  outStr+='+'
 return outStr+str(mod)+')'

class heroStats:
  STR=None
  DEX=None
  CON=None
  INT=None
  WIS=None
  CHA=None
  PHE=None
  SIZE=None
  HP=None
  SPD=None
  REF=None
  ENG=None
  WIL=None
  DEF=None
  LIM=None
  TREADS=None
  WEP=None
  UNA=None
  ACC=None
  def setPhe(self,entity):
   if 'Феноменальная характеристика' not in entity:
    return
   match entity.get('Феноменальная характеристика'):
    case 'Сила' : self.PHE=self.STR
    case 'Ловкость' : self.PHE=self.DEX
    case 'Выносливость' : self.PHE=self.CON
    case 'Интеллект' : self.PHE=self.INT
    case 'Мудрость' : self.PHE=self.WIS
    case 'Обаяние' : self.PHE=self.CHA

  def __init__(self,entity):
   self.STR=entity.get('Сила',-1)
   self.DEX=entity.get('Ловкость',-1)
   self.CON=entity.get('Выносливость',-1)
   self.INT=entity.get('Интеллект',-1)
   self.WIS=entity.get('Мудрость',-1)
   self.CHA=entity.get('Обаяние',-1)
   self.setPhe(entity)

   self.SIZE=entity.get('Размер',0)
   self.HP=entity.get('ЕЗ',0)
   self.SPD=entity.get('Скорость',0)
   self.REF=entity.get('Реакция',0)
   self.ENG=entity.get('Энергия',0)
   self.WIL=entity.get('Воля',0)

   self.DEF=int(entity.get('Бонус защиты',0))
   self.LIM=entity.get('Ограничение ловкости')
   self.TREADS=entity.get('Нити')
   self.WEP=entity.get('Владение оружием',0)
   self.UNA=entity.get('Рукопашный бой',0)
   self.ACC=entity.get('Стрельба',0)

def calculateSecondary(hero,doubleSpeed):
 hero.HP+=(hero.SIZE+3)*hero.CON
 hero.SPD+=math.floor((hero.DEX+hero.CON)/4)+hero.SIZE
 if doubleSpeed:
  hero.SPD*=2
 hero.REF+=math.floor((hero.DEX+hero.WIS)/4)
 hero.ENG+=math.floor((hero.CON+hero.CHA)/4)
 hero.WIL+=math.floor((hero.INT+hero.WIS)/4)
 DEX_BONUS=math.floor((hero.DEX-10)/2)
 if hero.LIM is None:
  hero.LIM=DEX_BONUS
 elif hero.LIM>DEX_BONUS:
  hero.LIM=DEX_BONUS
 hero.DEF+=10+hero.LIM-hero.SIZE

 return hero

def genEntity(entityDict):
# originWeapons=getWeapons()
# originPowers=getPowers()
 originPerks=getPerks()

 outStr=''
 for key in entityDict:
  entity=entityDict.get(key)

  template='Шаблон' in entity
  hero=heroStats(entity)
  if not template:
   hero=calculateSecondary(hero,'Четвероногое' in entity)

  outStr+='\\subsection{'+key+'}'
  outStr+=bookmark(key,'monster')
  outStr+=entity.get('описание','\\err нет описания')

  outStr+='\\begin{longtable}{l l l l l l l l l l}'
  outStr+='\\textbf{Сл:}'
  outStr+=' & '+str(hero.STR)
  if not template:
   outStr+=genPimaryMod(hero.STR)
  outStr+=' & \\textbf{Ин:}'
  outStr+=' & '+str(hero.INT)
  if not template:
   outStr+=genPimaryMod(hero.INT)
  outStr+=' & \\textbf{Скорость:}'
  outStr+=' & '+str(hero.SPD)
  outStr+=' & \\textbf{ЕЗ:}'
  outStr+=' & '+str(hero.HP)
  if template:
   outStr+=' & '
   outStr+=' & '
  else:
   outStr+=' & \\textbf{Размер:}'
   outStr+=' & '+genSize(hero.SIZE)
  outStr+='\\\\'

  outStr+='\\textbf{Лв:}'
  outStr+=' & '+str(hero.DEX)
  if not template:
   outStr+=genPimaryMod(hero.DEX)
  outStr+=' & \\textbf{Мд:}'
  outStr+=' & '+str(hero.WIS)
  if not template:
   outStr+=genPimaryMod(hero.WIS)
  outStr+=' & \\textbf{Реакция:}'
  outStr+=' & '+str(hero.REF)
  outStr+=' & \\textbf{Энергия:}'
  outStr+=' & '+str(hero.ENG)
  outStr+=' & \\textbf{Защита:}'
  outStr+=' & '+str(hero.DEF)
  outStr+='\\\\'

  outStr+='\\textbf{Вн:}'
  outStr+=' & '+str(hero.CON)
  if not template:
   outStr+=genPimaryMod(hero.CON)
  outStr+=' & \\textbf{Об:}'
  outStr+=' & '+str(hero.CHA)
  if not template:
   outStr+=genPimaryMod(hero.CHA)
  outStr+=' & \\textbf{Воля:}'
  outStr+=' & '+str(hero.WIL)
  outStr+=' & \\textbf{Нити:}'
  outStr+=' & '+hero.TREADS
  outStr+=' & '
  outStr+=' & '
  outStr+='\\\\'
  outStr+='\\end{longtable}'

  outStr+='\\textbf{Атаки}'
  if 'атаки' in entity:
   attacks=entity.get('атаки')
   outStr+='\\begin{longtable}{|p{3.5cm}|p{3cm}|c|c|c|c|c|}'
   outStr+='\\hline '
   outStr+='Название & Свойства & КМС & Дистанция & '
   outStr+='БПв & ТПв & КУ\\\\ \\hline '
#   for attack in attacks:
#    origin=getOriginWeapon(entity,originWeapons)
#    outStr+=genLine(attack,origin,hero)
#   outStr+='\\end{longtable}'

  battleSkills=hero.ACC+hero.WEP+hero.UNA
  if battleSkills>0:
   outStr+='\\newline'
   outStr+='\\textbf{Боевые Навыки: }'
   tmpStr=''
   tmpStr+='Владение оружием('+hero.WEP+'), ' if hero.WEP>0 else ''
   tmpStr+='Рукопашный бой('+hero.UNA+'), ' if hero.UNA>0 else ''
   tmpStr+='Стрельба('+hero.ACC+'), ' if hero.ACC>0 else ''
   outStr+=tmpStr[:-2]
  outStr+='\\newline'

  
  if 'Навыки' in entity:
   skills=entity.get('Навыки')
   #добавить автоматическое исправление под шаблон

   outStr+='\\textbf{Навыки: }'
   outStr+=genProps(props,short=True)
   outStr+='\\newline'

#  if 'Феномены' in entity:
#   powers=entity.get('Феномены')
#   #добавить автоматическое исправление под шаблон
#   for power in powers:
#    power=fillPower(power,originPowers)
#
#   outStr+='\\textbf{Феномены: }'
#   outStr+=genProps(props,costly=True)
#   outStr+='\\newline'

  if 'Недостатки' in entity:
   flaws=entity.get('Недостатки')
   outStr+='\\textbf{Недостатки}\\begin{itemize}'
   outStr+=genProps(flaws)
   outStr+='\\end{itemize}'

  if 'Трюки' in entity:
   tricks=entity.get('Трюки')
   #добавить автоматическое исправление под шаблон
   tricks=fillPerks(tricks,originPerks)

   outStr+='\\textbf{Трюки}\\begin{itemize}'
   outStr+=genProps(props)
   outStr+='\\end{itemize}'
  if Ходы in entity:
   outStr+='\\textbf{Ходы}\\begin{itemize}'
   moves=entity.get('Ходы')
   outStr+=genProps(moves,costly=True)
   outStr+='\\end{itemize}'
  outStr+='\\newpage'

 return outStr

#def getOriginWeapon(entity,originWeapons):
# if not checkKey('название',entity,keep=True):
#  return None
# originName=entity.get('базовый шаблон') if checkKey('базовый шаблон',entity,keep=True) else entity.get('название')
## list.dict[]
# origin=[x for x in originWeapons if x.get(originName) is not None]
# return origin

def prepSkills(skills):
 preped=[]
 for skill in skills:
  name=list(skill)[0]
  cost=skill.get(name)
  preped.append({name:None,'стоимость':cost})
 return preped

def prepPowers(powers,originPowers):
 preped=[]
 for power in powers:
  name=list(power)[0]
  origin=[x for x in originPowers if x.get('название')==name]
  preped.append({name:None,'стоимость':origin.get('стоимость')})
 return preped
 return 

def prepPerks(prop,originPerks):
 
 originName=entity.get('название')
# list.dict[]
 origin=[x for x in originPerks if x.get(originName) is not None]
 return origin

def getPowers():
 powers=[]
 dataNames=['powers','powers-monsters']
 for dataName in dataNames:
  yamlName='content/'+dataName+'.yaml'
  powers+=getDict(yamlName)
 return powers

def getPerks():
 dataName='tricks-monster'
 yamlName='content/'+dataName+'.yaml'
 return getDict(yamlName)

#def getWeapons():
# weapons=[]
# for dataName in glob.glob("content/weapons-*.yaml"):
#  yamlName='content/'+dataName+'.yaml'
#  weapons+=getDict(yamlName)
#
# powers=[x for x in getPowers() if x.get('Форма')=='Снаряд']
# for power in powers:
#  weapon={}
#  if checkKey('название',power):
#   weapon['назавние'].append(power.get('название'))
#  weapon['тип боеприпасов'].append('Ф')
#  if checkKey('Скорострельность',power):
#   weapon['скорострельность'].append(power.get('Скорострельность'))
#  else:
#   weapon['скорострельность'].append('1')
#  if checkKey('Дистанция',power):
#   tmp=power.get('Тип Повреждений')
#   tmp=tmp.split('/')
#   weapon['Ближняя Дистанция'].append(tmp[0])
#   weapon['Дальняя Дистанция'].append(tmp[1])
#  else:
#   weapon['Ближняя Дистанция'].append('20')
#   weapon['Дальняя Дистанция'].append('40')
#  if checkKey('Бонус Повреждений',power):
#   tmp=power.get('Бонус Повреждений')
#   tmp=tmp.split('/')
#   weapon['основной БПв'].append(tmp[0])
#   weapon['дополнительнй БПв'].append(tmp[1])
#  if checkKey('Тип Повреждений',power):
#   tmp=power.get('Тип Повреждений')
#   tmp=tmp.split(', ')
#   finalstr=''
#   for t in tmp:
#    finalstr+=t[0]
#   weapon['тип Пв'].append(finalstr)
#  if checkKey('КУ',power):
#   weapon['КУ'].append(power.get('КУ'))
#  else:
#   weapon['КУ'].append('20')
# return weapons


#- название: ""
#  Шаблон: "Да"
#  описание: ""
#  Сила: ''
#  Ловкость: ''
#  Выносливость: ''
#  Интеллект: ''
#  Мудрость: ''
#  Обаяние: ''
#  Феноменальная характеристика: ''
#  Размер: '(численное представление: 0-Средний)'
#  Четвероногое: "Да"
#  Скорость: '(модификатор относительно базового значения)'
#  Реакция: '(модификатор относительно базового значения)'
#  Воля: '(модификатор относительно базового значения)'
#  Энергия: '(модификатор относительно базового значения)'
#  ЕЗ: '(модификатор относительно базового значения)'
#  Нити: ""
#  Бонус защиты: ""
#  Ограничение ловкости: ""
#
#  атаки:
#  - название: ''
#    прототип: ''
#    свойства: ''
#    тип боеприпасов: ''
#    магазин: ''
#    скорострельность: ''
#    Ближняя Дистанция: ''
#    Дальняя Дистанция: ''
#    основной БПв: ''
#    дополнительнй БПв: ''
#    тип Пв: ''
#    КУ: ''
#
#  - название: ''
#    свойства: ''
#    тип боеприпасов: ''
#    магазин: ''
#    скорострельность: ''
#    Ближняя Дистанция: ''
#    Дальняя Дистанция: ''
#    основной БПв: ''
#    дополнительнй БПв: ''
#    тип Пв: ''
#    КУ: ''
#
#  Стрельба: (Значение Навыка)
#  Безоружный бой: (Значение Навыка)
#  Владение оружием: (Значение Навыка)
#
#  Навыки:
#  - (Название Навыка): (Значение Навыка)
#  - (Название Навыка): (Значение Навыка)
#
#  Трюки:
#  - (Название Трюка): '(Описание Трюка)'
#  - (Название Трюка): '(Описание Трюка)'
#
#  Недостатки:
#  - (Название Недостатка):'(Описание Недостатка)'
#  - (Название Недостатка):'(Описание Недостатка)'
#
#  Феномены:
#  - (Название Феномена): '(Описание Феномена)'
#    Цена: '(Стоимость Феномена)'
#  - (Название Феномена): '(Описание Феномена)'
#    Цена: '(Стоимость Феномена)'
#
#  Ходы:
#  - (Название Хода): '(Описание Хода)'
#    Цена: '(Стоимость Хода)'
#  - (Название Хода): '(Описание Хода)'
#    Цена: '(Стоимость Хода)'
