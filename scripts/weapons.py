from genLib import tryInt
from genLib import getName as sortKey
from genLib import pureGen
#from genLib import bookmark
from genLib import sortDict

def genLine(key,entity,idx):
 outStr=''
# outStr+=bookmark(key,'weapon')+key
 outStr+='\\index['+idx+']{'+key+'}'+key
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
   val=entity.get('магазин',False)
   outStr+=str(val) if val else '\\err'
  outStr+='/'
  val=entity.get('скорострельность',False)
  outStr+=str(val) if val else '\\err'
 else:
  outStr+='-'
 outStr+=' & '

 if isRanged:
  val=entity.get('Ближняя Дистанция',False)
  outStr+=str(val) if val else '\\err'
  outStr+='/'
  val=entity.get('Дальняя Дистанция',False)
  outStr+=str(val) if val else '\\err'
 else:
  outStr+='Ближ. бой'
 outStr+=' & '

 if 'основной БПв' in entity:
  val=entity.get('основной БПв')
  outStr+='+' if val>0 else ''
  outStr+=str(val)
 else:
  outStr+='\\err'

 val=entity.get('дополнительнй БПв',False)
 if isRanged or val:
  outStr+='/'
  if 'дополнительнй БПв' in entity:
   outStr+='+' if val>0 else ''
   outStr+=str(val)
  else:
   outStr+='\\err'
 outStr+=' & '

 outStr+=entity.get('тип Пв','\\err')
 outStr+=' & '

 val=entity.get('КУ',0)
 outStr+=str(val) if val>1 and val<=20 else '\\err'
 outStr+='+' if val==20 else ''

 outStr+=' & '

 outStr+=entity.get('требуемая Сила','-')
 outStr+=' & '

 outStr+=entity.get('СП','-')
 outStr+=' & '

 outStr+=entity.get('вес','-')
 outStr+='\\\\ \\hline '

 return outStr

def genEntity(entityDict,idx):
 outStr=''
 outStr+='\\begin{center}'
 outStr+='\\begin{longtable}{|p{3cm}|p{2.5cm}||c|c|c|c|c||c|c|c|}'
 outStr+='\\hline '
 outStr+='Название & Свойства & ТМС & Дистанция & '
 outStr+='БПв & ТПв & КУ & тСл & СП & Вес\\\\ \\hline '
 outStr+='\\hline '

 for key in entityDict:
  entity=entityDict.get(key)
  outStr+=genLine(key,entity,idx)

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
