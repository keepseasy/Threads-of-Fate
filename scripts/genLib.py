import re
def checkKey(keystr,entity,keep=False):
 if keystr not in entity:
  if not keep:
   entity[keystr]='\\tbd'
  return False
 val=entity.get(keystr)
 vType=type(val)
 if not vType==str and not vType==list or not val:
  if not keep:
   entity[keystr]='\\tbd'
  return False
 return True

def getOptional(keystr,entity):
  if checkKey(keystr,entity,keep=True):
   return entity.get(keystr)
  else:
   return '-'
def tryFloat(val):
 if val=='\\tbd':
  return val
 if re.match(r'^-?\d+(?:\.\d+)$', val) is None:
  return '\\err'
 return val

def tryInt(val):
 if val=='\\tbd':
  return val
 if val.startswith('-') and val[1:].isdigit():
  return val
 if val.isdigit():
  return val
 return '\\err'

def sortKey(dict):
 return dict.get('название','')

def genShort(prop):
 name=list(prop)[0]
 val=tryInt(prop.get(name))
 return name+'('+val+')'

def genLong(prop,costly):
 name=list(prop)[0]
 descr=prop.get(name)
 outStr='\\item\\textbf{'+name
 if costly:
  checkKey('Цена',prop)
  outStr+='('+prop.get('Цена')
  outStr+=')'
 outStr+=': }'+descr
 return outStr

def localSortKey(dict):
 return list(dict)[0]
def genProps(props,costly=False,short=False):
 outStr=''
 props.sort(key=localSortKey)
 strList=[]
 joiner=', ' if short else ''
 for prop in props:
  propStr=genShort(prop) if short else genLong(prop,costly)
  strList.append(propStr)
 return joiner.join(strList)

def genSize(val):
 match val:
  case -2: return 'Крошечный'
  case -1: return 'Маленький'
  case 0: return 'Средний'
  case 1: return 'Большой'
  case 2: return 'Огромный'
  case 3: return 'Громадный'
  case 4: return 'Исполинский'
  case _: return '\\tbd'

def clear(entityList,curSortKey):
 if entityList[0] is not str:
  newList=[]
  for feature in entityList:
   if feature is not str:
    skip=False
    for newFeature in newList:
     if newFeature['название']==feature['название']:
      skip=True
    if not skip:
     newList.append(feature)
  entityList=newList
  for feature in entityList:
   if feature is not str:
    value=feature.get('название')
    if value[0]=='-':
     entityList = [d for d in entityList if d['название'] != value and d['название'] != value[1:]]
  entityList.sort(key=curSortKey)
  return entityList

 newList=[]
 for feature in entityList:
  if feature not in newList:
   newList+=feature
 entityList=newList
 for feature in entityList:
  if feature[0]=='-':
   entityList.remove(feature)
   entityList.remove(feature[1:])
 entityList.sort()
 return entityList

def bookmark(name,eType):
 return '\\hypertarget{'+eType+str(hash(name))+'}{'+name+'}'

def makelink(name,eType,displayName=None):
 if displayName is None:
  displayName=name
 return '\\hyperlink{'+eType+str(hash(name))+'}{'+displayName+'}'