from genLib import checkKey
from genLib import getOptional
from genLib import sortKey
def pureGen():
 return False

def genEntity(entityList):
 outStr=''
 outStr+='\\begin{center}'
 outStr+='\\begin{tabular}{ |p{2.5cm}|p{7cm}||c|c|c||c|c| }'
 outStr+='\\hline'
 outStr+='Название & Дополнительные эффекты & СВ & РВ & ТПв & тСл & СП\\\\ \\hline'
 outStr+='\\hline'

 for entity in entityList:
  checkKey('название',entity)
  outStr+=entity.get('название')
  if checkKey('фантастическое',entity):
   outStr+='\\textsuperscript{ф}'
  outStr+=' & '

  outStr+=getOptional('дополнительные Эффекты',entity)
  outStr+=' & '

  checkKey('Сила Взрыва',entity)
  outStr+=entity.get('Сила Взрыва')
  outStr+=' & '

  checkKey('Радиус Взрыва',entity)
  outStr+=entity.get('Радиус Взрыва')
  outStr+=' & '

  checkKey('Тип ПВ',entity)
  outStr+=entity.get('Тип ПВ')
  outStr+=' & '

  outStr+=getOptional('требуемая Сила',entity)
  outStr+=' & '

  checkKey('СП',entity)
  outStr+=entity.get('СП')
  outStr+='\\\\ \\hline'

 outStr+='\\end{tabular}\\end{center}'
 return outStr

# { "название":"",
#   "фантастическое":"Да",
#   "требуемая Сила":"",
#   "Сила Взрыва":"",
#   "Радиус Взрыва":"",
#   "Тип ПВ":"",
#   "дополнительные Эффекты":"",
#   "СП":"",
# },