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
  if checkKey('Могущества',entity,keep=True):
   outStr+='\\paragraph{Могущества}\\begin{itemize}'
   outStr+=genProps('Могущества',entity,costly=True)
   outStr+='\\end{itemize}'
  if checkKey('Ходы',entity,keep=True):
   outStr+='\\paragraph{Ходы}\\begin{itemize}'
   outStr+=genProps('Ходы',entity,costly=True)
   outStr+='\\end{itemize}'
 return outStr

# {"название":"(Название)",
#  "Базовый предмет":"(предмет или оружие, из которого сделан предмет Могущества)",
#  "Запас Энергии":"(Описание)",
#  "СП":"(Описание)",
#  "описание":"(Описание)",
#  "Трюки":[
#   {"(Название Трюка)":"(Описание Трюка)"},
#   {"(Название Трюка)":"(Описание Трюка)"}
#  ],
#  "Могущества":[
#    {"(Название Могущества)":"(Описание Могущества)","cost":"(Стоимость Могущества)"},
#    {"(Название Могущества)":"(Описание Могущества)","cost":"(Стоимость Могущества)"}
#  ],
#  "Ходы":[
#    {"(Название Хода)":"(Описание Хода)","cost":"(Стоимость Хода)"},
#    {"(Название Хода)":"(Описание Хода)","cost":"(Стоимость Хода)"}
#  ]
# },