from genLib import pureGen
from genLib import getName as sortKey
from genLib import tryInt

def genLine(key,entity):
 outStr=''
 outStr+='\\textbf{'+key+'}'

# if 'Можно нанести на оружие' in entity: outStr+='\\newline [Масло]'

 outStr+='\\newline\\textit{Токсичность }'
 outStr+=tryInt(entity.get('Токсичность','\\err'))

 outStr+='\\newline\\textit{СП }'
 outStr+=tryInt(entity.get('СП'))
 outStr+=' & '

 outStr+=entity.get('Первичный эффект','-')
 outStr+=' & '

 outStr+=entity.get('Эффект Интоксикации','-')
 return outStr

def genEntity(entityDict,idx,form):
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
 for key in entityDict:
  if 'расширенная версия' in entity:
   outStr+='\\ifx\\islight\\undefined '
  entity=entityDict.get(key)
  outStr+=genLine(key,entity)
  outStr+='\\\\ \\hline '
  if 'расширенная версия' in entity:
   outStr+='\\fi '
 outStr+='\\end{longtable}'
 outStr+='\\end{center}'

 return outStr

#[название]:
##  Можно нанести на оружие:
#  Токсичность:
#  СП:
#  Первичный эффект:
#  Эффект Интоксикации: