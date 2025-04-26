from scripts.genLib import getName as sortKey
from scripts.genLib import pureGen

def genEntity(entityDict,idx,form):
  outStr=''
  for key in entityDict:
    entity=entityDict.get(key)
    if 'расширенная версия' in entity:
      outStr+='\\ifx\\islight\\undefined '
    outStr+='\\subsection{'+key
    outStr+='('+entity.get('часто используемые Характеристики','\\err не заданы Характеристики')
    outStr+=')}\\paragraph{}'+entity.get('описание','\\err не задано описание')
    outStr+='\\paragraph{Используйте Навык, если герой:} '+entity.get('когда использовать','\\err не описаны условия использования')
    if 'расширенная версия' in entity:
      outStr+='\\fi '

  return outStr

#[название] :
#  часто используемые Характеристики: ...
#  описание: ...
#  когда использовать: ...
