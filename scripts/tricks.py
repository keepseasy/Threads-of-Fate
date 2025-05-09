from scripts.genLib import getName as sortKey
from scripts.genLib import pureGen
from scripts.genLib import try_to_get

def genEntity(entityDict,idx,form):
  outStr=''
  for key in entityDict:
    entity=entityDict.get(key)
    outStr+='\\subsubsection{'+key
    if 'Могущество' in entity:
      outStr+='[Могущество]'
    outStr+='}'
    outStr+='\\index['+idx+']{'+key+'}'
    outStr+='\\paragraph{}'+try_to_get('описание', entity, key)
    if 'Свойства' in entity:
      props = entity.get('Свойства')
      outStr+='\\begin{itemize}'
      for prop in props:
        outStr+='\\item[--] '+prop
      outStr+='\\end{itemize}'
    

  return outStr

# [название]:
#   Могущество: #опционально
#   описание: ...
