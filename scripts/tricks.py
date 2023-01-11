from genLib import getName as sortKey
from genLib import pureGen

def genEntity(entityDict):
 outStr=''
 for key in entityDict:
  entity=entityDict.get(key)
  outStr+='\\subsection{'+key
  if 'Могущество' in entity:
   outStr+='[Могущество]'
  outStr+='}\\paragraph{}'+entity.get('описание','\\err не задано описание')
 return outStr

# [название]:
#   Могущество: #опционально
#   описание: ...
