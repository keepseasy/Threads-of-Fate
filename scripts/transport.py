from genLib import checkKey
from genLib import tryInt
from genLib import tryFloat
from genLib import getOptional
from genLib import pureGen

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

def genLine(key,entity):
 outStr=''
 outStr+=key
 if 'фантастический' in entity:
  outStr+='\\textsuperscript{ф}'
 outStr+=' & '

 outStr+=entity.get('Размер','\\err')
 if 'животное' in entity:
  outStr+='(Ж)'
 outStr+=' & '

 outStr+=entity.get('Защита','\\err')
 outStr+=' & '

 outStr+=entity.get('Прочность','-')
 outStr+=' & '

 checkKey('ЕЗ',entity)
 outStr+=entity.get('ЕЗ','\\err')
 outStr+=' & '

 outStr+=entity.get('ограничение Модификатора Ловкости','-')
 outStr+=' & '

 outStr+=entity.get('Проходимость','\\err')
 env=''
 if 'Тип передвижения' in entity:
  env=genEnv(entity.get('Тип передвижения'))
  outStr+=env
 outStr+=' & '

 if env == 'К':
  outStr+='-'
 else:
  outStr+=entity.get('Скорость','\\err')
  if 'Не разгоняется' in entity:
   outStr+='М'
 outStr+=' & '

 outStr+=entity.get('Грузоподъемность-вес','\\err')
 outStr+=' & '

 outStr+=entity.get('Расход','-')
 outStr+=' & '

 outStr+=entity.get('СП','-')
 outStr+='\\\\ \\hline'
 return outStr

def genEntity(entityDict):
 outStr=''
 outStr+='\\begin{center}'
 outStr+='\\begin{longtable}{|p{2.5cm}||c|c|c|c|c||c|c|c|c|c|c|}'
 outStr+='\\hline'
 outStr+='Название & Размер & Зщ & Прч & ЕЗ & оМЛв & П & Ск & ГВ & Р & СП\\\\ \\hline'
 outStr+='\\hline'

 for key in entityDict:
  entity=entityDict.get(key)
  outStr+=genLine(key,entity)

 outStr+='\\end{longtable}'
 outStr+='\\end{center}'
 outStr+='*Через черту указана максимальная грузоподъемность полуприцепа, который может перевозить тягач.'
 outStr+='\\newline'
 outStr+='**Скорость транспорта определена в его Описании.'
 for key in entityDict:
  entity=entityDict.get(key)
  outStr+='\\paragraph{'+key+'}'
  outStr+=entity.get('описание','\\err нет описания')

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