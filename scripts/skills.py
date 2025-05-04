from scripts.genLib import getName as sortKey
from scripts.genLib import pureGen
from scripts.genLib import try_to_get

def genEntity(entityDict,idx,form):
  outStr=''
  for key in entityDict:
    entity=entityDict.get(key)
    if 'расширенная версия' in entity:
      outStr+='\\ifx\\islight\\undefined '
    outStr+='\\subsection{'+key
    outStr+='('+try_to_get('часто используемые Характеристики', entity, key)
    outStr+=')}\\paragraph{}'+try_to_get('описание', entity, key)
    outStr+='\\paragraph{Используйте Навык, если герой:} '+try_to_get('когда использовать', entity, key)
    if 'расширенная версия' in entity:
      outStr+='\\fi '

  return outStr

#[название] :
#  часто используемые Характеристики: ...
#  описание: ...
#  когда использовать: ...
