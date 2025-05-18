from scripts.genLib import tryInt
from scripts.genLib import getName as sortKey
from scripts.genLib import pureGen
#from scripts.genLib import bookmark
from scripts.genLib import sortDict
from scripts.genLib import try_to_get
from scripts.genLib import printerr

def genLine(key,entity,idx):
  outStr=''
  outStr+=key
  outStr+=' & '

  outStr+=try_to_get('описание', entity, key)
  outStr+=' & '

  outStr+=try_to_get('СП', entity, key)
  outStr+='\\\\ \\hline'

  return outStr

def genEntity(entityDict,idx,form):
  outStr=''
  outStr+='\\begin{center}'

  outStr+='\\begin{longtable}{|p{4cm}|p{10.0cm}|p{0.7cm}|}'
  outStr+='\\hline '
  outStr+='\\textbf{Название} & \\textbf{Описание} & \\textbf{СП} \\\\ \\hline '

  for key in entityDict:
   entity=entityDict.get(key)
   outStr+=genLine(key,entity,idx)
  # outStr+='\\hline '
  outStr+='\\end{longtable}'
  outStr+='\\end{center}'

  return outStr

# [название]:
#   фантастическое: #необязательно
#   описание: ...
#   особые свойства: ...
#   свойства: ...
#   тип боеприпасов: ...
#   магазин: ...
#   скорострельность: ...
#   Ближняя Дистанция: ...
#   Дальняя Дистанция: ...
#   основной БПв: ...
#   дополнительнй БПв: ...
#   тип Пв: ...
#   КУ: ...
#   требуемая Сила: ...
#   СП: ...
#   вес: ...
