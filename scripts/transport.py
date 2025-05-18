from scripts.genLib import pureGen
from scripts.genLib import try_to_get

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

# def genEnv(val):
#  if type(val) != str:
#   return '\\err'
#  if val == 'Водный':
#   return 'В'
#  if val == 'Летающий':
#   return 'Л'
#  if val == 'Космический':
#   return 'К'
#  return '\\err'

def genLine(key,entity):
 outStr=''
 outStr+=key
 if 'фантастический' in entity:
  outStr+='\\textsuperscript{ф}'
 outStr+=' & '

 outStr+=try_to_get('Размер', entity, key)+' & '
 outStr+=try_to_get('Защита', entity, key)+' & '
 outStr+=entity.get('Прочность','-')+' & '
 outStr+=try_to_get('ЕЗ', entity, key)+' & '
 outStr+=entity.get('ограничение Модификатора Ловкости','-')+' & '
 outStr+=try_to_get('Проходимость', entity, key)+' & '

 if entity.get('Форма','') == 'Космический':
  outStr+='-'
 else:
  outStr+=try_to_get('Скорость', entity, key)
  if 'Не разгоняется' in entity:
   outStr+='М'
 outStr+=' & '

 outStr+=try_to_get('Грузоподъемность-вес', entity, key)+' & '
 outStr+=entity.get('Расход','-')+' & '
 outStr+=entity.get('СП','-')
 outStr+='\\\\ \\hline'
 return outStr

def genEntity(entityDict,idx,form):
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
 outStr+='** Скорость транспорта определена в его Описании.'
 for key in entityDict:
  entity=entityDict.get(key)
  outStr+='\\paragraph{'+key+'}'
  outStr+=try_to_get('описание', entity, key)

 return outStr

# { название:,
#   животное:Да,
#   фантастический:Да,

#   описание:,

#   Размер:,
#   Защита:,
#   Прочность:,
#   ЕЗ:,
#   ограничение Модификатора Ловкости:,

#   Проходимость:,
#   летающий:Да,
#   Скорость:,
#   Не разгоняется:Да,
#   Грузоподъемность-вес:,
#   Расход:,
#   СП:
# },