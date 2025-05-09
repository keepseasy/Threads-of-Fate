from scripts.genLib import tryInt
from scripts.genLib import getName as sortKey
from scripts.genLib import pureGen
#from scripts.genLib import bookmark
from scripts.genLib import sortDict
from scripts.genLib import try_to_get
from scripts.genLib import printerr

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
    outStr+=str(try_to_get('магазин', entity, key))
   outStr+='/'
   outStr+=str(try_to_get('скорострельность', entity, key))
  else:
   outStr+='-'
  outStr+=' & '

  if isRanged:
   outStr+=str(try_to_get('Ближняя Дистанция', entity, key))
   outStr+='/'
   outStr+=str(try_to_get('Дальняя Дистанция', entity, key))
  else:
   outStr+='Ближ. бой'
  outStr+=' & '

  if 'основной БПв' in entity:
   val=entity.get('основной БПв')
   outStr+='+' if val>0 else ''
   outStr+=str(val)
  else:
   printerr('Ошибка генерации: в записи ' + key + ' свойство основной БПв не задано')

  val=entity.get('дополнительнй БПв',False)
  if isRanged or val:
   outStr+='/'
   if '' in entity:
    outStr+='+' if val>0 else ''
    outStr+=str(val)
   else:
    printerr('Ошибка генерации: в записи ' + key + ' свойство дополнительнй БПв не задано')
  outStr+=' & '

  outStr+=try_to_get('тип Пв', entity, key)
  outStr+=' & '

  val=entity.get('КУ',0)
  if val>1 and val<=20:
    outStr+=str(val)
  else:
    printerr('Ошибка генерации: в записи ' + key + ' свойство КУ находится вне допустимых пределов')
  outStr+='+' if not val==20 else ''

  outStr+=' & '

  outStr+=entity.get('требуемая Сила','-')
  outStr+=' & '

  outStr+=entity.get('СП','-')
  outStr+=' & '

  outStr+=entity.get('вес','-')
  outStr+='\\\\ \\hline '

  return outStr

def genEntity(entityDict,idx,form):
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
   outStr+=try_to_get('описание', entity, key)
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
