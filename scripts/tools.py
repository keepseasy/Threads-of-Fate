from scripts.genLib import getName as sortKey
from scripts.genLib import genProps
from scripts.genLib import pureGen

def genEntity(entityDict,idx,form):
 outStr=''
 for key in entityDict:
  entity=entityDict.get(key)
  outStr+='\\subsection{'+key+'}'

  if 'Запас Энергии' in entity:
   outStr+='\\textbf{Запас Энергии: }'
   outStr+=entity.get('Запас Энергии')
   outStr+='\\newline'

  outStr+='\\textbf{СП: }'
  outStr+=entity.get('СП','-')

  if 'Базовый предмет' in entity:
   outStr+='\\newline\\textbf{Базовый предмет: }'
   outStr+=entity.get('Базовый предмет')

  outStr+='\\newline\\textbf{Описание: }'
  outStr+=entity.get('описание','\\err нет описания')
  outStr+='\\newline'
  if 'Свойства' in entity:
   outStr+='\\newline\\textbf{Свойства}'
   outStr+=genProps(entity.get('Свойства'))

  if 'Изъяны' in entity:
   outStr+='\\newline\\textbf{Изъяны}'
   outStr+=genProps(entity.get('Изъяны'))

  if 'Функции' in entity:
   outStr+='\\newline\\textbf{Функции}'
   outStr+=genProps(entity.get('Функции'))

  if 'Ходы' in entity:
   outStr+='\\newline\\textbf{Ходы}'
   outStr+=genProps(entity.get('Ходы'))
 return outStr

#- название: (Название)
#  Базовый предмет: (предмет или оружие, из которого сделан предмет Могущества)
#  Запас Энергии: (размер)
#  СП: (Стоимость)
#  описание: (Описание)
#  Свойства:
#  - (Название Трюка): (Описание Трюка)
#  - (Название Трюка): (Описание Трюка)
#
#  Функции:
#  - (Название Функции): (Описание Функции)
#    стоимость: (Стоимость Функции)
#  - (Название Функции): (Описание Функции)
#    стоимость: (Стоимость Функции)
#
#  Ходы:
#  - (Название Хода): (Описание Хода)
#    стоимость: (Стоимость Хода)
#  - (Название Хода): (Описание Хода)
#    стоимость: (Стоимость Хода)
