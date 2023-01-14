import math, glob, os
from genLib import getName as sortKey
from genLib import genProps
from genLib import genSize
from genLib import bookmark
from genLib import makelink
from genLib import pureGen
#from monsters_weapons import genLine
from genLib import getDict
from genLib import clear

def genPimaryMod(val,template):
 if template: return ''
 mod=math.floor((val-10)/2)
 outStr='('
 if mod>=0: outStr+='+'
 return outStr+str(mod)+')'

class heroStats:
  STR=None
  DEX=None
  CON=None
  INT=None
  WIS=None
  CHA=None
  PHE=None
  PHENAME=None
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
   self.PHE=0
   self.PHENAME=''
   if 'Феноменальная характеристика' not in entity: return
   self.PHENAME=entity.get('Феноменальная характеристика')
   match self.PHENAME:
    case 'Сила' : self.PHE=self.STR
    case 'Ловкость' : self.PHE=self.DEX
    case 'Выносливость' : self.PHE=self.CON
    case 'Интеллект' : self.PHE=self.INT
    case 'Мудрость' : self.PHE=self.WIS
    case 'Обаяние' : self.PHE=self.CHA
    case _ : self.PHENAME=''

  def __init__(self,entity):
   self.STR=entity.get('Сила',0)
   self.DEX=entity.get('Ловкость',0)
   self.CON=entity.get('Выносливость',0)
   self.INT=entity.get('Интеллект',0)
   self.WIS=entity.get('Мудрость',0)
   self.CHA=entity.get('Обаяние',0)
   self.setPhe(entity)

   self.SIZE=entity.get('Размер',0)
   self.HP=entity.get('ЕЗ',0)
   self.SPD=entity.get('Скорость',0)
   self.REF=entity.get('Реакция',0)
   self.ENG=entity.get('Энергия',0)
   self.WIL=entity.get('Воля',0)

   self.DEF=entity.get('Бонус защиты',0)
   self.LIM=entity.get('Ограничение ловкости')
   self.TREADS=entity.get('Нити',0)
   self.WEP=entity.get('Владение оружием',0)
   self.UNA=entity.get('Рукопашный бой',0)
   self.ACC=entity.get('Стрельба',0)

def calculateSecondary(hero,doubleSpeed):
 hero.HP+=(hero.SIZE+3)*hero.CON
 hero.SPD+=math.floor((hero.DEX+hero.CON)/4)+hero.SIZE
 if doubleSpeed: hero.SPD*=2
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

def checkStats(hero):
 count=0
 count+=1 if hero.STR!=0 else 0
 count+=1 if hero.DEX!=0 else 0
 count+=1 if hero.CON!=0 else 0
 count+=1 if hero.INT!=0 else 0
 count+=1 if hero.WIS!=0 else 0
 count+=1 if hero.CHA!=0 else 0
 count+=1 if hero.PHENAME!='' else 0
 count+=1 if hero.SPD!=0 else 0
 count+=1 if hero.REF!=0 else 0
 count+=1 if hero.WIL!=0 else 0
 count+=1 if hero.HP!=0 else 0
 count+=1 if hero.ENG!=0 else 0
 count+=1 if hero.TREADS!=0 else 0
 count+=1 if hero.SIZE!=0 else 0
 count+=1 if hero.DEF!=0 else 0
 return count

def genEntity(entityDict):
# originWeapons=getWeapons()
 originPowers=getPowers()
 originTricks=getTricks()

 outStr=''
 for key in entityDict:
  entity=entityDict.get(key)

  template='Шаблон' in entity
  hero=heroStats(entity)


  if not template: hero=calculateSecondary(hero,'Четвероногое' in entity)

  outStr+='\\subsection{'+key
  outStr+='[Легендарное]' if 'Легендарное' in entity else ''
  outStr+='[Не живое]' if 'Не живое' in entity else ''
  outStr+='}'

  outStr+=bookmark(key,'monster')
  outStr+=entity.get('описание','\\err нет описания')

  statlength=checkStats(hero)
  if statlength>0:
   outStr+='\\newline\\noindent\\begin{minipage}[b]{0.3\\linewidth}'
   outStr+='\\begin{tabular}{|l l|}'
   outStr+='\\hline'
   outStr+='\\textbf{Сл:} & '+str(hero.STR)+genPimaryMod(hero.STR,template)+'\\\\' if hero.STR!=0 else ''
   outStr+='\\textbf{Лв:} & '+str(hero.DEX)+genPimaryMod(hero.DEX,template)+'\\\\' if hero.DEX!=0 else ''
   outStr+='\\textbf{Вн:} & '+str(hero.CON)+genPimaryMod(hero.CON,template)+'\\\\' if hero.CON!=0 else ''
   outStr+='\\textbf{Ин:} & '+str(hero.INT)+genPimaryMod(hero.INT,template)+'\\\\' if hero.INT!=0 else ''
   outStr+='\\textbf{Мд:} & '+str(hero.WIS)+genPimaryMod(hero.WIS,template)+'\\\\' if hero.WIS!=0 else ''
   outStr+='\\textbf{Об:} & '+str(hero.CHA)+genPimaryMod(hero.CHA,template)+'\\\\' if hero.CHA!=0 else ''
   outStr+='\\textbf{ФХ:} & '+str(hero.PHENAME)+'\\\\' if hero.PHENAME!='' else ''
   outStr+='\\textbf{Скорость:} & '+str(hero.SPD)+'\\\\' if hero.SPD!=0 else ''
   outStr+='\\textbf{Реакция:} & '+str(hero.REF)+'\\\\' if hero.REF!=0 else ''
   outStr+='\\textbf{Воля:} & '+str(hero.WIL)+'\\\\' if hero.WIL!=0 else ''
   outStr+='\\textbf{ЕЗ:} & '+str(hero.HP)+'\\\\' if hero.HP!=0 else ''
   outStr+='\\textbf{Энергия:} & '+str(hero.ENG)+'\\\\' if hero.ENG!=0 else ''
   outStr+='\\textbf{Нити:} & '+str(hero.TREADS)+'\\\\' if hero.TREADS!=0 else ''
   outStr+='\\textbf{Размер:} & '+genSize(hero.SIZE)+'\\\\' if hero.SIZE!=0 else ''
   outStr+='\\textbf{Защита:} & '+str(hero.DEF)+'\\\\' if hero.DEF!=0 else ''
   outStr+='\\hline'

   outStr+='\\end{tabular}}'
   outStr+='\\end{minipage}'
   outStr+='\\begin{minipage}[b]{0.7\\linewidth}'


  if 'атаки' in entity:
   outStr+='\\newline\\textbf{Атаки}'
   weapons=entity.get('атаки')
   outStr+='\\begin{longtable}{|p{3cm}|p{2.5cm}|c|c|c|c|c|}'
   outStr+='\\hline '
   outStr+='Название & Свойства & КМС & Дистанция & '
   outStr+='БПв & ТПв & КУ\\\\ \\hline '
   for attack in prepWeapons(weapons,originWeapons):
    outStr+=genLine(attack,hero)
   outStr+='\\end{longtable}'

  battleSkills=hero.ACC+hero.WEP+hero.UNA
  if battleSkills>0:
   outStr+='\\newline'
   outStr+='\\textbf{Боевые Навыки: }'
   tmpStr=''
   tmpStr+='Владение оружием('+str(hero.WEP)+'), ' if hero.WEP>0 else ''
   tmpStr+='Рукопашный бой('+str(hero.UNA)+'), ' if hero.UNA>0 else ''
   tmpStr+='Стрельба('+str(hero.ACC)+'), ' if hero.ACC>0 else ''
   outStr+=tmpStr[:-2]

  if 'Навыки' in entity:
   skills=entity.get('Навыки')
   outStr+='\\newline\\textbf{Навыки: }'
   outStr+=genProps(prepSkills(skills))

  if 'Феномены' in entity:
   powers=entity.get('Феномены')
   outStr+='\\newline\\textbf{Феномены: }'
   outStr+=genProps(prepPowers(powers,originPowers))

  if statlength>0:
   outStr+='\\end{minipage}'

  if 'Недостатки' in entity:
   flaws=entity.get('Недостатки')
   outStr+='\\newline\\textbf{Недостатки}\\begin{itemize}'
   outStr+=genProps(flaws)
   outStr+='\\end{itemize}'

  if 'Трюки' in entity:
   tricks=entity.get('Трюки')
   outStr+='\\newline\\textbf{Трюки}\\begin{itemize}'
   outStr+=genProps(prepTricks(tricks,originTricks))
   outStr+='\\end{itemize}'

  if 'Функции' in entity:
   outStr+='\\newline\\textbf{Ходы}\\begin{itemize}'
   outStr+=genProps(entity.get('Функции'))
   outStr+='\\end{itemize}'

  if 'Ходы' in entity:
   outStr+='\\newline\\textbf{Ходы}\\begin{itemize}'
   outStr+=genProps(entity.get('Ходы'))
   outStr+='\\end{itemize}'
  outStr+='\\newpage'

 return outStr

def prepWeapons(props,origins):
 preped=[]
 for prop in props:
  name=list(prop)[0]
  origin=origins.get(name,None)
  preped.append(weaponMerge(prop,origin))
 return preped

##############################################################################
weaponMerge
genLine
##############################################################################


def prepSkills(props):
 preped=[]
 for prop in props:
  name=list(prop)[0]
  cost=prop.get(name)
  preped.append({name:None,'стоимость':cost})
 return preped

def prepPowers(props,origins):
 preped=[]
 for prop in props:
  name=list(prop)[0]
  origin=origins.get(name,{'стоимость':'\\err не найден феномен'})
  cost=origin.get('стоимость','\\err нет стоимости')
  preped.append({name:None,'стоимость':cost})
 return preped

def prepTricks(props,origins):
 preped=[]
 for prop in props:
  name=list(prop)[0]
  descr=prop.get(name,'\\err нет описания')
  if name in origins:
   origin=origins.get(name)
   descr=origin.get('описание',descr)
  preped.append({name:descr})
 return preped

def getPowers():
 props={}
 dataNames=['powers','powers-monsters']
 for dataName in dataNames:
  yamlName='content/'+dataName+'.yaml'
  props|=getDict(yamlName)
 for dataName in dataNames:
  yamlName='localContent/'+dataName+'.yaml'
  props|=getDict(yamlName)
 return clear(props)

def getTricks():
 props={}
 dataName='tricks-monster'
 yamlName='content/'+dataName+'.yaml'
 props|=getDict(yamlName)
 yamlName='localContent/'+dataName+'.yaml'
 props|=getDict(yamlName)
 return clear(props)

def getWeapons():
 props=[]
 dataNames=['weapons-elder','weapons-melee','weapons-modern','weapons-monsters','weapons-supplimental']
 for dataName in dataNames:
  yamlName='content/'+dataName+'.yaml'
  props|=getDict(yamlName)
 for dataName in dataNames:
  yamlName='localContent/'+dataName+'.yaml'
  props|=getDict(yamlName)
 for power in getPowers():
  props.append(weaponFromPower(power))

 return clear(props)

def weaponFromPower(power):
 for power in powers:
  if checkKey('название',power):
   prop['назавние'].append(power.get('название'))
  prop['тип боеприпасов'].append('Ф')
  if checkKey('Скорострельность',power):
   prop['скорострельность'].append(power.get('Скорострельность'))
  else:
   prop['скорострельность'].append('1')
  if checkKey('Дистанция',power):
   tmp=power.get('Тип Повреждений')
   tmp=tmp.split('/')
   prop['Ближняя Дистанция'].append(tmp[0])
   prop['Дальняя Дистанция'].append(tmp[1])
  else:
   prop['Ближняя Дистанция'].append('20')
   prop['Дальняя Дистанция'].append('40')
  if checkKey('Бонус Повреждений',power):
   tmp=power.get('Бонус Повреждений')
   tmp=tmp.split('/')
   prop['основной БПв'].append(tmp[0])
   prop['дополнительнй БПв'].append(tmp[1])
  if checkKey('Тип Повреждений',power):
   tmp=power.get('Тип Повреждений')
   tmp=tmp.split(', ')
   finalstr=''
   for t in tmp:
    finalstr+=t[0]
   prop['тип Пв'].append(finalstr)
  if checkKey('КУ',power):
   prop['КУ'].append(power.get('КУ'))
  else:
   prop['КУ'].append('20')




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
#  Функции:
#  - (Название Функции): '(Описание Функции)'
#    Цена: '(Стоимость Функции)'
#  - (Название Функции): '(Описание Функции)'
#    Цена: '(Стоимость Функции)'
#
#  Ходы:
#  - (Название Хода): '(Описание Хода)'
#    Цена: '(Стоимость Хода)'
#  - (Название Хода): '(Описание Хода)'
#    Цена: '(Стоимость Хода)'
