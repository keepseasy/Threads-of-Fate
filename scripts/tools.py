from scripts.genLib import getName as sortKey
from scripts.genLib import genProps
from scripts.genLib import pureGen
from scripts.genLib import try_to_get

def genEntity(entityDict,idx,form):
 outStr=''
 for key in entityDict:
  entity=entityDict.get(key)
  outStr+='\\subsubsection{'+key
  if 'Симбионт' in entity:
    outStr+='[Симбионт]'
  outStr+='}'

  if 'Запас Энергии' in entity:
   outStr+='\\textbf{Запас Энергии: }'
   outStr+=entity.get('Запас Энергии')
   outStr+=' Зр'
   outStr+='\\newline'

  outStr+='\\textbf{СП: }'
  outStr+=entity.get('СП','-')

  if 'Базовый предмет' in entity:
   outStr+='\\newline\\textbf{Базовый предмет: }'
   outStr+=entity.get('Базовый предмет')

  outStr+='\\newline\\textbf{Описание: }'
  outStr+=try_to_get('описание', entity, key)

  if 'Свойства' in entity:
   outStr+='\\paragraph{Свойства}'
   outStr+=genProps(entity.get('Свойства'))

  if 'Изъяны' in entity:
   outStr+='\\paragraph{Изъяны}'
   outStr+=genProps(entity.get('Изъяны'))

  if 'Функции' in entity:
   outStr+='\\paragraph{Функции}'
   outStr+=genProps(entity.get('Функции'))

  # if 'Ходы' in entity:
  #  outStr+='\\paragraph{Ходы}'
  #  outStr+=genProps(entity.get('Ходы'))
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
