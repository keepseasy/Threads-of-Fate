from scripts.genLib import pureGen
from scripts.genLib import getName as sortKey
from scripts.powerForms import getForms

#from scripts.genLib import bookmark

def genEntity(entityDict,idx,form):
  outStr=''
  # allForms=True if form=='' else False

  for key in entityDict:
    entity=entityDict.get(key)
    outStr+='\\subsection{'+key
    outStr+='}'
    outStr+='\\index['+idx+']{'+key+'}'
    
    if 'Форма' in entity:
      outStr+='\\textbf{Форма: }'+entity.get('Форма')
      if 'Уточнение Формы' in entity:
        outStr+='('+entity.get('Уточнение Формы')+')'

    outStr+='\\paragraph{} \\textit{'+entity.get('Описание','\\err нет описания')+'}'

#------------------------------------------------------------------
    outStr+='\\paragraph{Стоимость'
    if 'Поддержание' in entity:
      outStr+='/Поддержание'
    if 'риз' in entity:
      outStr+='[РИЗ]'
    outStr+=': }'+entity.get('Стоимость','\\err нет стоимости')+' Эн'
    if 'Поддержание' in entity:
      outStr+='/'+entity.get('Поддержание')+' Эн'
    if 'Поддержание' in entity and not 'Длительность' in entity:
      outStr+='\\err есть Поддержание но нет продолжительности'
    if 'Заметка к стоимости' in entity:
      outStr+=' '+entity.get('Заметка к стоимости')

#------------------------------------------------------------------
    outStr+='\\leavevmode\\newline \\textbf{СП: }'+entity.get('СП','\\err СП')
    if 'Особые ингридиенты' in entity:
      outStr+=entity.get('Особые ингридиенты')

#------------------------------------------------------------------
    if 'Сложность Подготовки' in entity:
      outStr+='\\leavevmode\\newline \\textbf{Сложность Подготовки: }'+entity.get('Сложность Подготовки')
    if 'Сопротивление' in entity:
      outStr+='\\leavevmode\\newline \\textbf{Сопротивление: }'+entity.get('Сопротивление')
    if 'Сопротивление Наведению' in entity:
      outStr+='\\leavevmode\\newline \\textbf{Сопротивление Наведению: }'+entity.get('Сопротивление Наведению')

#------------------------------------------------------------------
    if 'Время подготовки' in entity:
      outStr+='\\leavevmode\\newline \\textbf{Время подготовки: }'+entity.get('Время подготовки')
    if 'Время активации' in entity:
      outStr+='\\leavevmode\\newline \\textbf{Время активации: }'+entity.get('Время активации')
    if 'Длительность' in entity:
      outStr+='\\leavevmode\\newline \\textbf{Длительность: }'+entity.get('Длительность')
    if 'Дистанция' in entity:
      outStr+='\\leavevmode\\newline \\textbf{Дистанция: }'+entity.get('Дистанция')
      
#------------------------------------------------------------------
    outStr+='\\paragraph{Эффект: }'+entity.get('Эффект','\\err нет описания эффекта')
    if 'Цена ошибки' in entity:
      outStr+='\\paragraph{Цена ошибки: }'+entity.get('Цена ошибки')
    if 'Усиление' in entity:
      enhList=entity.get('Усиление')
      outStr+='\\paragraph{Усиление:}\\begin{itemize}'
      if type(enhList) is not list:
        outStr+='\\item \\err не удалось извлечь список усилений'
      for enh in enhList:
        outStr+='\\item'
        if type(enh) is not dict:
          outStr+='\\err неправильный формат записи усилений'
        outStr+='+'+enh.get('Стоимость','\\err нет стоимости')
        outStr+=' СП -> '
        outStr+=enh.get('Описание','\\err нет описания')
      outStr+='\\end{itemize}'
    if 'заметки' in entity:
      outStr+='\\paragraph{}'+entity.get('заметки')
  return outStr
