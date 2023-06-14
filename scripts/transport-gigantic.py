from genLib import pureGen
from genLib import getName as sortKey

def genEnv(val):
 if val is None:
  return ''
 if type(val) != str:
  return '\\err'
 if val == 'Водный':
  return 'В'
 if val == 'Летающий':
  return 'Л'
 if val == 'Космический':
  return 'К'
 return '\\err'

def genEntity(entityDict,idx):
 outStr=''
 for key in entityDict:
  entity=entityDict.get(key)
  outStr+='\\paragraph{'+key
  if 'фантастический' in entity:
   outStr+='\\textsuperscript{ф}'
  outStr+='}'

  env=genEnv(entity.get('Тип передвижения'))
  outStr+='Скорость '
  if env == 'К':
   outStr+='-'
  else:
   outStr+=entity.get('Скорость','\\err нет скорости')
   if 'Не разгоняется' in entity:
    outStr+='М'
  outStr+='. '

  outStr+='Проходимость '
  outStr+=entity.get('Проходимость','\\err нет проходимости')
  outStr+='. '

  outStr+='Тип передвижения '
  outStr+=entity.get('Тип передвижения','\\err нет Типа передвижения')
  outStr+='.'

  outStr+='\\newline'+entity.get('описание','\\err нет описания')

 return outStr

#[название]:
#  описание: 
#  Проходимость: 
#  Скорость: 
#  Тип передвижения: 