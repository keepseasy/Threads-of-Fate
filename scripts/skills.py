from genLib import getName as sortKey
from genLib import pureGen

def genEntity(entityDict,idx,form):
 outStr=''
 for key in entityDict:
  entity=entityDict.get(key)
  outStr+='\\subsection{'+key
  outStr+='('+entity.get('часто используемые Характеристики','\\err не заданы Характеристики')
  outStr+=')}\\paragraph{}'+entity.get('описание','\\err не задано описание')
  outStr+='\\paragraph{Используйте Навык, если герой:} '+entity.get('когда использовать','\\err не описаны условия использования')

 return outStr

#[название] :
#  часто используемые Характеристики: ...
#  описание: ...
#  когда использовать: ...
