from scripts.genLib import getName as sortKey
from scripts.genLib import pureGen
from scripts.genLib import try_to_get

def genEntity(entityDict,idx,form):
  outStr=''
  outStr+='\\begin{center}'
  outStr+='\\begin{tabular}{ |p{2.7cm}|p{7cm}||c|c|c||c|c|c| }'
  outStr+='\\hline'
  outStr+='Название & Дополнительные эффекты & СВ & РВ & ТПв & тСл & СП & Вес \\\\ \\hline'
  outStr+='\\hline'

  for key in entityDict:
    entity=entityDict.get(key)
    outStr+=key

    if 'фантастическое' in entity: outStr+='\\textsuperscript{ф}'
    outStr+=' & '

    outStr+=entity.get('дополнительные Эффекты','-')
    outStr+=' & '

    outStr+=try_to_get('Сила Взрыва', entity, key)
    outStr+=' & '

    outStr+=try_to_get('Радиус Взрыва', entity, key)
    outStr+=' & '

    outStr+=try_to_get('Тип ПВ', entity, key)
    outStr+=' & '

    outStr+=entity.get('требуемая Сила','-')
    outStr+=' & '

    outStr+=try_to_get('СП', entity, key)
    outStr+=' & '

    outStr+=try_to_get('вес', entity, key)
    outStr+='\\\\ \\hline'

  outStr+='\\end{tabular}\\end{center}'
  for key in entityDict:
    entity=entityDict.get(key)
    if 'описание' in entity:
      outStr+='\\paragraph{'+key+': }'
      outStr+=entity.get('описание')
  return outStr

#название:
#  фантастическое:
#  требуемая Сила:
#  Сила Взрыва:
#  Радиус Взрыва:
#  Тип ПВ:
#  дополнительные Эффекты:
#  СП:
