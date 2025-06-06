from scripts.genLib import pureGen
from scripts.genLib import try_to_get
def sortKey(dict1):
 entity=list(dict1)[1]
 return int(entity.get('бонус Защиты','-1'))

def genLine(key,entity,form):
  outStr=''
  outStr+=key
  if 'особые свойства' in entity:
    outStr+='*'
  if 'фантастическое' in entity:
    outStr+='\\textsuperscript{ф}'
  outStr+=' & '

  outStr+='+'+try_to_get('бонус Защиты', entity, key)
  outStr+=' & '

  if form=='Щит':
    if 'БПв' in entity:
      val=entity.get('БПв')
      outStr+='+' if val>0 else ''
      outStr+=str(val)  
    else:
      outStr+='-'
    outStr+=' & '

  outStr+=entity.get('ограничение Модификатора Ловкости','-')
  outStr+=' & '

  outStr+=entity.get('требуемая Выносливость','-')
  outStr+=' & '

  outStr+=entity.get('Помеха на Скрытность','-')
  outStr+=' & '

  outStr+=entity.get('СП','-')
  outStr+=' & '

  outStr+=entity.get('вес','-')
  outStr+='\\\\ \\hline'

  return outStr

def genEntity(entityDict,idx,form):
  outStr=''
  outStr+='\\begin{center}'
  outStr+='\\begin{tabular}{|c||c|'
  outStr+='c|' if form=='Щит' else ''
  outStr+='c|c|c||c|c|c|}'
  outStr+='\\hline'
  outStr+='Название & БЗщ'
  outStr+=' & БПв' if form=='Щит' else ''
  outStr+=' & оМЛв & тВн & ПС & СП & Вес\\\\ \\hline'
  outStr+='\\hline'

  for key in entityDict:
    entity=entityDict.get(key)
    outStr+=genLine(key,entity,form)

  outStr+='\\end{tabular}'
  outStr+='\\end{center}'

  for key in entityDict:
    entity=entityDict.get(key)
    outStr+='\\paragraph{'+key+'}'
    outStr+=try_to_get('описание', entity, key)
    if 'особые свойства' in entity:
      outStr+='\\newline\\textbf{Особые свойства(*): }'+entity.get('особые свойства')

  return outStr

#название:
#  фантастическое:
#  описание:
#  особые свойства:
#  бонус Защиты:
#  ограничение Модификатора Ловкости:
#  требуемая Выносливость:
#  Помеха на Скрытность:
#  СП:
#  вес:
