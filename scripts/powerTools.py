from genLib import checkKey
from genLib import getOptional
from genLib import sortKey
from genLib import genProps
def pureGen():
 return False

def genEntity(entityList):
 outStr=''
 for entity in entityList:

  checkKey('название',entity)
  outStr+='\\subsection{'+entity.get('название')+'}'

  if checkKey('Запас Энергии',entity,keep=True):
   outStr+='\\textbf{Запас Энергии: }'
   outStr+=entity.get('Запас Энергии')
   outStr+='\\newline'

  outStr+='\\textbf{СП: }'
  outStr+=getOptional('СП',entity)

  if checkKey('Базовый предмет',entity,keep=True):
   outStr+='\\newline\\textbf{Базовый предмет: }'
   outStr+=entity.get('Базовый предмет')

  outStr+='\\newline\\textbf{Описание: }'
  checkKey('описание',entity)
  outStr+=entity.get('описание')
  outStr+='\\newline'
  if checkKey('Трюки',entity,keep=True):
   outStr+='\\textbf{Трюки}\\begin{itemize}'
   outStr+=genProps('Трюки',entity)
   outStr+='\\end{itemize}'
  if checkKey('Изъяны',entity,keep=True):
   outStr+='\\textbf{Изъяны}\\begin{itemize}'
   outStr+=genProps('Изъяны',entity)
   outStr+='\\end{itemize}'
  if checkKey('Функции',entity,keep=True):
   outStr+='\\textbf{Функции}\\begin{itemize}'
   outStr+=genProps('Функции',entity,costly=True)
   outStr+='\\end{itemize}'
  if checkKey('Ходы',entity,keep=True):
   outStr+='\\textbf{Ходы}\\begin{itemize}'
   outStr+=genProps('Ходы',entity,costly=True)
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
#    Цена: "(Стоимость Функции)"
#  - "(Название Функции)": "(Описание Функции)"
#    Цена: "(Стоимость Функции)"
#
#  Ходы:
#  - "(Название Хода)": "(Описание Хода)"
#    Цена: "(Стоимость Хода)"
#  - "(Название Хода)": "(Описание Хода)"
#    Цена: "(Стоимость Хода)"