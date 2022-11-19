from genLib import checkKey
from genLib import sortKey

def genEntity(entityList):
 outStr=''
 for entity in entityList:
  checkKey('название',entity)
  checkKey('описание',entity)
  checkKey('Экспертные Навыки',entity)
  checkKey('название Трюка Атрибута',entity)
  checkKey('описание Трюка',entity)
  checkKey('название Хода Атрибута',entity)
  checkKey('стоимость Хода',entity)
  checkKey('описание Хода',entity)
  checkKey('штраф Хода без Нитей',entity)

  outStr+='\\subsection{'+entity.get('название')
  if 'Наследие' in entity:
   outStr+='[Наследие]'
  if 'innatePower' in entity:
   outStr+='[Могущество]'
 
  outStr+='}'
  outStr+='\\paragraph{Экспертные навыки: } '+entity.get('Экспертные Навыки')
  outStr+='\\newline '+entity.get('описание')
  outStr+='\\paragraph{'+entity.get('название Трюка Атрибута')
  outStr+=':} '+entity.get('описание Трюка')
  outStr+='\\paragraph{Ход — '+entity.get('название Хода Атрибута')
  outStr+=' ('+entity.get('стоимость Хода')
  outStr+='):} '+entity.get('описание Хода')

  if 'название результата неприятности Успех' in entity:
   checkKey('описание Успеха',entity)
   checkKey('название результата неприятности Затруднения',entity)
   checkKey('описание Затруднений',entity)
   checkKey('название результата неприятности Проблемы',entity)
   checkKey('описание Проблемы',entity)
   checkKey('название результата неприятности Катастрофа',entity)
   checkKey('описание Катастрофы',entity)

   outStr+='\\paragraph{Если Ход совершается без обрыва Нитей,} '+entity.get('штраф Хода без Нитей')
   outStr+='\\trouble{'+entity.get('название результата неприятности Успех')
   outStr+='}{'+entity.get('описание Успеха')
   outStr+='}{'+entity.get('название результата неприятности Затруднения')
   outStr+='}{'+entity.get('описание Затруднений')
   outStr+='}{'+entity.get('название результата неприятности Проблемы')
   outStr+='}{'+entity.get('описание Проблемы')
   outStr+='}{'+entity.get('название результата неприятности Катастрофа')
   outStr+='}{'+entity.get('описание Катастрофы')
   outStr+='}'

 return outStr

# {"название":"",
#  "Экспертные Навыки":"",
#  "описание":"",
#  "название Трюка Атрибута":"",
#  "описание Трюка":"",
#  "название Хода Атрибута":"",
#  "стоимость Хода":"",
#  "описание Хода":"",
#  "штраф Хода без Нитей":"",
#  "название результата неприятности Успех":"",
#  "описание Успеха":"",
#  "название результата неприятности Затруднения":"",
#  "описание Затруднений":"",
#  "название результата неприятности Проблемы":"",
#  "описание Проблемы":"",
#  "название результата неприятности Катастрофа":"",
#  "описание Катастрофы":""
# },