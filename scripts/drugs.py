from genLib import checkKey
from genLib import getOptional
from genLib import sortKey
#from genLib import genProps
from genLib import tryInt
def pureGen():
 return False

def genLine(entity):
 outStr=''
 checkKey('название',entity)
 outStr+='\\textbf{'+entity.get('название')

 if checkKey('Можно нанести на оружие',entity,keep=True):
  outStr+='\\newline [Масло]'
 outStr+='}'

 outStr+='\\newline\\textit{Токсичность }'
 checkKey('Токсичность',entity)
 outStr+=tryInt(entity.get('Токсичность'))

 outStr+='\\newline\\textit{СП }'
 checkKey('СП',entity)
 outStr+=tryInt(entity.get('СП'))
 outStr+=' & '

 outStr+=getOptional('Первичный эффект',entity)
 outStr+=' & '

 outStr+=getOptional('Эффект Интоксикации',entity)
 return outStr

def genEntity(entityList):
 outStr=''
 outStr+='\\begin{center}'
 outStr+='\\begin{longtable}{|p{3cm}|p{6.5cm}|p{6.5cm}|}'
 outStr+='\\hline '
 outStr+=' & '
 outStr+='\\textbf{Первичный эффект}'
 outStr+=' & '
 outStr+='\\textbf{Эффект Интоксикации}'
 outStr+='\\\\ '
 outStr+='\\hline '
 for entity in entityList:
  outStr+=genLine(entity)
  outStr+='\\\\ \\hline '

 outStr+='\\end{longtable}'
 outStr+='\\end{center}'

 return outStr

# {"название":"",
#  "Можно нанести на оружие":"Да",
#  "Токсичность":"",
#  "СП":"",
#  "Первичный эффект":"",
#  "Эффект Интоксикации":""
# },