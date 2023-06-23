from genLib import pureGen
from genLib import getName as sortKey

def genEntity(entityDict,idx,form):
 outStr=''
 for key in entityDict:
  entity=entityDict.get(key)
  outStr+='\\subsection{'+key+'}'
  outStr+='\\textbf{Риск:}'+entity.get('риск','\\err не задан риск')
  outStr+='\\newline\\textbf{СП:}'+entity.get('СП','\\err не задана СП')
  outStr+='\\paragraph{Описание:}'+entity.get('описание','\\err не задано описание')
  outStr+='\\paragraph{Эффекты:}'+entity.get('эффекты','\\err не заданы эффекты')
  outStr+='\\paragraph{Проблемы:}'+entity.get('проблемы','\\err не заданы проблемы')
 return outStr

#[название]:
#  описание: 
#  эффекты: 
#  проблемы: 
#  риск: 
#  СП: 
