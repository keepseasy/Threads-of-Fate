import math
#import os
#import glob
from scripts.genLib import getName as sortKey
from scripts.genLib import genProps
from scripts.genLib import genSize
#from scripts.genLib import bookmark
from scripts.genLib import makelink
from scripts.genLib import pureGen
from scripts.genLib import getDict
from scripts.genLib import clear
from scripts.genLib import try_to_get

#def genPimaryMod(val,template=False):
# if template: return ''
def genPimaryMod(val):
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
  WOUND=None
  DOUBLE_WOUND=None
  MORTAL_WOUND=None
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
   self.STR=10+entity.get('Сила',0)
   self.DEX=10+entity.get('Ловкость',0)
   self.CON=10+entity.get('Выносливость',0)
   self.INT=10+entity.get('Интеллект',0)
   self.WIS=10+entity.get('Мудрость',0)
   self.CHA=10+entity.get('Обаяние',0)
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
  hero.HP+=int((hero.SIZE+3)*hero.CON)
  hero.DOUBLE_WOUND = int(hero.HP/3)
  hero.WOUND = int(hero.HP*2/3)
  hero.MORTAL_WOUND = int(hero.HP/5)
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

def genEntity(entityDict,idx,form):
  originWeapons=getWeapons()
  originPowers=getPowers()
  originTricks=getTricks()

  outStr=''
  for key in entityDict:
    entity=entityDict.get(key)
  #  print(key)

    hero=heroStats(entity)

    # newLineNeeded=False

    hero=calculateSecondary(hero,'Четвероногое' in entity)

    outStr+='\\subsubsection{'+key
    outStr+='[Легендарное]' if 'Легендарное' in entity else ''
    outStr+='[Не живое]' if 'Не живое' in entity else ''
    outStr+='}'
    outStr+='\\index['+idx+']{'+key+'}'
  #  outStr+=bookmark(key,'monster')

    if 'атаки' in entity:
      weapons=entity.get('атаки')
      outStr+='\\begin{longtable}{|p{3cm}|p{2.5cm}|c|c|c|c|c|}'
      outStr+='\\multicolumn{7}{c}{\\textbf{Атаки}} \\\\ \\hline'
      outStr+='Название & Свойства & КМС & Дистанция & '
      outStr+='БПв & ТПв & КУ \\\\ \\hline '
      for attack in prepWeapons(weapons,originWeapons,hero):
  #     print(attack)
        outStr+=genWeaponLine(attack)
      outStr+='\\end{longtable}'
    
    outStr+='\\begin{multicols}{2}'
    outStr+='\\begin{tabular}{|p{2cm} p{2cm}|}'
    outStr+='\\multicolumn{2}{c}{\\textbf{Характеристики}} \\\\ \\hline'
    outStr+='\\textbf{Сл:} & '+str(hero.STR)+genPimaryMod(hero.STR)+'\\\\'# if hero.STR!=0 else ''
    outStr+='\\textbf{Лв:} & '+str(hero.DEX)+genPimaryMod(hero.DEX)+'\\\\'# if hero.DEX!=0 else ''
    outStr+='\\textbf{Вн:} & '+str(hero.CON)+genPimaryMod(hero.CON)+'\\\\'# if hero.CON!=0 else ''
    outStr+='\\textbf{Ин:} & '+str(hero.INT)+genPimaryMod(hero.INT)+'\\\\'# if hero.INT!=0 else ''
    outStr+='\\textbf{Мд:} & '+str(hero.WIS)+genPimaryMod(hero.WIS)+'\\\\'# if hero.WIS!=0 else ''
    outStr+='\\textbf{Об:} & '+str(hero.CHA)+genPimaryMod(hero.CHA)+'\\\\'# if hero.CHA!=0 else ''
    outStr+='\\textbf{ФХ:} & '+str(hero.PHENAME)+'\\\\' if hero.PHENAME!='' else ''
    outStr+='\\hline\\hline'
    outStr+='\\textbf{Воля:} & '+str(hero.WIL)+'\\\\'# if hero.WIL!=0 else ''
    outStr+='\\textbf{Реакция:} & '+str(hero.REF)+'\\\\'# if hero.REF!=0 else ''
    outStr+='\\textbf{Скорость:} & '+str(hero.SPD)+'\\\\'# if hero.SPD!=0 else ''
    outStr+='\\textbf{Энергия:} & '+str(hero.ENG)+'\\\\'# if hero.ENG!=0 else ''
    outStr+='\\hline\\hline'
    outStr+='\\textbf{ЕЗ:} & '+str(hero.HP)+'\\\\'# if hero.HP!=0 else ''
    outStr+='\\textbf{Ранен:} & '+str(hero.WOUND)+'\\\\'# if hero.HP!=0 else ''
    outStr+='\\textbf{Разбит:} & '+str(hero.DOUBLE_WOUND)+'\\\\'# if hero.HP!=0 else ''
    outStr+='\\textbf{Контузия:} & '+str(hero.MORTAL_WOUND)+'\\\\'# if hero.HP!=0 else ''
    outStr+='\\hline\\hline'
    outStr+='\\textbf{Нити:} & '+str(hero.TREADS)+'\\\\' if hero.TREADS!=0 else ''
    outStr+='\\textbf{Размер:} & '+genSize(hero.SIZE)+'\\\\' if hero.SIZE!=0 else ''
    outStr+='\\textbf{Защита:} & '+str(hero.DEF)+'\\\\'# if hero.DEF!=0 else ''
    outStr+='\\hline \\end{tabular}'


    battleSkills=hero.ACC+hero.WEP+hero.UNA
    if battleSkills>0:
      outStr+='\\paragraph{Боевые Навыки: }'
      tmpStr=''
      tmpStr+='Владение оружием('+str(hero.WEP)+'), ' if hero.WEP>0 else ''
      tmpStr+='Рукопашный бой('+str(hero.UNA)+'), ' if hero.UNA>0 else ''
      tmpStr+='Стрельба('+str(hero.ACC)+'), ' if hero.ACC>0 else ''
      outStr+=tmpStr[:-2]
      outStr+='\\newline'

    if 'Навыки' in entity:
      skills=entity.get('Навыки')
      outStr+='\\textbf{Навыки: }'
      outStr+=genProps(prepSkills(skills))
      outStr+='\\newline'

    if 'Феномены' in entity:
      powers=entity.get('Феномены')
      outStr+='\\textbf{Феномены: }'
      outStr+=genProps(prepPowers(powers,originPowers))
      outStr+='\\newline'


    if 'Недостатки' in entity:
      flaws=entity.get('Недостатки')
      outStr+='\\textbf{Недостатки: }'
      outStr+=genProps(flaws,shrot_ver=True)

    outStr+='\\columnbreak\\newline'

    if 'Трюки' in entity:
      tricks=entity.get('Трюки')
      outStr+='\\textbf{Трюки}'
      outStr+=genProps(prepTricks(tricks,originTricks))

    if 'Функции' in entity:
      outStr+='\\textbf{Функции}'
      outStr+=genProps(entity.get('Функции'))

    if 'Ходы' in entity:
      outStr+='\\textbf{Ходы}'
      outStr+=genProps(entity.get('Ходы'))
  
    outStr+='\\end{multicols}'
    outStr+='\\clearpage'

  for key in entityDict:
    outStr+='\\paragraph{'+key+': }'
    outStr+=try_to_get('описание', entity, key)
  return outStr

def prepWeapons(props,origins,hero):
  preped=[]
  for prop in props:
    name=list(prop)[0]
    weapon=prop.get(name)
    if type(weapon)!=dict:
      weapon={}
    originName=weapon.get('базовый шаблон',name)
    origin=origins.get(originName,None)
    merged={name:weaponMerge(weapon,origin,hero)}
    preped.append(merged)
  return preped

##############################################################################
def weaponMerge(weapon,origin,hero):
  merged={}
  if not origin:
    return merged
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
def genWeaponLine(prop):
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
  outStr+='*' if 'Помеха Основная' in weapon else ''
  outStr+=' & '

  outStr+=weapon.get('тип Пв','\\err')
  outStr+=' & '

  val=weapon.get('КУ',0)
  outStr+=str(val) if val>1 and val<=20 else '-'
  outStr+='+' if val<20 else ''

  outStr+='\\\\ '
  outStr+=genWeaponSubLine(weapon) if addLine else ''
  outStr+='\\hline '
  return outStr

def genWeaponSubLine(weapon):
 outStr=' &  & - & Ближ. бой & '

 val=weapon.get('ББ БПв','err')
 if val=='err':
  outStr+='\\err'
 else:
  outStr+='+' if val>0 else ''
  outStr+=str(val)
 outStr+='*' if 'Помеха Дополнительная' in weapon else ''

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
  origin=origins.get(name,{})
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
  dataNames=['weapons','weapons-monsters']
  for dataName in dataNames:
    yamlName='base_content/'+dataName+'.yaml'
    props|=getDict(yamlName)
  for dataName in dataNames:
    yamlName='dlc/'+dataName+'.yaml'
    props|=getDict(yamlName)
  powers=getPowers()

  for key in powers:
    power=powers.get(key)
    if power.get('Форма')=='Снаряд':
      props[key]=weaponFromMissile(key,power)
    if power.get('Форма')=='Бомба':
      props[key]=weaponFromBomb(key,power)
    if power.get('Форма')=='Метка':
      props[key]=props["Метка/касание"]
  # for key in props:
    # print(key)
  return clear(props)

def weaponFromMissile(key,power):
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


def weaponFromBomb(key,power):
 prop={}
 prop['тип боеприпасов']='Ф'
 prop['скорострельность']='1'

 tmp=power.get('Дистанция','5/20')
 tmp=tmp.split('/')
 prop['Ближняя Дистанция']=int(tmp[0])
 prop['Дальняя Дистанция']=int(tmp[1])
 tmp=power.get('Бонус Повреждений','0/-1')
 tmp=tmp.split('/')
 prop['основной БПв']=int(tmp[0])
 prop['дополнительнй БПв']=int(tmp[1])

 tmp=power.get('Тип Повреждений','Д')
 tmp=tmp.split(', ')
 finalstr=''
 for t in tmp:
  finalstr+=t[0]
 prop['тип Пв']=finalstr

 prop['КУ']=int(power.get('КУ','20'))

 return prop

def weaponFromMark(key,prop):

 prop={}
 prop['тип боеприпасов']='Ф'
 prop['скорострельность']='1'

 tmp=prop.get('Дистанция','5/20')
 tmp=tmp.split('/')
 prop['Ближняя Дистанция']=int(tmp[0])
 prop['Дальняя Дистанция']=int(tmp[1])
 tmp=prop.get('Бонус Повреждений','0/-1')
 tmp=tmp.split('/')
 prop['основной БПв']=int(tmp[0])
 prop['дополнительнй БПв']=int(tmp[1])

 tmp=prop.get('Тип Повреждений','Д')
 tmp=tmp.split(', ')
 finalstr=''
 for t in tmp:
  finalstr+=t[0]
 prop['тип Пв']=finalstr

 prop['КУ']=int(prop.get('КУ','20'))

 return prop

#(название):
#  Форма: 
#  описание: ''
#  Сила: 
#  Ловкость: 
#  Выносливость: 
#  Интеллект: 
#  Мудрость: 
#  Обаяние: 
#  Феноменальная характеристика: 
#  Размер: (численное представление: 0-Средний)
#  Четвероногое: Да
#  Скорость: (модификатор относительно базового значения)
#  Реакция: (модификатор относительно базового значения)
#  Воля: (модификатор относительно базового значения)
#  Энергия: (модификатор относительно базового значения)
#  ЕЗ: (модификатор относительно базового значения)
#  Нити: 
#  Бонус защиты: 
#  Ограничение ловкости: 
#
#  атаки:
#    - (название):
#        базовый шаблон:
#        свойства: ''
#        тип боеприпасов: ''
#        магазин: ''
#        скорострельность: ''
#        Ближняя Дистанция: ''
#        Дальняя Дистанция: ''
#        основной БПв: ''
#        дополнительнй БПв: ''
#        тип Пв: ''
#        КУ: ''
#
#    - (название):
#        базовый шаблон:
#        свойства: ''
#        тип боеприпасов: ''
#        магазин: ''
#        скорострельность: ''
#        Ближняя Дистанция: ''
#        Дальняя Дистанция: ''
#        основной БПв: ''
#        дополнительнй БПв: ''
#        тип Пв: ''
#        КУ: ''
#
#  Стрельба: (Значение Навыка)
#  Рукопашный бой: (Значение Навыка)
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
#  - (Название Недостатка): '(Описание Недостатка)'
#  - (Название Недостатка): '(Описание Недостатка)'
#
#  Феномены:
#  - (Название Феномена): '(Описание Феномена)'
#    Цена: '(Стоимость Феномена)'
#  - (Название Феномена): '(Описание Феномена)'
#    Цена: '(Стоимость Феномена)'
#
#  Функции:
#  - (Название Функции): '(Описание Функции)'
#  - (Название Функции): '(Описание Функции)'
#
#  Ходы:
#  - (Название Хода): '(Описание Хода)'
#    Цена: '(Стоимость Хода)'
#  - (Название Хода): '(Описание Хода)'
#    Цена: '(Стоимость Хода)'
