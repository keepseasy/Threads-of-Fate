from genLib import checkKey
from genLib import sortKey

def genEntity(entityList):
 outStr=''
 for entity in entityList:

  checkKey('название',entity)
  outStr+='\\subsection{'+entity.get('название')
  outStr+='}'

  checkKey('риск',entity)
  outStr+='\\newline\\textbf{Риск:}'+entity.get('риск')

  checkKey('СП',entity)
  outStr+='\\newline\\textbf{СП:}'+entity.get('СП')

  checkKey('описание',entity)
  outStr+='\\paragraph{Описание:}'+entity.get('описание')

  checkKey('эффекты',entity)
  outStr+='\\paragraph{Эффекты:}'+entity.get('эффекты')

  checkKey('проблемы',entity)
  outStr+='\\paragraph{Проблемы:}'+entity.get('проблемы')

 return outStr

# {"название":"",
#  "описание":"",
#  "эффекты":"",
#  "проблемы":"",
#  "риск":"",
#  "СП":""
# },