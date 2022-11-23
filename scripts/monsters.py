import math
from genLib import checkKey
from genLib import tryInt
from genLib import sortKey
from genLib import genProps
from weapons import genLine
def pureGen():
 return False

def genStat(val):
 if val.isdigit():
  mod=int(val)
  mod=math.floor((int(val)-10)/2)
  return val+'('+str(mod)+')'
 else:
  return '\\err'

def genEntity(entityList):
 outStr=''
 for entity in entityList:
  checkKey('Сила',entity)
  checkKey('Ловкость',entity)
  checkKey('Вспыльчивость',entity)
  checkKey('Интеллект',entity)
  checkKey('Мудрость',entity)
  checkKey('Обаяние',entity)

  checkKey('Скорость',entity)
  checkKey('Реакция',entity)
  checkKey('Воля',entity)

  checkKey('ЕЗ',entity)
  checkKey('Энергия',entity)
  checkKey('Нити',entity)

  checkKey('Размер',entity)
  checkKey('защита',entity)

  checkKey('название',entity)
  outStr+='\\subsection{'+entity.get('название')
  outStr+='}'

  outStr+='\\begin{center}'
  outStr+='\\begin{longtable}{l l l l l l l l l l}'

  outStr+='\\textbf{Сл:}'
  outStr+=' & '+genStat(entity.get('Сила'))
  outStr+=' & \\textbf{Ин:}'
  outStr+=' & '+genStat(entity.get('Интеллект'))
  outStr+=' & \\textbf{Скорость:}'
  outStr+=' & '+tryInt(entity.get('Скорость'))
  outStr+=' & \\textbf{ЕЗ:}'
  outStr+=' & '+tryInt(entity.get('ЕЗ'))
  outStr+=' & \\textbf{Размер:}'
  outStr+=' & '+entity.get('Размер')
  outStr+='\\\\'

  outStr+='\\textbf{Лв:}'
  outStr+=' & '+genStat(entity.get('Ловкость'))
  outStr+=' & \\textbf{Мд:}'
  outStr+=' & '+genStat(entity.get('Мудрость'))
  outStr+=' & \\textbf{Реакция:}'
  outStr+=' & '+tryInt(entity.get('Реакция'))
  outStr+=' & \\textbf{Энергия:}'
  outStr+=' & '+tryInt(entity.get('Энергия'))
  outStr+=' & \\textbf{Защита:}'
  outStr+=' & '+tryInt(entity.get('защита'))
  outStr+='\\\\'

  outStr+='\\textbf{Вн:}'
  outStr+=' & '+genStat(entity.get('Вспыльчивость'))
  outStr+=' & \\textbf{Об:}'
  outStr+=' & '+genStat(entity.get('Обаяние'))
  outStr+=' & \\textbf{Воля:}'
  outStr+=' & '+tryInt(entity.get('Воля'))
  outStr+=' & \\textbf{Нити:}'
  outStr+=' & '+tryInt(entity.get('Нити'))
  outStr+=' & '
  outStr+=' & '
  outStr+='\\\\'
  outStr+='\\end{longtable}'
  outStr+='\\end{center}'

  outStr+='\\paragraph{Атаки}'
  if checkKey('атаки',entity):
   attacks=entity.get('атаки')
   outStr+='\\begin{center}'
   outStr+='\\begin{longtable}{|p{3cm}|p{2.5cm}|c|c|c|c|c|p{4cm}|}'
   outStr+='\\hline '
   outStr+='Название & Свойства & КМС & Дистанция & '
   outStr+='БПв & ТПв & КУ & Особые свойства\\\\ \\hline '
   for attack in attacks:
    outStr+=genLine(attack,monster=True)
   outStr+='\\end{longtable}'
   outStr+='\\end{center}'
  else:
   outStr+='\\tbd'


  checkKey('описание',entity)
  outStr+='\\paragraph{}'+entity.get('описание')

  if checkKey('Навыки',entity,keep=True):
   outStr+='\\paragraph{Навыки: }'
   outStr+=genProps('Навыки',entity,short=True)

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

# {"название":"(Название Существа)",
#  "описание":"(Описание Существа)",
#  "Сила":"",
#  "Ловкость":"",
#  "Вспыльчивость":"",
#  "Интеллект":"",
#  "Мудрость":"",
#  "Обаяние":"",
#  
#  "Скорость":"(Скорость Существа)",
#  "Реакция":"(Реакция Существа)",
#  "Воля":"(Воля Существа)",
#
#  "ЕЗ":"(Количество ЕЗ Существа)",
#  "Энергия":"(Количество ЭН Существа)",
#  "Нити":"(Количество Нитей, когда существо входит в игру)",
#
#  "защита":"(Защита Существа)",
#  "атаки":[
#    (структуру брать из оружия)
#  ],
#  "Навыки":[
#    {"(Название Навыка)":"(Значение Навыка)"},
#    {"(Название Навыка)":"(Значение Навыка)"}
#  ],
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