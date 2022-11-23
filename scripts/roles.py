from genLib import checkKey
from genLib import sortKey
def pureGen():
 return False

def genEntity(entityList):
 outStr='Чтобы определить Амплуа случайным образом, бросьте К20 и сверьтесь с результатом.'
 outStr+='\\begin{center}\\begin{tabular}{ |c|p{12cm}|c| }\\hline \\textbf{К20} & \\textbf{Если...} & \\textbf{...то герой} \\\\ \\hline '

 for entity in entityList:
  checkKey('результат Броска',entity)
  checkKey('название',entity)
  checkKey('описание',entity)

  outStr+='\\textbf{'+entity.get('результат Броска')
  outStr+='} & '+entity.get('описание')
  outStr+=' & '+entity.get('название')
  outStr+=' \\\\ \\hline '

 outStr+='\\end{tabular}\\end{center}'
 outStr+='Чтобы определить Грань случайным образом, бросьте К20 и сверьтесь с результатом.'

 for entity in entityList:

  outStr+='\\subsection{'+entity.get('название')
  outStr+='}\\begin{center}\\begin{tabular}{ p{1cm} p{15cm} }'

  variants=entity.get('Грань')
  for variant in variants:
   checkKey('результат Броска',variant)
   checkKey('Орел',variant)
   checkKey('Решка',variant)

   outStr+=variant.get('результат Броска')
   outStr+='. & '+variant.get('Орел')
   outStr+=', \\textbf{НО} '+variant.get('Решка')
   outStr+=' \\\\'
  outStr+='\\end{tabular}\\end{center}'
 return outStr
