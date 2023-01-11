import re
def getName(dict):
 return list(dict)[0]
def pureGen():
 return False
def sortDict(entityDict,curSortKey=getName):
 return dict(sorted(entityDict.items(),key=curSortKey))

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

def genProps(props,eType=None):
 props.sort(key=getName)
 strList=[]
 joiner=', '
 for prop in props:
  cost=prop.get('стоимость',None)
  name=getName(prop)
  descr=prop.get(name,None)
  
  if eType is not None:
   name=makelink(prop,eType)
  if cost is not None:
   name+='('+prop.get('стоимость')+')'
  if descr is not None:
   joiner=''
   name='\\item\\textbf{'+name+': }'+descr
  strList.append(name)
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

def clear(entityDict,curSortKey):
 entityDict=sortDict(entityDict,curSortKey)
 for feature in entityDict:
  name=getName(feature)
  if name[0]=='-':
   my_dict.pop(name[1:], None)
   del my_dict[name]
 return entityDict

def bookmark(name,eType):
 return '\\hypertarget{'+eType+str(hash(name))+'}{}'

def makelink(name,eType,displayName=None):
 if displayName is None:
  displayName=name
 return '\\hyperlink{'+eType+str(hash(name))+'}{'+displayName+'}'