from genLib import getName as sortKey
from genLib import pureGen

def genEntity(entityDict,idx,form):
 outStr=''
 outStr+='\\begin{center}'
 outStr+='\\begin{tabular}{ |p{2.7cm}|p{7cm}||c|c|c||c|c| }'
 outStr+='\\hline'
 outStr+='Название & Дополнительные эффекты & СВ & РВ & ТПв & тСл & СП\\\\ \\hline'
 outStr+='\\hline'

 for key in entityDict:
  if 'расширенная версия' in entity:
   outStr+='\\ifx\\islight\\undefined '
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
  if 'расширенная версия' in entity:
   outStr+='\\fi '

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
