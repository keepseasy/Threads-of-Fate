from scripts.genLib import pureGen
from scripts.genLib import getName as sortKey
from scripts.genLib import tryInt
from scripts.genLib import try_to_get
from scripts.genLib import printerr

# def genLine(key,entity):
#  outStr=''
#  outStr+='\\textbf{'+key+'}'

# # if 'Можно нанести на оружие' in entity: outStr+='\\newline [Масло]'

#  outStr+='\\newline\\textit{Токсичность }'
#  outStr+=tryInt(try_to_get('Токсичность', entity, key))

#  outStr+='\\newline\\textit{СП }'
#  outStr+=tryInt(entity.get('СП'))
#  outStr+=' & '

#  outStr+=entity.get('Первичный эффект','-')
#  outStr+=' & '

#  outStr+=entity.get('Побочки','-')
#  return outStr

def genEntity(entityDict,idx,form):
  outStr=''
  for key in entityDict:
    entity=entityDict.get(key)

    outStr+='\\subsubsection{'+key+'}'
    outStr+='\\index['+idx+']{'+key+'}'

    outStr+='\\begin{center}'
    outStr+='\\begin{tabular}{p{3cm} p{3cm} p{10cm} }'

    outStr+='\\textit{Токсичность '
    outStr+=tryInt(try_to_get('Токсичность', entity, key))
    outStr+='} & '

    outStr+='\\textit{СП '
    outStr+=try_to_get('СП', entity, key)
    outStr+='} & '

    if form=='Яд':
      outStr+='\\textit{Условия приема: '
      outStr+=try_to_get('Условия приема', entity, key)
      outStr+='}'
    elif form=='Лекарство':
      outStr+='\\textit{ВП - '
      outStr+=try_to_get('ВП', entity, key)
      outStr+='}'
    else:
      printerr(key + ' имеет неизвестную форму')
    outStr+='\\end{tabular}'
    outStr+='\\end{center}'
    
    outStr+=try_to_get('Описание', entity, key)

    outStr+='\\paragraph{Первичный эффект. }'
    outStr+=try_to_get('Первичный эффект', entity, key)

    outStr+='\\paragraph{Побочки. }'
    outStr+=try_to_get('Побочки', entity, key)

  return outStr

#[название]:
##  Можно нанести на оружие:
#  Токсичность:
#  СП:
#  Первичный эффект:
#  Эффект Интоксикации: