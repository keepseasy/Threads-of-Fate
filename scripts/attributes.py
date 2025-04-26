from scripts.genLib import getName as sortKey
from scripts.genLib import pureGen
from scripts.genLib import genProps

def genEntity(entityDict,idx,form):
 outStr=''
 for key in entityDict:
  entity=entityDict.get(key)

  if 'расширенная версия' in entity:
   outStr+='\\ifx\\islight\\undefined '
  outStr+='\\subsubsection{'+key
  if 'Наследие' in entity: outStr+='[Наследие]'
  outStr+='}'
  outStr+='\\index['+idx+']{'+key+'}'
  outStr+='\\paragraph{Экспертные навыки: } '+entity.get('Экспертные Навыки','\\err не заданы Экспертные Навыки')
  outStr+='\\newline '+entity.get('описание','\\err не задано описание Атрибута')

  if 'Трюки' in entity:
   # outStr+='\\newline'
   # outStr+='\\textbf{Трюки}'
   outStr+=genProps(entity.get('Трюки'))
   # outStr+='\\paragraph{'+entity.get('название Трюка','\\err не задано название трюка')
   # outStr+=':} '+entity.get('описание Трюка','\\err не задано описание трюка')

  if 'Функции' in entity:
   outStr+='\\newline'
   outStr+='\\textbf{Функции}'
   outStr+=genProps(entity.get('Функции'))

  # if 'название Функции' in entity:
   # outStr+='\\paragraph{Функция — '+entity.get('название Функции','\\err не задано название Функции')
   # outStr+=':} '+entity.get('описание Функции','\\err не задано описание Функции')

  outStr+='\\paragraph{Ход — '+entity.get('название Хода','\\err не задано название Хода')
  outStr+=' ('+entity.get('стоимость Хода','\\err не задана стоимость Хода')
  outStr+='):} '+entity.get('описание Хода','\\err не задано описание Хода')

  outStr+='\\paragraph{Если Ход совершается без обрыва Нитей,} '+entity.get('штраф Хода без Нитей','\\err не задан штраф')
  if 'название результата неприятности Успех' in entity:
   outStr+='\\trouble{'+entity.get('название результата неприятности Успех')
   outStr+='}{'+entity.get('описание Успеха','\\err не задано описание Успеха')
   outStr+='}{'+entity.get('название результата неприятности Затруднения','\\err не задано название Затруднения')
   outStr+='}{'+entity.get('описание Затруднений','\\err не задано описание Затруднения')
   outStr+='}{'+entity.get('название результата неприятности Проблемы','\\err не задано название Проблем')
   outStr+='}{'+entity.get('описание Проблемы','\\err не задано описание Проблем')
   outStr+='}{'+entity.get('название результата неприятности Катастрофа','\\err не задано название Катастрофы')
   outStr+='}{'+entity.get('описание Катастрофы','\\err не задано описание Катастрофы')
   outStr+='}'
  if 'расширенная версия' in entity:
   outStr+='\\fi '
 return outStr

# [название]:
#   Экспертные Навыки: ...
#   описание: ...
#   название Трюка: ...
#   описание Трюка: ...
#   название Функции: ...
#   описание Функции: ...
#   название Хода: ...
#   стоимость Хода: ...
#   описание Хода: ...
#   штраф Хода без Нитей: ...
#   название результата неприятности Успех: ...
#   описание Успеха: ...
#   название результата неприятности Затруднения: ...
#   описание Затруднений: ...
#   название результата неприятности Проблемы: ...
#   описание Проблемы: ...
#   название результата неприятности Катастрофа: ...
#   описание Катастроф: ...
