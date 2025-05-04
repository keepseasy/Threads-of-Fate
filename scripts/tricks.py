from scripts.genLib import getName as sortKey
from scripts.genLib import pureGen
from scripts.genLib import try_to_get

def genEntity(entityDict,idx,form):
 outStr=''
 for key in entityDict:
  entity=entityDict.get(key)
  if 'расширенная версия' in entity:
   outStr+='\\ifx\\islight\\undefined '
  outStr+='\\subsubsection{'+key
  if 'Могущество' in entity:
   outStr+='[Могущество]'
  outStr+='}'
  outStr+='\\index['+idx+']{'+key+'}'
  outStr+='\\paragraph{}'+try_to_get('описание', entity, key)
  if 'расширенная версия' in entity:
   outStr+='\\fi '
 return outStr

# [название]:
#   Могущество: #опционально
#   описание: ...
