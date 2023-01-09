import math
from genLib import checkKey
from genLib import tryInt
from genLib import sortKey
#from genLib import genProps
from genLib import genSize
from monsters import heroStats
from genLib import clear
def pureGen():
 return False

class weaponStats:
 displayName=None
 hasSpecial=False
 alias=None
 features=[]
 wType=None
 clipSize=None
 rateOfFire=None
 shortDist=None
 longDist=None
 dmg0=None
 dmg1=None
 dmgType=None
 crit=None
 def __init__(self,entity):
  self.displayName=entity.get('название') if checkKey('название',entity,keep=True) else None
  self.alias=entity.get('базовый шаблон') if checkKey('базовый шаблон',entity,keep=True) else None
  self.hasSpecial=checkKey('особые свойства',entity,keep=True)

  if checkKey('свойства',entity,keep=True):
   features=entity.get('свойства')
    if features is list:
     self.features=features
    else:
     self.features.append('\\err не удалось извлечь список свойств')
  self.wType=entity.get('тип боеприпасов') if checkKey('тип боеприпасов',entity,keep=True) else None
  self.clipSize=entity.get('магазин') if checkKey('магазин',entity,keep=True) else None
  if self.clipSize is not int:
   self.clipSize=None
  self.rateOfFire=entity.get('скорострельность') if checkKey('скорострельность',entity,keep=True) else None
  if self.rateOfFire is not int:
   self.rateOfFire=None
  self.shortDist=entity.get('Ближняя Дистанция') if checkKey('Ближняя Дистанция',entity,keep=True) else None
  if self.shortDist is not int:
   self.shortDist=None
  self.longDist=entity.get('Дальняя Дистанция') if checkKey('Дальняя Дистанция',entity,keep=True) else None
  if self.longDist is not int:
   self.longDist=None
  self.dmg0=entity.get('основной БПв') if checkKey('основной БПв',entity,keep=True) else None
  if self.dmg0 is not int:
   self.dmg0=None
  self.dmg1=entity.get('дополнительнй БПв') if checkKey('дополнительнй БПв',entity,keep=True) else None
  if self.dmg1 is not int:
   self.dmg1=None
  self.dmgType=entity.get('тип Пв') if checkKey('тип Пв',entity,keep=True) else None
  self.crit=entity.get('КУ') if checkKey('КУ',entity,keep=True) else None
  if self.crit is not int:
   self.crit=None

 def merge(self,origin):
  self.hasSpecial|=origin.hasSpecial
  features=self.features+origin.features
  self.features=clear(features)
  self.features.sort()
  self.wType=origin.wType

  if self.clipSize is None:
   self.clipSize=origin.clipSize
  else:
   self.clipSize+=0 if origin.clipSize is None else origin.clipSize
  if self.rateOfFire is None:
   self.rateOfFire=origin.rateOfFire
  else:
   self.rateOfFire+=0 if origin.rateOfFire is None else origin.rateOfFire
  if self.shortDist is None:
   self.shortDist=origin.shortDist
  else:
   self.shortDist+=0 if origin.shortDist is None else origin.shortDist
  if self.longDist is None:
   self.longDist=origin.longDist
  else:
   self.longDist+=0 if origin.longDist is None else origin.longDist
  if self.dmg0 is None:
   self.dmg0=origin.dmg0
  else:
   self.dmg0+=0 if origin.dmg0 is None else origin.dmg0
  if self.dmg1 is None:
   self.dmg1=origin.dmg1
  else:
   self.dmg1+=0 if origin.dmg1 is None else origin.dmg1
  if self.crit is None:
   self.crit=origin.crit
  else:
   self.crit+=0 if origin.crit is None else origin.crit
  self.dmgType=origin.dmgType if self.dmgType is None else self.dmgType

def genMod(val):
 return math.floor((val-10)/2)

def genRef(weapon,eType)
 displayName=weapon.displayName
 if weapon.alias is None
  name=weapon.displayName
 else
  name=weapon.alias
  displayName+='('+weapon.alias+')'
 if name is not None:
  return '\\hyperlink{'+eType+str(hash(name))+'}{'+displayName+'}'
 return '\\err не задано название Оружия, ссылка не создана!'

def calcBonus(weapon,hero)
 if weapon.wType is not None:
  bonus=hero.ACC
  match weapon.wType:
   case 'М' : bonus+=genMod(hero.DEX)+genMod(hero.STR)+hero.SIZE
   case 'Ф' :bonus+=genMod(hero.PHE)-hero.SIZE
   case -: bonus+=genMod(hero.DEX)-hero.SIZE
  return bonus
 bonus=hero.SIZE+genMod(hero.DEX)+genMod(hero.STR)
 bonus+= hero.UNA if 'Естественное' in weapon.features else hero.WEP
 return bonus

def genLine(entity,origin,hero):
 weapon=weaponStats(entity)
 if not origin is None
  weapon.merge(weaponStats(origin))
 outStr=genRef(weapon,'power') if weapon.wType=='Ф' else genRef(weapon,'weapon')
 if weapon.hasSpecial:
  outStr+='*'
 outStr+=' & '
 if weapon.features:
  features=weapon.features
  features.sort()
  for feature in features:
   outStr+=feature+', '
  outStr=outStr[:-2]
 outStr+=' & '

 isRanged=weapon.wType is not None
 if isRanged:
  outStr+=weapon.wType
  outStr+='/'
  if weapon.wType=='М':
   outStr+='-'
  elif weapon.wType=='Ф':
   outStr+='-'
  elif weapon.wType=='Э':
   outStr+='*'
  else:
   outStr+=str(weapon.clipSize) if weapon.clipSize is not None else '\\err'
  outStr+='/'
  outStr+=str(weapon.rateOfFire) if weapon.rateOfFire is not None else '\\err'
  outStr+=' & '
  outStr+=str(weapon.shortDist) if weapon.shortDist is not None else '\\err'
  outStr+='/'
  outStr+=str(weapon.longDist) if weapon.longDist is not None else '\\err'
 else:
  outStr+='-'
  outStr+=' & '
  outStr+='Ближ. бой'
 outStr+=' & '

 bonus=calcBonus(weapon,hero)
 dmg0=weapon.dmg0+bonus
 dmg1=weapon.dmg1+bonus

 if dmg0 is not None:
  if dmg0>0:
   outStr+='+'
  outStr+=str(dmg0)
 else:
  outStr+='\\err'
 secondary=dmg1 is not None
 if isRanged or secondary:
  outStr+='/'
  if secondary:
   if dmg1>0:
    outStr+='+'
   outStr+=str(dmg1)
  else:
   outStr+='\\err'
 outStr+=' & '

 if weapon.dmgType is not None:
 checkKey('тип Пв',entity)
 outStr+=entity.get('тип Пв')
 outStr+=' & '

 if weapon.crit is None or weapon.crit<1 or weapon.crit>20:
  outStr+='\\err'
 else:
  outStr+=str(weapon.crit)
  if weapon.crit<20
   outStr+='+'
 outStr+='\\\\ '
 if weapon.wType is not None:
  if weapon.wType='М' and 'Снаряды' not in weapon.features:
   outStr+=genSubLine(weapon,hero)
 outStr+='\\hline '
 return outStr

def genSubLine(weapon,hero):
 outStr=' & '
 outStr=' & '
 outStr+='-'
 outStr+=' & '
 outStr+='Ближ. бой'
 outStr+=' & '
 weapon.wType=None
 bonus=calcBonus(weapon,hero)
 dmg0=weapon.dmg0+bonus

 if dmg0 is not None:
  if dmg0>0:
   outStr+='+'
  outStr+=str(dmg0)
 else:
  outStr+='\\err'
 outStr+=' & '
 outStr+=' & '
 outStr+='\\\\ '
 return outStr
