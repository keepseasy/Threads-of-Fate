from scripts.genLib import pureGen
from scripts.genLib import getName as sortKey
from scripts.genLib import try_to_get

def genEntity(entityDict,idx,form):
 outStr=''
 for key in entityDict:
  entity=entityDict.get(key)
  outStr+='\\subsection{'+key
  if 'Отдых' in entity: outStr+=' (Отдых)'
  outStr+='}'
  if 'Антракт' in entity:
    outStr+='\\textbf{Длительность: Антракт}'
  else:
    outStr+='\\textbf{Длительность: Интерлюдия}'
  outStr+='\\newline\\textbf{Риск: }'+try_to_get('риск', entity, key)
  outStr+='\\newline\\textbf{СП: }'+try_to_get('СП', entity, key)
  outStr+='\\paragraph{Описание: }'+try_to_get('описание', entity, key)
  outStr+='\\paragraph{Эффект: }'+try_to_get('эффект', entity, key)
  outStr+='\\paragraph{Проблемы: }'+try_to_get('проблемы', entity, key)
 return outStr

#[название]:
#  описание: 
#  эффекты: 
#  проблемы: 
#  риск: 
#  СП: 
