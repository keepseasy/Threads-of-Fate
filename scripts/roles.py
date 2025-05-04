from scripts.genLib import getName as sortKey
from scripts.genLib import pureGen
from scripts.genLib import try_to_get
from scripts.genLib import printerr
def pureGen():
 return False

def genEntity(entityDict,idx,form):
 outStr='Чтобы определить Амплуа случайным образом, бросьте К20 и сверьтесь с результатом.'
 outStr+='\\begin{center}\\begin{tabular}{ |c|p{12cm}|c| }\\hline \\textbf{К20} & \\textbf{Если...} & \\textbf{...то герой} \\\\ \\hline '
 count=0
 for key in entityDict:
  entity=entityDict.get(key)

  count+=1
  outStr+='\\textbf{'+str(count)
  outStr+='} & '+try_to_get('описание', entity, key)
  outStr+=' & '+key
  outStr+=' \\\\ \\hline '
 outStr+='\\end{tabular}\\end{center}'

 if count!=20:
  printerr('Ошибка генерации: в записи ' + key + ' свойство Амплуа содержит не 20 записей')
 outStr+='Чтобы определить Грань случайным образом, бросьте К20 и сверьтесь с результатом.'

 for key in entityDict:
  entity=entityDict.get(key)
  outStr+='\\subsection{'+key+'}'
  outStr+='\\begin{center}\\begin{tabular}{ p{1cm} p{15cm} }'

  variants=entity.get('Грани')
  if variants is None:
   printerr('Ошибка генерации: в записи ' + key + ' не задано свойство: Грани')
  count=0
  for variant in variants:
   pros=list(variant)[0]
   cons=variant.get(pros)
   count+=2
   outStr+=str(count-1)+'-'+str(count)
   outStr+='. & '+pros
   outStr+=', \\textbf{НО} '+cons
   outStr+=' \\\\'
  outStr+='\\end{tabular}\\end{center}'
 if count!=20:
  printerr('Ошибка генерации: в записи ' + key + ' свойство Грани содержит не 10 записей')
 return outStr
