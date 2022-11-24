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
  outStr+='\\textbf{Базовый предмет: }'
  checkKey('Базовый предмет',entity)
  outStr+=entity.get('Базовый предмет')

  outStr+='\\newline\\textbf{Запас Энергии: }'
  outStr+=getOptional('Запас Энергии',entity)

  outStr+='\\newline\\textbf{СП: }'
  outStr+=getOptional('СП',entity)

  outStr+='\\paragraph{Описание: }'
  checkKey('описание',entity)
  outStr+=entity.get('описание')

  if checkKey('Трюки',entity,keep=True):
   outStr+='\\paragraph{Трюки}\\begin{itemize}'
   outStr+=genProps('Трюки',entity)
   outStr+='\\end{itemize}'
  if checkKey('Функции',entity,keep=True):
   outStr+='\\paragraph{Функции}\\begin{itemize}'
   outStr+=genProps('Функции',entity,costly=True)
   outStr+='\\end{itemize}'
  if checkKey('Ходы',entity,keep=True):
   outStr+='\\paragraph{Ходы}\\begin{itemize}'
   outStr+=genProps('Ходы',entity,costly=True)
   outStr+='\\end{itemize}'
  if checkKey('Изъяны',entity,keep=True):
   outStr+='\\paragraph{Изъяны}\\begin{itemize}'
   outStr+=genProps('Изъяны',entity,costly=True)
   outStr+='\\end{itemize}'
 return outStr

# {"название":"(Название)",
#  "Базовый предмет":"(предмет или оружие, из которого сделан предмет Функции)",
#  "Запас Энергии":"(Описание)",
#  "СП":"(Описание)",
#  "описание":"(Описание)",
#  "Трюки":[
#   {"(Название Трюка)":"(Описание Трюка)"},
#   {"(Название Трюка)":"(Описание Трюка)"}
#  ],
#  "Функции":[
#    {"(Название Функции)":"(Описание Функции)","cost":"(Стоимость Функции)"},
#    {"(Название Функции)":"(Описание Функции)","cost":"(Стоимость Функции)"}
#  ],
#  "Ходы":[
#    {"(Название Хода)":"(Описание Хода)","cost":"(Стоимость Хода)"},
#    {"(Название Хода)":"(Описание Хода)","cost":"(Стоимость Хода)"}
#  ]
#  "Изъяны":[
#    {"(Название Изъяна)":"(Описание Изъяна)"},
#    {"(Название Изъяна)":"(Описание Изъяна)"}
#  ]
# },