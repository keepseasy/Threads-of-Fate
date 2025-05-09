from scripts.genLib import getName as sortKey
from scripts.genLib import pureGen
from scripts.genLib import genProps
from scripts.genLib import try_to_get

def genEntity(entityDict,idx,form):
 outStr=''
 for key in entityDict:
  entity=entityDict.get(key)

  outStr+='\\subsubsection{'+key
  if 'Наследие' in entity: outStr+='[Наследие]'
  outStr+='}'
  outStr+='\\index['+idx+']{'+key+'}'
  if 'Экспертные навыки' in entity:
    outStr+='\\paragraph{Экспертные навыки: } '+entity.get('Экспертные Навыки')
  else:
    outStr+='\\paragraph{Экспертные навыки:} нет.'


  #outStr+='\\newline ' + try_to_get('описание', entity, key)

  if 'Свойства' in entity:
   #outStr+='\\newline'
   outStr+='\\paragraph{Свойства}'
   outStr+=genProps(entity.get('Свойства'))

  if 'Функции' in entity:
   #outStr+='\\newline'
   outStr+='\\paragraph{Функции}'
   outStr+=genProps(entity.get('Функции'))

  if 'Снаряжение' in entity:
    #outStr+='\\newline'
    outStr+='\\paragraph{Снаряжение}'
    outStr+=genProps(entity.get('Снаряжение'))

  outStr+='\\paragraph{Темная Сторона. }' + try_to_get('Темная Сторона', entity, key)

  outStr+='\\paragraph{Ход - ' + try_to_get('название Хода', entity, key)
  outStr+=' (' + try_to_get('стоимость Хода', entity, key)
  outStr+='):} ' + try_to_get('описание Хода', entity, key)

  outStr+='\\paragraph{Если Ход совершается без обрыва Нитей,} ' + try_to_get('штраф Хода без Нитей', entity, key)
  outStr+='\\trouble{' + try_to_get('название результата неприятности Успех', entity, key)
  outStr+='}{' + try_to_get('описание Успеха', entity, key)
  outStr+='}{' + try_to_get('название результата неприятности Затруднения', entity, key)
  outStr+='}{' + try_to_get('описание Затруднений', entity, key)
  outStr+='}{' + try_to_get('название результата неприятности Проблемы', entity, key)
  outStr+='}{' + try_to_get('описание Проблемы', entity, key)
  outStr+='}{' + try_to_get('название результата неприятности Катастрофа', entity, key)
  outStr+='}{' + try_to_get('описание Катастрофы', entity, key)
  outStr+='}'
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
