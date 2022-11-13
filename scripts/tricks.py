from genLib import checkKey
from genLib import sortKey

def genEntity(entityList):
 outStr=''
 for entity in entityList:
  checkKey('название',entity)
  outStr+='\\subsection{'+entity.get('название')

  if checkKey('Могущество',entity,keep=True):
   outStr+='[Могущество]'

  checkKey('описание',entity)
  outStr+='}\\paragraph{}'+entity.get('описание')

 return outStr

# {"название":"",
#  "Могущество":"Да",
#  "описание":""
# },