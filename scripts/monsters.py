import math, glob, os
from genLib import checkKey
from genLib import tryInt
from genLib import sortKey
from genLib import genProps
from genLib import genSize
from genLib import bookmark
from genLib import makeref
from monsters-weapons import genLine
from genFromYaml import getList
def pureGen():
 return False

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
  def fillGaps(self):
   self.STR=0 if self.STR is None else self.STR
   self.DEX=0 if self.DEX is None else self.DEX
   self.CON=0 if self.CON is None else self.CON
   self.INT=0 if self.INT is None else self.INT
   self.WIS=0 if self.WIS is None else self.WIS
   self.CHA=0 if self.CHA is None else self.CHA

   self.SIZE=0 if self.SIZE is None else self.SIZE
   self.HP=0 if self.HP is None else self.HP
   self.SPD=0 if self.SPD is None else self.SPD
   self.REF=0 if self.REF is None else self.REF
   self.ENG=0 if self.ENG is None else self.ENG
   self.WIL=0 if self.WIL is None else self.WIL

   self.DEF=0 if self.DEF is None else self.DEF
   self.TREADS='-' if self.TREADS is None else self.TREADS
   self.WEP=0 if self.WEP is None else self.WEP
   self.UNA=0 if self.UNA is None else self.UNA
   self.ACC=0 if self.ACC is None else self.ACC

  def setPhe(self,entity):
   if not checkKey('Феноменальная характеристика',entity,keep=True):
    return
   match entity.get('Феноменальная характеристика'):
    case 'Сила' : self.PHE=self.STR
    case 'Ловкость' : self.PHE=self.DEX
    case 'Выносливость' : self.PHE=self.CON
    case 'Интеллект' : self.PHE=self.INT
    case 'Мудрость' : self.PHE=self.WIS
    case 'Обаяние' : self.PHE=self.CHA

  def __init__(self,entity):
   self.STR=int(entity.get('Сила')) if checkKey('Сила',entity,keep=True) else None
   self.DEX=int(entity.get('Ловкость')) if checkKey('Ловкость',entity,keep=True) else None
   self.CON=int(entity.get('Выносливость')) if checkKey('Выносливость',entity,keep=True) else None
   self.INT=int(entity.get('Интеллект')) if checkKey('Интеллект',entity,keep=True) else None
   self.WIS=int(entity.get('Мудрость')) if checkKey('Мудрость',entity,keep=True) else None
   self.CHA=int(entity.get('Обаяние')) if checkKey('Обаяние',entity,keep=True) else None
   setPhe(entity)

   self.SIZE=int(entity.get('Размер')) if checkKey('Размер',entity,keep=True) else None
   self.HP=int(entity.get('ЕЗ')) if checkKey('ЕЗ',entity,keep=True) else None
   self.SPD=int(entity.get('Скорость')) if checkKey('Скорость',entity,keep=True) else None
   self.REF=int(entity.get('Реакция')) if checkKey('Реакция',entity,keep=True) else None
   self.ENG=int(entity.get('Энергия')) if checkKey('Энергия',entity,keep=True) else None
   self.WIL=int(entity.get('Воля')) if checkKey('Воля',entity,keep=True) else None

   self.DEF=int(entity.get('Бонус защиты')) if checkKey('Бонус защиты',entity,keep=True) else None
   self.LIM=int(entity.get('Ограничение ловкости')) if checkKey('Ограничение ловкости',entity,keep=True) else None
   self.TREADS=entity.get('Нити') if checkKey('Нити',entity,keep=True) else None
   self.WEP=entity.get('Владение оружием') if checkKey('Владение оружием',entity,keep=True) else None
   self.UNA=entity.get('Рукопашный бой') if checkKey('Рукопашный бой',entity,keep=True) else None
   self.ACC=entity.get('Стрельба') if checkKey('Стрельба',entity,keep=True) else None

def genEntity(entityList):
 outStr=''
 originWeapons=getWeapons()
 originPowers=getPowers()
 originPerks=getPerks()

 for entity in entityList:
  outStr=''
  outStr+='\\subsection{'
  outStr+=bookmark(entity.get('название','\\err не задано название'),'monster')
  outStr+='}'
  checkKey('описание',entity)
  outStr+=entity.get('описание')

  outStr+='\\begin{longtable}{l l l l l l l l l l}'
  hero=heroStats(entity)
  hero.fillGaps()
  template=checkKey('Шаблон',entity,keep=True)
  if not template:
   hero.HP+=(hero.SIZE+3)*hero.CON
   hero.SPD+=math.floor((hero.DEX+hero.CON)/4)+hero.SIZE
   if checkKey('Четвероногое',entity,keep=True):
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
  checkKey('защита',entity)
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
  if checkKey('атаки',entity):
   attacks=entity.get('атаки')
   outStr+='\\begin{longtable}{|p{3.5cm}|p{3cm}|c|c|c|c|c|}'
   outStr+='\\hline '
   outStr+='Название & Свойства & КМС & Дистанция & '
   outStr+='БПв & ТПв & КУ\\\\ \\hline '
   for attack in attacks:
    origin=getOriginWeapon(entity,originWeapons)
    outStr+=genLine(attack,origin,hero)
   outStr+='\\end{longtable}'
  else:
   outStr+='\\tbd'

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
  if checkKey('Навыки',entity,keep=True):
   outStr+='\\textbf{Навыки: }'
   props=entity.get('Навыки')
   outStr+=genProps(props,short=True)
   outStr+='\\newline'

  if checkKey('Феномены',entity,keep=True):
   outStr+='\\textbf{Феномены: }'

   originPowers

   #сформировать словарь феноменов основываясь на списке
   props=entity.get('Феномены')
   outStr+=genProps(props,costly=True)
   outStr+='\\newline'
  if checkKey('Недостатки',entity,keep=True):
   outStr+='\\textbf{Недостатки}\\begin{itemize}'
   props=entity.get('Недостатки')
   outStr+=genProps(props)
   outStr+='\\end{itemize}'
  if checkKey('Трюки',entity,keep=True):
   outStr+='\\textbf{Трюки}\\begin{itemize}'

   originPerks
   #сформировать словарь трюков основываясь на списке и описании
   #если трюк есть в списке общих, достать оттуда, иначе взять описание из карточки существа
   props=entity.get('Трюки')
   outStr+=genProps(props)
   outStr+='\\end{itemize}'
  if checkKey('Ходы',entity,keep=True):
   outStr+='\\textbf{Ходы}\\begin{itemize}'
   props=entity.get('Ходы')
   outStr+=genProps(props,costly=True)
   outStr+='\\end{itemize}'
  outStr+='\\newpage'

 return outStr

def getOriginWeapon(entity,originWeapons)
 if not checkKey('название',entity,keep=True):
  return None
 originName=entity.get('базовый шаблон') if checkKey('базовый шаблон',entity,keep=True) else entity.get('название')
 list.dict[]
 origin=[x for x in originWeapons if x.get(originName) is not None]
 return origin[0] if origin is list else origin

def getOriginPower(entity,originPowers)
 if not checkKey('название',entity,keep=True):
  return None
 originName=entity.get('базовый шаблон') if checkKey('базовый шаблон',entity,keep=True) else entity.get('название')
 list.dict[]
 origin=[x for x in originWeapons if x.get(originName) is not None]
 return origin[0] if origin is list else origin

def getPerks(entity,originPerks)
 if not checkKey('название',entity,keep=True):
  return None
 originName=entity.get('базовый шаблон') if checkKey('базовый шаблон',entity,keep=True) else entity.get('название')
 list.dict[]
 origin=[x for x in originWeapons if x.get(originName) is not None]
 return origin[0] if origin is list else origin

def getPowers:
 powers=[]
 dataNames=['powers','powers-monsters']
 for dataName in dataNames
  yamlName='content/'+dataName+'.yaml'
  powers+=getList(yamlName)
 return powers

def getPerks:
 dataName='tricks-monster'
 yamlName='content/'+dataName+'.yaml'
 return getList(yamlName)

def getWeapons:
 weapons=[]
 for dataName in glob.glob("content/weapons-*.yaml"):
  yamlName='content/'+dataName+'.yaml'
  weapons+=getList(yamlName)

 powers=[x for x in getPowers() if x.get('Форма')=='Снаряд']
 for power in powers
  weapon={}
  if checkKey('название',power):
   weapon['назавние'].append(power.get('название'))
  weapon['тип боеприпасов'].append('Ф')
  if checkKey('Скорострельность',power):
   weapon['скорострельность'].append(power.get('Скорострельность'))
  else
   weapon['скорострельность'].append('1')
  if checkKey('Дистанция',power):
   tmp=power.get('Тип Повреждений')
   tmp=tmp.split('/')
   weapon['Ближняя Дистанция'].append(tmp[0])
   weapon['Дальняя Дистанция'].append(tmp[1])
  else:
   weapon['Ближняя Дистанция'].append('20')
   weapon['Дальняя Дистанция'].append('40')
  if checkKey('Бонус Повреждений',power):
   tmp=power.get('Бонус Повреждений')
   tmp=tmp.split('/')
   weapon['основной БПв'].append(tmp[0])
   weapon['дополнительнй БПв'].append(tmp[1])
  if checkKey('Тип Повреждений',power):
   tmp=power.get('Тип Повреждений')
   tmp=tmp.split(', ')
   finalstr=''
   for t in tmp:
    finalstr+=t[0]
   weapon['тип Пв'].append(finalstr)
  if checkKey('КУ',power):
   weapon['КУ'].append(power.get('КУ'))
  else
   weapon['КУ'].append('20')
 return weapons


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
