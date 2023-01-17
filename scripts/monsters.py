import math, glob, os
from genLib import getName as sortKey
from genLib import genProps
from genLib import genSize
from genLib import bookmark
from genLib import makelink
from genLib import pureGen
from genLib import getDict
from genLib import clear

def genPimaryMod(val,template=False):
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
 originWeapons=getWeapons()
 originPowers=getPowers()
 originTricks=getTricks()

 outStr=''
 for key in entityDict:
  entity=entityDict.get(key)

  template='Шаблон' in entity
  hero=heroStats(entity)

  newLineNeeded=False

  if not template: hero=calculateSecondary(hero,'Четвероногое' in entity)

  outStr+='\\subsection{'+key
  outStr+='[Легендарное]' if 'Легендарное' in entity else ''
  outStr+='[Не живое]' if 'Не живое' in entity else ''
  outStr+='}'

  outStr+=bookmark(key,'monster')

  if 'атаки' in entity:
   outStr+='\\newline' if newLineNeeded else ''
   outStr+='\\textbf{Атаки}'
   weapons=entity.get('атаки')
   outStr+='\\begin{longtable}{|p{3cm}|p{2.5cm}|c|c|c|c|c|}'
   outStr+='\\hline '
   outStr+='Название & Свойства & КМС & Дистанция & '
   outStr+='БПв & ТПв & КУ \\\\ \\hline '
   for attack in prepWeapons(weapons,originWeapons,hero,template):
    outStr+=genWeaponLine(attack,template)
   outStr+='\\end{longtable}'
  
  outStr+=entity.get('описание','\\err нет описания')
  newLineNeeded=True
  statlength=checkStats(hero)
  if statlength>0:
#   outStr+='\\newline\\noindent\\begin{minipage}[b]{0.3\\linewidth}'
   outStr+='\\newline\\begin{tabular}{|l l|}'
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
   outStr+='\\textbf{Размер:} & '+genSize(hero.SIZE)+'\\\\' if hero.SIZE!=0 or not template else ''
   outStr+='\\textbf{Защита:} & '+str(hero.DEF)+'\\\\' if hero.DEF!=0 else ''
   outStr+='\\hline'

   outStr+='\\end{tabular}'
   newLineNeeded=False
#   outStr+='\\end{minipage}'
#   outStr+='\\begin{minipage}[b]{0.7\\linewidth}'

  battleSkills=hero.ACC+hero.WEP+hero.UNA
  if battleSkills>0:
   outStr+='\\newline' if newLineNeeded else ''
   outStr+='\\textbf{Боевые Навыки: }'
   tmpStr=''
   tmpStr+='Владение оружием('+str(hero.WEP)+'), ' if hero.WEP>0 else ''
   tmpStr+='Рукопашный бой('+str(hero.UNA)+'), ' if hero.UNA>0 else ''
   tmpStr+='Стрельба('+str(hero.ACC)+'), ' if hero.ACC>0 else ''
   outStr+=tmpStr[:-2]
   newLineNeeded=True

  if 'Навыки' in entity:
   skills=entity.get('Навыки')
   outStr+='\\newline' if newLineNeeded else ''
   outStr+='\\textbf{Навыки: }'
   outStr+=genProps(prepSkills(skills))
   newLineNeeded=True

  if 'Феномены' in entity:
   powers=entity.get('Феномены')
   outStr+='\\newline' if newLineNeeded else ''
   outStr+='\\textbf{Феномены: }'
   outStr+=genProps(prepPowers(powers,originPowers))
   newLineNeeded=True

#  if statlength>0:
#   outStr+='\\end{minipage}'

  if 'Недостатки' in entity:
   flaws=entity.get('Недостатки')
   outStr+='\\newline' if newLineNeeded else ''
   outStr+='\\textbf{Недостатки}'
   outStr+=genProps(flaws)
   newLineNeeded=True


  if 'Трюки' in entity:
   tricks=entity.get('Трюки')
   outStr+='\\newline' if newLineNeeded else ''
   outStr+='\\textbf{Трюки}'
   outStr+=genProps(prepTricks(tricks,originTricks))
   newLineNeeded=True

  if 'Функции' in entity:
   outStr+='\\newline' if newLineNeeded else ''
   outStr+='\\textbf{Ходы}'
   outStr+=genProps(entity.get('Функции'))
   newLineNeeded=True

  if 'Ходы' in entity:
   outStr+='\\newline' if newLineNeeded else ''
   outStr+='\\textbf{Ходы}'
   outStr+=genProps(entity.get('Ходы'))
  outStr+='\\newpage'

 return outStr

def prepWeapons(props,origins,hero,template):
 preped=[]
 for prop in props:
  name=list(prop)[0]
  weapon=prop.get(name)
  if type(weapon)!=dict:
   weapon={}
  originName=weapon.get('базовый шаблон',name)
  origin=origins.get(originName,None)
  merged={name:weaponMerge(weapon,origin,hero,template)}
  preped.append(merged)
 return preped

##############################################################################
def weaponMerge(weapon,origin,hero,template):
 merged={}
 wType=origin.get('тип боеприпасов','')
 features=clear(origin.get('свойства',{})|weapon.get('свойства',{}))
 natural='Естественное' in features

 bDex=math.floor((hero.DEX-10)/2)
 bStr=math.floor((hero.STR-10)/2)
 bPhe=math.floor((hero.PHE-10)/2)
 meleeBonus=hero.SIZE+bDex+bStr
 meleeBonus+=hero.UNA if natural else hero.WEP
 bonus=hero.ACC
 if wType=='М':
  bonus+=hero.SIZE+bDex+bStr
 elif wType=='Ф':
  bonus+=bPhe-hero.SIZE
 else:
  bonus+=bDex-hero.SIZE
 bonus=meleeBonus if wType=='' else bonus

 wBonus=origin.get('основной БПв',0)+weapon.get('основной БПв',0)
 eBonus=origin.get('дополнительнй БПв',0)+weapon.get('дополнительнй БПв',0)

 if template:
  meleeBonus=0
  bonus=0
 else:
  if bonus==0:
   merged['Помеха Основная']=True
  if meleeBonus==0:
   merged['Помеха Дополнительная']=True

 if 'КУ' in weapon:
  origin['КУ']=origin.get('КУ')+weapon.get('КУ')

 merged['свойства']=features
 if 'особые свойства' in origin or 'особые свойства' in weapon:
  merged['особые свойства']=''
 merged['тип боеприпасов']=wType
 merged['магазин']=weapon.get('магазин',origin.get('магазин'))
 merged['скорострельность']=weapon.get('скорострельность',origin.get('скорострельность'))
 if 'Ближняя Дистанция' in origin:
  merged['Ближняя Дистанция']=origin.get('Ближняя Дистанция')+weapon.get('Ближняя Дистанция',0)
 if 'Дальняя Дистанция' in origin:
  merged['Дальняя Дистанция']=origin.get('Дальняя Дистанция')+weapon.get('Дальняя Дистанция',0)
 merged['ББ БПв']=wBonus+meleeBonus
 merged['основной БПв']=wBonus+bonus
 if 'дополнительнй БПв' in origin:
  merged['дополнительнй БПв']=eBonus+bonus
 merged['тип Пв']=weapon.get('тип Пв',origin.get('тип Пв'))
 if 'КУ' in weapon:
  merged['КУ']=origin.get('КУ')+weapon.get('КУ')
 elif 'КУ' in origin:
  merged['КУ']=origin.get('КУ')

 return merged

##############################################################################
def genWeaponLine(prop,template):
 outStr=''
 name=list(prop)[0]
 weapon=prop.get(name,{})

 wType=weapon.get('тип боеприпасов','')
 isRanged=wType!=''
 features=list(weapon.get('свойства',[]))
 features.sort()
 addLine='Снаряды' not in features and wType=='М'

 eType='power' if wType=='Ф' else 'weapon'
 originName=weapon.get('базовый шаблон',name)
 outStr+=makelink(originName,eType,name)
 outStr+='*' if 'особые свойства' in weapon else ''
 outStr+=' & '


 joiner=', '
 outStr+=joiner.join(features)
 outStr+=' & '

 if isRanged:
  outStr+=wType
  outStr+='/'
  if wType=='М':
   outStr+='-'
  elif wType=='Ф':
   outStr+='-'
  elif wType=='Э':
   outStr+='*'
  else:
    val=weapon.get('магазин',False)
    outStr+=str(val) if val else '\\err'
  outStr+='/'
  val=weapon.get('скорострельность',False)
  outStr+=str(val) if val else '\\err'
  outStr+=' & '
  val=weapon.get('Ближняя Дистанция',False)
  outStr+=str(val) if val else '\\err'
  outStr+='/'
  val=weapon.get('Дальняя Дистанция',False)
  outStr+=str(val) if val else '\\err'
 else:
  outStr+='- & Ближ. бой'
 outStr+=' & '

 if 'основной БПв' in weapon:
  val=weapon.get('основной БПв')
  outStr+='+' if val>0 else ''
  outStr+=str(val)
 else:
  outStr+='\\err'

 val=weapon.get('дополнительнй БПв',False)
 if isRanged or val:
  outStr+='/'
  if 'дополнительнй БПв' in weapon:
   outStr+='+' if val>0 else ''
   outStr+=str(val)
  else:
   outStr+='\\err'
 outStr+='*' if 'Помеха Основная' in weapon and not template else ''
 outStr+=' & '

 outStr+=weapon.get('тип Пв','\\err')
 outStr+=' & '

 val=weapon.get('КУ',0)
 outStr+=str(val) if val>1 and val<=20 else '-'
 outStr+='+' if val<20 else ''

 outStr+='\\\\ '
 outStr+=genWeaponSubLine(weapon,template) if addLine else ''
 outStr+='\\hline '
 return outStr

def genWeaponSubLine(weapon,template):
 outStr=' &  & - & Ближ. бой & '

 val=weapon.get('ББ БПв',False)
 outStr+='+' if val>0 else ''
 outStr+=str(val) if val else '\\err'
 outStr+='*' if 'Помеха Дополнительная' in weapon and not template else ''

 outStr+=' &  &  \\\\ '
 return outStr
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
 props={}
 dataNames=['weapons-elder','weapons-melee','weapons-modern','weapons-monsters','weapons-supplimental']
 for dataName in dataNames:
  yamlName='content/'+dataName+'.yaml'
  props|=getDict(yamlName)
 for dataName in dataNames:
  yamlName='localContent/'+dataName+'.yaml'
  props|=getDict(yamlName)
 powers=getPowers()
 for key in powers:
  power=powers.get(key)
  if power.get('Форма')=='Снаряд':
   props[key]=weaponFromPower(key,power)

 return clear(props)

def weaponFromPower(key,power):
 prop={}
 prop['тип боеприпасов']='Ф'

 prop['скорострельность']=int(power.get('Скорострельность','1'))

 tmp=power.get('Дистанция','20/40')
 tmp=tmp.split('/')
 prop['Ближняя Дистанция']=int(tmp[0])
 prop['Дальняя Дистанция']=int(tmp[1])
 tmp=power.get('Бонус Повреждений','\\err/\\err')
 tmp=tmp.split('/')
 prop['основной БПв']=int(tmp[0])
 prop['дополнительнй БПв']=int(tmp[1])

 tmp=power.get('Тип Повреждений','-')
 tmp=tmp.split(', ')
 finalstr=''
 for t in tmp:
  finalstr+=t[0]
 prop['тип Пв']=finalstr

 prop['КУ']=int(power.get('КУ','20'))

 return prop

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
