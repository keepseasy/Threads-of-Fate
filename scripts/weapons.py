from genLib import checkKey
from genLib import tryInt
from genLib import tryFloat
from genLib import getOptional
from genLib import sortKey
def pureGen():
 return False

def genLine(entity,monster=False):
 outStr=''
 checkKey('название',entity)
 outStr+=entity.get('название')
 if not monster and checkKey('особые свойства',entity,keep=True):
  outStr+='*'
 if checkKey('фантастическое',entity):
  outStr+='\\textsuperscript{ф}'
 outStr+=' & '
 if checkKey('свойства',entity,keep=True):
#  outStr+=getOptional('свойства',entity)
  features=entity.get('свойства')
#  print(features)
  features.sort()
  for feature in entity.get('свойства'):
   outStr+=feature+', '
  outStr=outStr[:-2]
 outStr+=' & '

 isRanged=checkKey('тип боеприпасов',entity)
 if isRanged:
  tmp=entity.get('тип боеприпасов')
  outStr+=tmp
  outStr+='/'
  if tmp=='М':
   outStr+='-'
  elif tmp=='Э':
   outStr+='*'
  else:
   checkKey('магазин',entity)
   outStr+=tryInt(entity.get('магазин'))
  outStr+='/'
  checkKey('скорострельность',entity)
  outStr+=tryInt(entity.get('скорострельность'))
 else:
  outStr+='-'
 outStr+=' & '

 if isRanged:
  checkKey('Ближняя Дистанция',entity)
  checkKey('Дальняя Дистанция',entity)
  outStr+=tryInt(entity.get('Ближняя Дистанция'))
  outStr+='/'
  outStr+=tryInt(entity.get('Дальняя Дистанция'))
 else:
  outStr+='Ближ. бой'
 outStr+=' & '

 checkKey('основной БПв',entity)
 dmgStr=tryInt(entity.get('основной БПв'))
 if not dmgStr=='\\err' and not dmgStr=='\\tbd':
  if int(dmgStr)>0:
   outStr+='+'
 outStr+=dmgStr
 secondary=checkKey('дополнительнй БПв',entity)
 if isRanged or secondary:
  outStr+='/'
  dmgStr=tryInt(entity.get('дополнительнй БПв'))
  if not dmgStr=='\\err' and not dmgStr=='\\tbd':
   if int(dmgStr)>0:
    outStr+='+'
  outStr+=dmgStr
 outStr+=' & '

 checkKey('тип Пв',entity)
 outStr+=entity.get('тип Пв')
 outStr+=' & '

 checkKey('КУ',entity)
 tmp=tryInt(entity.get('КУ'))
 if tmp=='\\err' or tmp=='\\tbd':
  outStr+=tmp
 elif int(tmp)==0 or int(tmp)>20:
  outStr+='\\err'
 elif int(tmp)==20:
  outStr+=tmp
 else:
  outStr+=tmp
  outStr+='+'

 outStr+=' & '


 if monster:
  outStr+=getOptional('особые свойства',entity)
 else:
  outStr+=getOptional('требуемая Сила',entity)
  outStr+=' & '

  outStr+=getOptional('СП',entity)
  outStr+=' & '

  outStr+=getOptional('вес',entity)
 outStr+='\\\\ \\hline '

 return outStr

def genEntity(entityList):
 outStr=''
 outStr+='\\begin{center}'
 outStr+='\\begin{longtable}{|p{3cm}|p{2.5cm}||c|c|c|c|c||c|c|c|}'
 outStr+='\\hline '
 outStr+='Название & Свойства & ТМС & Дистанция & '
 outStr+='БПв & ТПв & КУ & тСл & СП & Вес\\\\ \\hline '
 outStr+='\\hline '

 for entity in entityList:
  outStr+=genLine(entity)

 outStr+='\\end{longtable}'
 outStr+='\\end{center}'

 for entity in entityList:
  outStr+='\\paragraph{'+entity.get('название')+'}'
  checkKey('описание',entity)
  outStr+=entity.get('описание')
  if checkKey('особые свойства',entity,keep=True):
   outStr+='\\newline\\textbf{Особые свойства(*): }'+entity.get('особые свойства')

 return outStr

# { "название":"",
#   "фантастическое":"Да",
#   "описание":"",
#   "особые свойства":"",
#   "свойства":"",
#   "тип боеприпасов":"",
#   "магазин":"",
#   "скорострельность":"",
#   "Ближняя Дистанция":"",
#   "Дальняя Дистанция":"",
#   "основной БПв":"",
#   "дополнительнй БПв":"",
#   "тип Пв":"",
#   "КУ":"",
#   "требуемая Сила":"",
#   "СП":"",
#   "вес":""
# },