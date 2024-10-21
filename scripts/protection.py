from genLib import pureGen
def sortKey(dict1):
 entity=list(dict1)[1]
 return int(entity.get('бонус Защиты','-1'))

def genLine(key,entity):
 outStr=''
 if 'расширенная версия' in entity:
  outStr+='\\ifx\\islight\\undefined '
 outStr+=key
 if 'особые свойства' in entity:
  outStr+='*'
 if 'фантастическое' in entity:
  outStr+='\\textsuperscript{ф}'
 outStr+=' & '

 outStr+='+'+entity.get('бонус Защиты','\\err')
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
 if 'расширенная версия' in entity:
  outStr+='\\fi '

 return outStr

def genEntity(entityDict,idx,form):
 outStr=''
 outStr+='\\begin{center}'
 outStr+='\\begin{tabular}{|c||c|c|c||c|c|c|}'
 outStr+='\\hline'
 outStr+='Название & БЗщ & оМЛв & тВн & ПС & СП & Вес\\\\ \\hline'
 outStr+='\\hline'

 for key in entityDict:
  entity=entityDict.get(key)
  outStr+=genLine(key,entity)

 outStr+='\\end{tabular}'
 outStr+='\\end{center}'

 for key in entityDict:
  entity=entityDict.get(key)
  outStr+='\\paragraph{'+key+'}'
  outStr+=entity.get('описание','\\err нет описания')
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
