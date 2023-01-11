from genLib import getName as sortKey
from genLib import genProps
from genLib import pureGen

def genEntity(entityDict):
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
  if 'Трюки' in entity:
   outStr+='\\textbf{Трюки}\\begin{itemize}'
   outStr+=genProps(entity.get('Трюки'))
   outStr+='\\end{itemize}'

  if 'Изъяны' in entity:
   outStr+='\\textbf{Изъяны}\\begin{itemize}'
   outStr+=genProps(entity.get('Изъяны'))
   outStr+='\\end{itemize}'

  if 'Функции' in entity:
   outStr+='\\textbf{Функции}\\begin{itemize}'
   outStr+=genProps(entity.get('Функции'))
   outStr+='\\end{itemize}'

  if 'Ходы' in entity:
   outStr+='\\textbf{Ходы}\\begin{itemize}'
   outStr+=genProps(entity.get('Ходы'))
   outStr+='\\end{itemize}'
 return outStr

#- название: "(Название)"
#  Базовый предмет: "(предмет или оружие, из которого сделан предмет Могущества)"
#  Запас Энергии: "(размер)"
#  СП: "(Стоимость)"
#  описание: "(Описание)"
#  Трюки:
#  - "(Название Трюка)": "(Описание Трюка)"
#  - "(Название Трюка)": "(Описание Трюка)"
#
#  Функции:
#  - "(Название Функции)": "(Описание Функции)"
#    стоимость: "(Стоимость Функции)"
#  - "(Название Функции)": "(Описание Функции)"
#    стоимость: "(Стоимость Функции)"
#
#  Ходы:
#  - "(Название Хода)": "(Описание Хода)"
#    стоимость: "(Стоимость Хода)"
#  - "(Название Хода)": "(Описание Хода)"
#    стоимость: "(Стоимость Хода)"