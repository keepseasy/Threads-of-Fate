from genLib import checkKey
from genLib import tryInt
from genLib import tryFloat
from genLib import getOptional
def pureGen():
 return False
import re
def sortKey(dict):
 if not ('Скорость' in dict):
  return -1

 spdStr=dict.get('Скорость')
 if not type(spdStr)==str:
  return -1

 match=re.search(r'\d+', spdStr)
 if not match:
  return -1

 numStr=match.group(0)
 if numStr=='':
  return -1

 return int(numStr)

def genEnv(val)
 if type(val) != str:
  return '\\err'
 if val == 'Водный':
  return 'В'
 if val == 'Летающий':
  return 'Л'
 if val == 'Космический':
  return 'К'
 return '\\err'

def genLine(entity):
 outStr=''

 checkKey('название',entity)
 outStr+=entity.get('название')
 if checkKey('фантастический',entity,keep=True):
  outStr+='\\textsuperscript{ф}'
 outStr+=' & '

 checkKey('Размер',entity)
 outStr+=entity.get('Размер')
 if checkKey('животное',entity,keep=True):
  outStr+='(Ж)'
 outStr+=' & '

 checkKey('Защита',entity)
 outStr+=entity.get('Защита')
 outStr+=' & '

 outStr+=getOptional('Прочность',entity)
 outStr+=' & '

 checkKey('ЕЗ',entity)
 outStr+=entity.get('ЕЗ')
 outStr+=' & '

 outStr+=getOptional('ограничение Модификатора Ловкости',entity)
 outStr+=' & '

 checkKey('Проходимость',entity)
 outStr+=entity.get('Проходимость')
 env=''
 if checkKey('Тип передвижения',entity,keep=True):
  env=genEnv(entity.get('Тип передвижения'))
  outStr+=env
 outStr+=' & '

 if env == 'К':
  outStr+='-'
 else:
  checkKey('Скорость',entity)
  outStr+=entity.get('Скорость')
  if checkKey('Не разгоняется',entity,keep=True):
   outStr+='М'
 outStr+=' & '

 checkKey('Грузоподъемность-вес',entity)
 outStr+=entity.get('Грузоподъемность-вес')
 outStr+=' & '

 outStr+=getOptional('Расход',entity)
 outStr+=' & '

 outStr+=getOptional('СП',entity)
 outStr+='\\\\ \\hline'
 return outStr

def genEntity(entityList):
 outStr=''
 outStr+='\\begin{center}'
 outStr+='\\begin{longtable}{|p{2.5cm}||c|c|c|c|c||c|c|c|c|c|c|}'
 outStr+='\\hline'
 outStr+='Название & Размер & Зщ & & Прч & ЕЗ & оМЛв & П & Ск & ГВ & Р & СП\\\\ \\hline'
 outStr+='\\hline'

 for entity in entityList:
  outStr+=genLine(entity)

 outStr+='\\end{longtable}'
 outStr+='\\end{center}'
 outStr+='*Через черту указана максимальная грузоподъемность полуприцепа, который может перевозить тягач.'
 outStr+='\\newline'
 outStr+='**Скорость транспорта определена в его Описании.'
 for entity in entityList:
  outStr+='\\paragraph{'+entity.get('название')+'}'
  checkKey('описание',entity)
  outStr+=entity.get('описание')

 return outStr

# { "название":"",
#   "животное":"Да",
#   "фантастический":"Да",

#   "описание":"",

#   "Размер":"",
#   "Защита":"",
#   "Прочность":"",
#   "ЕЗ":"",
#   "ограничение Модификатора Ловкости":"",

#   "Проходимость":"",
#   "летающий":"Да",
#   "Скорость":"",
#   "Не разгоняется":"Да",
#   "Грузоподъемность-вес":"",
#   "Расход":"",
#   "СП":""
# },