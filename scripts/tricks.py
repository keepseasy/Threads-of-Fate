from scripts.genLib import getName as sortKey
from scripts.genLib import pureGen

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
  outStr+='\\paragraph{}'+entity.get('описание','\\err не задано описание')
  if 'расширенная версия' in entity:
   outStr+='\\fi '
 return outStr

# [название]:
#   Могущество: #опционально
#   описание: ...
