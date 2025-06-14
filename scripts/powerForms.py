from scripts.genLib import getName as sortKey
from scripts.genFromYaml import main
def pureGen():
 return True
class formTemplate:
 props={}
 def __init__(self, name, genInfo):
  self.props={}
  self.name=name
  self.genInfo=genInfo
  self.genInfo(self)
 def genEntity(self,entity,idx,form):
  outStr=''
  index=list(self.props)
  for item in index:
   mandatory=self.props.get(item)
   if item in entity or mandatory:
    outStr+='\\newline\\textbf{'
    outStr+=item
    outStr+=': }'
    outStr+=entity.get(item)
  return outStr

def genEntity(entity,idx,form):
 outStr=''
 for form in getForms():
  outStr+='\\section{'+form.name+'}'
  outStr+=form.genInfo(form)
  outStr+=main('powers','powers',form.name)
 return outStr

def getForms():
  forms=[]
  forms.append(formTemplate('Снаряд',genProjectileInfo))
  forms.append(formTemplate('Бомба',genBombInfo))
  forms.append(formTemplate('Метка',genMarkInfo))
  forms.append(formTemplate('Область',genRegionInfo))
  forms.append(formTemplate('Призыв',genSummonInfo))
  forms.append(formTemplate('Наговор',genHexInfo))
  # forms.append(formTemplate('Ритуал',genRitualInfo))
  return forms

def genProjectileInfo(self):
  outStr='Исказитель отправляет Снаряд в цель. Снаряд наносит Пв, как Дальнобойное оружие, а вместо МЛв в формуле Меткости используется МФх.'

  outStr+='\\begin{itemize}'

  prop='Тип Повреждений'
  self.props[prop]=True
  outStr+='\\item '+prop+' и '

  prop='Бонус к Повреждениям'
  self.props[prop]=True
  outStr+=prop+' указаны в описании.'
  outStr+='\\end{itemize}'

  outStr+='Если в описании феномена не указано обратного, то:'
  outStr+='\\begin{itemize}'

  prop='Дистанции'
  self.props[prop]=False
  outStr+='\\item '+prop+' Снаряда составляют 20/40;'

  prop='Критический Удар'
  self.props[prop]=False
  outStr+='\\item '+prop+' Снаряда равен 20;'

  prop='Скорострельность'
  self.props[prop]=False
  outStr+='\\item '+prop+' Снаряда рана 1.'

  outStr+='\\end{itemize}'
  return outStr

def genBombInfo(self):
  outStr='Исказитель метает Бомбу – сгусток своей Энергии, во врагов, и наслаждается эффектом. Чтобы поразить цель, герой проверяет Меткость по обычным правилам, но МФх и КонцентрацияЭ определяют, насколько мощной получится Бомба. Бомбу, как и гранату, можно метать в землю, или прямо существо. Эффекты Взрыва указаны в описании конкретных феноменов. Если Цель Бомбы получает КУ при ее активации, эффекты КУ распространяются на всех существ в Радиусе Взрыва.'
  outStr+='\\newline Бомба является Метательным оружием. Пока Бомба не брошена, она занимет руку, а Стоимость Поддержания Бомбы равна 0. '

  outStr+='Если в описании феномена не указано обратного, то:'
  outStr+='\\begin{itemize}'

  prop='Радиус Взрыва'
  self.props[prop]=False
  outStr+='\\item '+prop+' Бомбы равен \\textbf{|1+МФх|} (минимум 2);'

  prop='Сила Взрыва'
  self.props[prop]=False
  outStr+='\\item '+prop+' Бомбы равна \\textbf{|10+Концентрация(МФх)|};'

  prop='Тип Повреждений'
  self.props[prop]=False
  outStr+='\\item '+prop+' Бомбы является Дробящим;'

  prop='Бонус Повреждений'
  self.props[prop]=False
  outStr+='\\item '+prop+' Бомбы равен 0/-1;'

  prop='Дистанции'
  self.props[prop]=False
  outStr+='\\item '+prop+' Бомбы составляют 5/20;'

  prop='Критический Удар'
  self.props[prop]=False
  outStr+='\\item '+prop+' Бомбы равен 20;'
  outStr+='\\end{itemize}'

  return outStr

def genMarkInfo(self):
  outStr='Исказитель накладывает Метку на предмет или существо. Если цель сопротивляется, герой должен преуспеть в маневре «Касание». При провале Метка остается в руке героя. Он может по-вторить маневр позднее. Пока Метка не наложена, она занимет руку, а Стоимость Поддержания Метки равна 0.'
  return outStr

def genRegionInfo(self):
  outStr='Герой создает Область, которая налагает эффекты на попавших в нее. Активатор Области может выбрать, влияют на него эффекты, или нет.'
  outStr+='\\begin{itemize}'
  prop='Дистанция'
  self.props[prop]=True
  outStr+='\\item'+prop+' Области определяет максимальное удаление от героя, на котором накладываются эффекты области во время ее активации.'
  outStr+='\\end{itemize}'

  outStr+='Если в описании не указано иначе, Область является кругом вокруг героя и не перемещается вместе с ним.'
  #особое свойство 'Уточнение Формы'. Отображается в названии.
  outStr+='\\newline Возможные формы Области:'
  outStr+='\\begin{itemize}'
  outStr+='\\item[--] \\textbf{Круг} вокруг героя. \\textbf{Дистанция} определяет радиус круга.'
  outStr+='\\item[--] \\textbf{Периметр} очерченный героем. Это должна быть замкнутая линия без самопересечений. \\textbf{Дистанция} определяет 2 максимально удаленные друг от друга точки периметра.'
  outStr+='\\item[--] \\textbf{Конус} перед героем. При сотворении Феномена герой может определить, насколько широким будет конус, но он не может быть больше, чем полукруг. Размах конуса не влияет на силу эффектов и затраты Энергии на сотворение Феномена. \\textbf{Дистанция} определяет радиус конуса.'
  outStr+='\\end{itemize}'

  return outStr

def genSummonInfo(self):
  outStr='Герой перемещает или призывает откуда-то существа, предметы и субстанции. Никто, даже сам исказаитель не скажет, откуда именно они прибывают.'
  outStr+='\\newline Призванные существа исполняют все приказы призывателя. По истечении времени Призыва они обычно возвращаются восвояси, но порой могут и задержаться. В этом случае контроль исказителя над их действиями прекращается, а существа редко бывают довольны фактом призыва.'

  prop='Дистанция'
  self.props[prop]=False
  outStr+='\\newline Если не указана \\textbf{'+prop+'}, то призванный предмет оказывается в руке призывателя, а призванное существо на свободном пятачке не дальше метра от исказителя. Призванное существо не может по своей воле отойти от призывателя дальше, чем указано в Дистанции. Если призванное существо или предмет случайно или намеренно удаляются дальше, чем указано в Дистанции, Призыв немедленно Прерывается.'

  return outStr

def genHexInfo(self):
  outStr='Герой воздействует Наговором на выбранную цель. Если герой не видит цель, но она находится в пределах Дистанции, он проверяет Наведение. В случае провала активация считается Прерванной.'
  outStr+='\\newline Если цель покидает пределы Дистанции или находится за пределами Дистанции на момент активации Наговора, активация автоматически Прерывается.'
  outStr+='\\begin{itemize}'

  prop='Дистанция'
  self.props[prop]=True
  outStr+='\\item[--] \\textbf{'+prop+'} Наговора указана в описании.'

  outStr+='\\end{itemize}'
  return outStr
 