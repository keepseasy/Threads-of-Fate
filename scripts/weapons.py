from genLib import tryInt
from genLib import getName as sortKey
from genLib import pureGen
from genLib import bookmark
from genLib import sortDict

def genLine(key,entity):
 outStr=''
 outStr+=bookmark(key,'weapon')+key
 if 'особые свойства' in entity:
  outStr+='*'
 if 'фантастическое' in entity:
  outStr+='\\textsuperscript{ф}'
 outStr+=' & '
 if 'свойства' in entity:
  features=sortDict(entity.get('свойства')).keys()
  joiner=', '
  outStr+=joiner.join(features)
 outStr+=' & '

 tmp=entity.get('тип боеприпасов',False)
 isRanged=bool(tmp)
 if isRanged:
  outStr+=tmp
  outStr+='/'
  if tmp=='М':
   outStr+='-'
  elif tmp=='Э':
   outStr+='*'
  else:
   outStr+=tryInt(entity.get('магазин','\\err'))
  outStr+='/'
  outStr+=tryInt(entity.get('скорострельность','\\err'))
 else:
  outStr+='-'
 outStr+=' & '

 if isRanged:
  outStr+=tryInt(entity.get('Ближняя Дистанция','\\err'))
  outStr+='/'
  outStr+=tryInt(entity.get('Дальняя Дистанция','\\err'))
 else:
  outStr+='Ближ. бой'
 outStr+=' & '

 dmgStr=tryInt(entity.get('основной БПв','\\err'))
 if not dmgStr=='\\err' and not dmgStr=='\\tbd':
  if int(dmgStr)>0:
   outStr+='+'
 outStr+=dmgStr
 secondary=bool(entity.get('дополнительнй БПв',False))
 if isRanged or secondary:
  outStr+='/'
  dmgStr=tryInt(entity.get('дополнительнй БПв','\\err'))
  if not dmgStr=='\\err' and not dmgStr=='\\tbd':
   if int(dmgStr)>0:
    outStr+='+'
  outStr+=dmgStr
 outStr+=' & '

 outStr+=entity.get('тип Пв','\\err')
 outStr+=' & '

 tmp=tryInt(entity.get('КУ','\\err'))
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

 outStr+=entity.get('требуемая Сила','-')
 outStr+=' & '

 outStr+=entity.get('СП','-')
 outStr+=' & '

 outStr+=entity.get('вес','-')
 outStr+='\\\\ \\hline '

 return outStr

def genEntity(entityDict):
 outStr=''
 outStr+='\\begin{center}'
 outStr+='\\begin{longtable}{|p{3cm}|p{2.5cm}||c|c|c|c|c||c|c|c|}'
 outStr+='\\hline '
 outStr+='Название & Свойства & ТМС & Дистанция & '
 outStr+='БПв & ТПв & КУ & тСл & СП & Вес\\\\ \\hline '
 outStr+='\\hline '

 for key in entityDict:
  entity=entityDict.get(key)
  outStr+=genLine(key,entity)

 outStr+='\\end{longtable}'
 outStr+='\\end{center}'

 for key in entityDict:
  entity=entityDict.get(key)

  outStr+='\\paragraph{'+key+'}'
  outStr+=entity.get('описание','\\err нет описания')
  special=entity.get('особые свойства',None)
  if special is not None:
   outStr+='\\newline\\textbf{Особые свойства(*): }'+special

 return outStr

# [название]:
#   фантастическое: #необязательно
#   описание: ...
#   особые свойства: ...
#   свойства: ...
#   тип боеприпасов: ...
#   магазин: ...
#   скорострельность: ...
#   Ближняя Дистанция: ...
#   Дальняя Дистанция: ...
#   основной БПв: ...
#   дополнительнй БПв: ...
#   тип Пв: ...
#   КУ: ...
#   требуемая Сила: ...
#   СП: ...
#   вес: ...
