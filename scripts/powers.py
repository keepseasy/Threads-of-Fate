from genLib import checkKey
from genLib import sortKey
from powerForms import getForms
def pureGen():
 return False

def genEntity(entityList):
 outStr=''
 for entity in entityList:
  checkKey('название',entity)
  outStr+='\\subsection{'+entity.get('название')+'}'

  outStr+='\\textbf{Стоимость'
  sus=checkKey('поддержание',entity)
  if checkKey('продолжительность',entity,keep=True):
#   duration=entity.get('продолжительность')
   if sus:
    outStr+='/Поддержание'

  checkKey('стоимость',entity)
  outStr+=': }'+entity.get('стоимость')+' Эн'
  tmp=entity.get('поддержание')
  if not tmp=='\\tbd':
   outStr+='/'+tmp+' Эн'
  if checkKey('РИЗ',entity,keep=True):
   outStr+=', РИЗ'


#------------------------------------------------------------------
#form
  outStr+='\\newline \\textbf{Форма: }'
  if checkKey('Форма',entity,keep=True):
   entityForm=entity.get('Форма')
   outStr+=entityForm
   forms=getForms()
   for form in forms:
    if form.name==entityForm:
     if form.name=='Область' and checkKey('Уточнение',entity,keep=True):
      outStr+='['+entity.get('Форма')+']'
     outStr+=form.genEntity(entity)
     break
   else:
    outStr+='\\err у Могущества неправильная Форма'
  else:
   outStr+='\\err у Могущества не назначена Форма'
#------------------------------------------------------------------
# aiming resist
  if checkKey('сопротивление Наведению',entity,keep=True):
   outStr+='\\newline \\textbf{Сопротивление Наведению: }'+entity.get('сопротивление Наведению')
#------------------------------------------------------------------
  if checkKey('продолжительность',entity,keep=True):
   outStr+='\\newline \\textbf{Длительность: }'+entity.get('продолжительность')
  if checkKey('время сотворения',entity,keep=True):
   outStr+='\\newline \\textbf{Время сотворения: }'+entity.get('время сотворения')
#------------------------------------------------------------------
  checkKey('описание',entity)
  outStr+='\\paragraph{Описание: }'+entity.get('описание')
  if checkKey('Усиление',entity):
   enhList=entity.get('Усиление')
   outStr+='\\paragraph{Усиление:}\\begin{itemize}'
   if type(enhList) is not list:
    outStr+='\\item \\err не удалось извлечь список усилений'
   else:
    for enh in enhList:
     outStr+='\\item'
     if type(enh) is not dict:
      outStr+='\\err неправильный формат записи усилений'
     else:
      checkKey('стоимость',enh)
      checkKey('описание',enh)
      outStr+='+'+enh.get('стоимость')
      outStr+=' Эн -> '
      outStr+=enh.get('описание')
   outStr+='\\end{itemize}'
 return outStr

# { "название":"",
#   "описание":"",

#   "стоимость":"",
#   "поддержание":"",
#   "РИЗ":"Да",
#   "время сотворения":"",
#   "продолжительность":"",
#   "сопротивление Наведению":"",

#   "Форма":"",
#   "exactForm":"",

#   "Тип Повреждений":"",
#   "Бонус Повреждений":"",
#   "КУ":"",
#   "Скорострельность":"",
#   "Радиус Взрыва":"",
#   "Сила Взрыва":"",
#   "Дистанция":"",
#   "Сопротивление":"",

#   "Усиление":[
#      {"стоимость":"","описание":""},
#      {"стоимость":"","описание":""}
#    ]
# },