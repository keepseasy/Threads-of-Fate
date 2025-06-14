from scripts.genLib import pureGen
from scripts.genLib import getName as sortKey
from scripts.powerForms import getForms

#from scripts.genLib import bookmark

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
  #  outStr+='\\newline'
  outStr+='\\paragraph{} \\textit{'+entity.get('описание','\\err нет описания')+'}'
  outStr+='\\paragraph{Стоимость'
  if 'поддержание' in entity:
   outStr+='/Поддержание'
  if 'риз' in entity:
   outStr+='[РИЗ]'
  outStr+=': }'+entity.get('стоимость','\\err нет стоимости')+' Эн'
  if 'поддержание' in entity:
   outStr+='/'+entity.get('поддержание')+' Эн'
  if 'поддержание' in entity and not 'Длительность' in entity:
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
  if 'сопротивление Наведению' in entity:
   outStr+='\\newline \\textbf{Сопротивление Наведению: }'+entity.get('сопротивление Наведению')
#------------------------------------------------------------------
  if 'Длительность' in entity:
   outStr+='\\newline \\textbf{Длительность: }'+entity.get('Длительность')
  if 'Время активации' in entity:
   outStr+='\\newline \\textbf{Время активации: }'+entity.get('Время активации')
  if 'Сопротивление' in entity:
   outStr+='\\newline \\textbf{Сопротивление: }'+entity.get('Сопротивление')
   
#------------------------------------------------------------------
  outStr+='\\paragraph{Эффект: }'+entity.get('эффект','\\err нет описания эффекта')
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
  if 'заметки' in entity:
   outStr+='\\paragraph{}'+entity.get('заметки')
 return outStr

# [название]:
#   описание:

#   стоимость:
#   поддержание:
#   РИЗ:
#   Время активации:
#   Длительность:
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
