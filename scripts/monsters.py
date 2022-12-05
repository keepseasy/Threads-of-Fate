import math
from genLib import checkKey
from genLib import tryInt
from genLib import sortKey
from genLib import genProps
from genLib import genSize
from weapons import genLine
def pureGen():
 return False

def genPimaryMod(val):
 mod=math.floor((val-10)/2)
 outStr='('
 if mod>=0:
  outStr+='+'
 return outStr+str(mod)+')'

def genEntity(entityList):
 outStr=''
 for entity in entityList:
  noSkipRef=checkKey('название',entity)
  entityName=entity.get('название')
  outStr+='\\subsection{'+entityName
  outStr+='}'
  if noSkipRef:
   outStr+='\\hypertarget{monster'+str(hash(entityName))+'}{}'
  else:
   outStr+='\\err не задано название Существа, ссылка не создана!'

  outStr+='\\begin{longtable}{l l l l l l l l l l}'

  STR=int(entity.get('Сила')) if checkKey('Сила',entity,keep=True) else 0
  DEX=int(entity.get('Ловкость')) if checkKey('Ловкость',entity,keep=True) else 0
  CON=int(entity.get('Выносливость')) if checkKey('Выносливость',entity,keep=True) else 0
  INT=int(entity.get('Интеллект')) if checkKey('Интеллект',entity,keep=True) else 0
  WIS=int(entity.get('Мудрость')) if checkKey('Мудрость',entity,keep=True) else 0
  CHA=int(entity.get('Обаяние')) if checkKey('Обаяние',entity,keep=True) else 0

  SIZE=int(entity.get('Размер')) if checkKey('Размер',entity,keep=True) else 0
  HP=int(entity.get('ЕЗ')) if checkKey('ЕЗ',entity,keep=True) else 0
  SPD=int(entity.get('Скорость')) if checkKey('Скорость',entity,keep=True) else 0
  REF=int(entity.get('Реакция')) if checkKey('Реакция',entity,keep=True) else 0
  ENG=int(entity.get('Энергия')) if checkKey('Энергия',entity,keep=True) else 0
  WIL=int(entity.get('Воля')) if checkKey('Воля',entity,keep=True) else 0

  DEF=int(entity.get('Бонус защиты')) if checkKey('Бонус защиты',entity,keep=True) else 0
  LIM=int(entity.get('Ограничение ловкости')) if checkKey('Ограничение ловкости',entity,keep=True) else 1000

  TREADS=entity.get('Нити') if checkKey('Нити',entity,keep=True) else "-"

  template=checkKey('Шаблон',entity,keep=True)
  if not template:
   HP+=(SIZE+3)*CON
   SPD+=math.floor((DEX+CON)/4)+SIZE
   if checkKey('Четвероногое',entity,keep=True):
    SPD*=2
   REF+=math.floor((DEX+WIS)/4)
   ENG+=math.floor((CON+CHA)/4)
   WIL+=math.floor((INT+WIS)/4)
   DEX_BONUS=math.floor((DEX-10)/2)
   if LIM>DEX_BONUS:
    LIM=DEX_BONUS
   DEF+=10+LIM-SIZE

  outStr+='\\textbf{Сл:}'
  outStr+=' & '+str(STR)
  if not template:
   outStr+=genPimaryMod(STR)
  outStr+=' & \\textbf{Ин:}'
  outStr+=' & '+str(INT)
  if not template:
   outStr+=genPimaryMod(INT)
  outStr+=' & \\textbf{Скорость:}'
  outStr+=' & '+str(SPD)
  outStr+=' & \\textbf{ЕЗ:}'
  outStr+=' & '+str(HP)
  if template:
   outStr+=' & '
   outStr+=' & '
  else:
   outStr+=' & \\textbf{Размер:}'
   outStr+=' & '+genSize(SIZE)
  outStr+='\\\\'

  outStr+='\\textbf{Лв:}'
  outStr+=' & '+str(DEX)
  if not template:
   outStr+=genPimaryMod(DEX)
  outStr+=' & \\textbf{Мд:}'
  outStr+=' & '+str(WIS)
  if not template:
   outStr+=genPimaryMod(WIS)
  outStr+=' & \\textbf{Реакция:}'
  outStr+=' & '+str(REF)
  outStr+=' & \\textbf{Энергия:}'
  outStr+=' & '+str(ENG)
  checkKey('защита',entity)
  outStr+=' & \\textbf{Защита:}'
  outStr+=' & '+str(DEF)
  outStr+='\\\\'

  outStr+='\\textbf{Вн:}'
  outStr+=' & '+str(CON)
  if not template:
   outStr+=genPimaryMod(CON)
  outStr+=' & \\textbf{Об:}'
  outStr+=' & '+str(CHA)
  if not template:
   outStr+=genPimaryMod(CHA)
  outStr+=' & \\textbf{Воля:}'
  outStr+=' & '+str(WIL)
  outStr+=' & \\textbf{Нити:}'
  outStr+=' & '+TREADS
  outStr+=' & '
  outStr+=' & '
  outStr+='\\\\'
  outStr+='\\end{longtable}'

  outStr+='\\textbf{Атаки}'
  if checkKey('атаки',entity):
   attacks=entity.get('атаки')
   outStr+='\\begin{longtable}{|p{3cm}|p{2.5cm}|c|c|c|c|c|p{4cm}|}'
   outStr+='\\hline '
   outStr+='Название & Свойства & КМС & Дистанция & '
   outStr+='БПв & ТПв & КУ & Особые свойства\\\\ \\hline '
   for attack in attacks:
    outStr+=genLine(attack,monster=True)
   outStr+='\\end{longtable}'
  else:
   outStr+='\\tbd\\newline'

  checkKey('описание',entity)
  outStr+=entity.get('описание')

  outStr+='\\newline'
  if checkKey('Навыки',entity,keep=True):
   outStr+='\\textbf{Навыки: }'
   outStr+=genProps('Навыки',entity,short=True)
   outStr+='\\newline'

  if checkKey('Трюки',entity,keep=True):
   outStr+='\\textbf{Трюки}\\begin{itemize}'
   outStr+=genProps('Трюки',entity)
   outStr+='\\end{itemize}'
  if checkKey('Могущества',entity,keep=True):
   outStr+='\\textbf{Могущества}\\begin{itemize}'
   outStr+=genProps('Могущества',entity,costly=True)
   outStr+='\\end{itemize}'
  if checkKey('Ходы',entity,keep=True):
   outStr+='\\textbf{Ходы}\\begin{itemize}'
   outStr+=genProps('Ходы',entity,costly=True)
   outStr+='\\end{itemize}'

 return outStr

# {"название":"(Название Существа)",
#  "описание":"(Описание Существа)",
#  "Сила":"",
#  "Ловкость":"",
#  "Выносливость":"",
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