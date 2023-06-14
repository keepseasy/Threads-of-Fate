from genLib import getName as sortKey
from genLib import pureGen

def genEntity(entityDict,idx):
 outStr=''
 for key in entityDict:
  entity=entityDict.get(key)
  outStr+='\\subsubsection{'+key
  if 'Могущество' in entity:
   outStr+='[Могущество]'
  outStr+='}'
  outStr+='\\index['+idx+']{'+key+'}'
  outStr+='\\paragraph{}'+entity.get('описание','\\err не задано описание')
 return outStr

# [название]:
#   Могущество: #опционально
#   описание: ...
