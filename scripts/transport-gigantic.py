from scripts.genLib import pureGen
from scripts.genLib import getName as sortKey
from scripts.genLib import printerr
from scripts.genLib import try_to_get

def genEnv(val, key):
 if val is None:
  return ''
 if type(val) != str:
  printerr('Ошибка генерации: в записи ' + key + ' не задано свойство: Тип передвижения')
  return ''
 if val == 'Водный':
  return 'В'
 if val == 'Летающий':
  return 'Л'
 if val == 'Космический':
  return 'К'
 printerr('Ошибка генерации: в записи ' + key + ' свойство Тип передвижения задано некорректно')
 return ''

def genEntity(entityDict,idx,form):
 outStr=''
 for key in entityDict:
  entity=entityDict.get(key)
  outStr+='\\paragraph{'+key
  if 'фантастический' in entity:
   outStr+='\\textsuperscript{ф}'
  outStr+='}'

  env=genEnv(entity.get('Тип передвижения'), key)
  outStr+='Скорость '
  if env == 'К':
   outStr+='-'
  else:
   outStr+=try_to_get('Скорость', entity, key)
   if 'Не разгоняется' in entity:
    outStr+='М'
  outStr+='. '

  outStr+='Проходимость '
  outStr+=try_to_get('Проходимость', entity, key)
  outStr+='. '

  outStr+='Тип передвижения '
  outStr+=try_to_get('Тип передвижения', entity, key)
  outStr+='.'

  outStr+='\\newline'+try_to_get('описание', entity, key)

 return outStr

#[название]:
#  описание: 
#  Проходимость: 
#  Скорость: 
#  Тип передвижения: 