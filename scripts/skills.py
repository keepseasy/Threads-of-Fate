from genLib import checkKey
from genLib import sortKey
def pureGen():
 return False

def genEntity(entityList):
 outStr=''
 for entity in entityList:
  checkKey('название',entity)
  checkKey('описание',entity)
  checkKey('часто используемые Характеристики',entity)
  checkKey('когда использовать',entity)

  outStr+='\\subsection{'+entity.get('название')
  outStr+='('+entity.get('часто используемые Характеристики')
  outStr+=')}\\paragraph{}'+entity.get('описание')
  outStr+='\\paragraph{Используйте Навык, если герой:} '+entity.get('когда использовать')

 return outStr

# { "название" : "",
#   "часто используемые Характеристики" : "",
#   "описание" : "",
#   "когда использовать" : ""
# },