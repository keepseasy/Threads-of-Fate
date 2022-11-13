#import math
from genLib import checkKey
from genLib import tryInt
from genLib import tryFloat
from genLib import getOptional
def sortKey(dict):
 if ('бонус Защиты' in dict):
  return dict.get('бонус Защиты')
 else:
  return ''

def genLine(entity,monster=False):
 outStr=''

 checkKey('название',entity)
 outStr+=entity.get('название')
 if checkKey('особые свойства',entity,keep=True):
  outStr+='*'
 if checkKey('фантастический',entity):
  outStr+='\\textsuperscript{ф}'
 outStr+=' & '

 checkKey('бонус Защиты',entity)
 outStr+=entity.get('бонус Защиты')
 outStr+=' & '

 outStr+=getOptional('Класс Защиты',entity)
 outStr+=' & '

 outStr+=getOptional('ограничение Модификатора Ловкости',entity)
 outStr+=' & '

 outStr+=getOptional('требуемая Выносливость',entity)
 outStr+=' & '

 outStr+=getOptional('Помеха на Скрытность',entity)
 outStr+=' & '

 outStr+=getOptional('СП',entity)
 outStr+=' & '

 outStr+=getOptional('вес',entity)
 outStr+='\\\\ \\hline'

 return outStr

def genEntity(entityList):
 outStr=''
 outStr+='\\begin{tabular}{|c||c|c|c|c||c|c|c|}'
 outStr+='\\hline'
 outStr+='Название & БЗщ & КЗ & оМЛв & ПС & тВн & СП & Вес\\\\ \\hline'
 outStr+='\\hline'

 for entity in entityList:
  outStr+=genLine(entity)

 outStr+='\\end{tabular}'
 outStr+='\\end{center}'

 for entity in entityList:
  outStr+='\\paragraph{'+entity.get('название')+'}'
  checkKey('описание',entity)
  outStr+=entity.get('описание')
  if checkKey('особые свойства',entity,keep=True):
   outStr+='\\newline\\textbf{Особые свойства(*): }'+entity.get('особые свойства')

 return outStr

# { "название":"",
#   "фантастический":"Да",
#   "описание":"",
#   "особые свойства":"",
#   "бонус Защиты":"",
#   "Класс Защиты":"",
#   "ограничение Модификатора Ловкости":"",
#   "требуемая Выносливость":"",
#   "Помеха на Скрытность":"1",
#   "СП":"",
#   "вес":""
# },