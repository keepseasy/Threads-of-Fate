from genLib import checkKey
from genLib import tryInt
from genLib import tryFloat
from genLib import getOptional
from genLib import sortKey
def pureGen():
 return False

def genEnv(val):
 if type(val) != str:
  return '\\err'
 if val == 'Водный':
  return 'В'
 if val == 'Летающий':
  return 'Л'
 if val == 'Космический':
  return 'К'
 return '\\err'

def genEntity(entityList):
 outStr=''
 for entity in entityList:
  checkKey('название',entity)
  outStr+='\\paragraph{'+entity.get('название')
  if checkKey('фантастический',entity,keep=True):
   outStr+='\\textsuperscript{ф}'
  outStr+='}'

  env=''
  if checkKey('Тип передвижения',entity,keep=True):
   env=genEnv(entity.get('Тип передвижения'))

  outStr+='Скорость '
  if env == 'К':
   outStr+='-'
  else:
   checkKey('Скорость',entity)
   outStr+=entity.get('Скорость')
   if checkKey('Не разгоняется',entity,keep=True):
    outStr+='М'
  outStr+='. '

  outStr+='Проходимость '
  checkKey('Проходимость',entity)
  outStr+=entity.get('Проходимость')
  outStr+=env
  outStr+='.'

  checkKey('описание',entity)
  outStr+='\\newline'+entity.get('описание')

 return outStr

#- название: 
#  описание: ""
#  Проходимость: 
#  Скорость: 
#  Тип передвижения: 