from genLib import pureGen
from genLib import getName as sortKey
from powerForms import getForms

#from genLib import bookmark

def genEntity(entityDict,idx,form):
 outStr=''
 allForms=True if form=='' else False

 for key in entityDict:
  entity=entityDict.get(key)
  outStr+='\\subsection{'+key
  if 'Уточнение Формы' in entity and not allForms:
   outStr+='['+entity.get('Уточнение Формы')+']'
  outStr+='}'
  outStr+='\\index['+idx+']{'+key+'}'
#  outStr+=bookmark(key,'power')
  if allForms:
   outStr+='\\textbf{Форма: }'+entity.get('Форма','\\err')
   if 'Уточнение Формы' in entity:
    outStr+='['+entity.get('Уточнение Формы')+']'
   outStr+='\\newline'

  outStr+='\\textbf{Стоимость'
  if 'поддержание' in entity:
   outStr+='/Поддержание'
  outStr+=': }'+entity.get('стоимость','\\err нет стоимости')+' Эн'
  if 'поддержание' in entity:
   outStr+='/'+entity.get('поддержание')+' Эн'
  if 'поддержание' in entity and not 'продолжительность' in entity:
   outStr+='\\err есть поддержание но нет продолжительности'

#------------------------------------------------------------------
#form
  entityForm=entity.get('Форма')
  forms=getForms()
  for curForm in forms:
   if curForm.name==entityForm:
    if curForm.name=='Область' and 'Уточнение' in entity:
     outStr+='['+entity.get('Форма')+']'
    outStr+=curForm.genEntity(entity,idx,form)
    break
  else:
   outStr+='\\err у Феномена неправильная Форма'
#------------------------------------------------------------------
# aiming resist
  if 'сопротивление Наведению' in entity:
   outStr+='\\newline \\textbf{Сопротивление Наведению: }'+entity.get('сопротивление Наведению')
#------------------------------------------------------------------
  if 'продолжительность' in entity:
   outStr+='\\newline \\textbf{Длительность: }'+entity.get('продолжительность')
  if 'время сотворения' in entity:
   outStr+='\\newline \\textbf{Время сотворения: }'+entity.get('время сотворения')
#------------------------------------------------------------------
  outStr+='\\paragraph{Описание: }'+entity.get('описание','\\err нет описания')
  if 'Усиление' in entity:
   enhList=entity.get('Усиление')
   outStr+='\\paragraph{Усиление:}\\begin{itemize}'
   if type(enhList) is not list:
    outStr+='\\item \\err не удалось извлечь список усилений'
   for enh in enhList:
    outStr+='\\item'
    if type(enh) is not dict:
     outStr+='\\err неправильный формат записи усилений'
    outStr+='+'+enh.get('стоимость','\\err нет стоимости')
    outStr+=' Эн -> '
    outStr+=enh.get('описание','\\err нет описания')
   outStr+='\\end{itemize}'
 return outStr

# [название]:
#   описание:

#   стоимость:
#   поддержание:
#   РИЗ:
#   время сотворения:
#   продолжительность:
#   сопротивление Наведению:

#   Форма:
#   Уточнение:

#   Тип Повреждений:
#   Бонус Повреждений:
#   КУ:
#   Скорострельность:
#   Радиус Взрыва:
#   Сила Взрыва:
#   Дистанция:
#   Сопротивление:

#   Усиление:
#   - [стоимость]:
#     описание:
