from scripts.genLib import pureGen
from scripts.genLib import getName as sortKey
from scripts.genLib import try_to_get

def genEntity(entityDict,idx,form):
 outStr=''
 for key in entityDict:
  entity=entityDict.get(key)
  outStr+='\\subsection{'+key+'}'
  outStr+='\\textbf{Риск:}'+try_to_get('риск', entity, key)
  outStr+='\\newline\\textbf{СП:}'+try_to_get('СП', entity, key)
  outStr+='\\paragraph{Описание:}'+try_to_get('описание', entity, key)
  outStr+='\\paragraph{Эффекты:}'+try_to_get('эффекты', entity, key)
  outStr+='\\paragraph{Проблемы:}'+try_to_get('проблемы', entity, key)
 return outStr

#[название]:
#  описание: 
#  эффекты: 
#  проблемы: 
#  риск: 
#  СП: 
