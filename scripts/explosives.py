from genLib import getName as sortKey
from genLib import pureGen

def genEntity(entityDict):
 outStr=''
 outStr+='\\begin{center}'
 outStr+='\\begin{tabular}{ |p{2.5cm}|p{7cm}||c|c|c||c|c| }'
 outStr+='\\hline'
 outStr+='Название & Дополнительные эффекты & СВ & РВ & ТПв & тСл & СП\\\\ \\hline'
 outStr+='\\hline'

 for key in entityDict:
  entity=entityDict.get(key)
  outStr+=key

  if 'фантастическое' in entity: outStr+='\\textsuperscript{ф}'
  outStr+=' & '

  outStr+=entity.get('дополнительные Эффекты','-')
  outStr+=' & '

  outStr+=entity.get('Сила Взрыва','\\err')
  outStr+=' & '

  outStr+=entity.get('Радиус Взрыва','\\err')
  outStr+=' & '

  outStr+=entity.get('Тип ПВ','\\err')
  outStr+=' & '

  outStr+=entity.get('требуемая Сила','-')
  outStr+=' & '

  outStr+=entity.get('СП','\\err')
  outStr+='\\\\ \\hline'

 outStr+='\\end{tabular}\\end{center}'
 return outStr

#название:
#  фантастическое:
#  требуемая Сила:
#  Сила Взрыва:
#  Радиус Взрыва:
#  Тип ПВ:
#  дополнительные Эффекты:
#  СП:
