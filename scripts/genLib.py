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
 if ('название' in dict):
  return dict.get('название')
 else:
  return ''

def genShort(prop):
 name=list(prop)[0]
 val=tryInt(prop.get(name))
 return name+'('+val+')'

def genLong(prop,costly):
 name=list(prop)[0]
 descr=prop.get(name)
 outStr='\\item\\textbf{'+name
 if costly:
  checkKey('cost',prop)
  outStr+='('+tryInt(prop.get('cost'))
  outStr+=')'
 outStr+=': }'+descr
 return outStr

def localSortKey(dict):
 return list(dict)[0]
def genProps(name,entity,costly=False,short=False):
  outStr=''
  if name in entity:
   props=entity.get(name)
   props.sort(key=localSortKey)
   strList=[]
   joiner=', ' if short else ''
   for prop in props:
    propStr=genShort(prop) if short else genLong(prop,costly)
    strList.append(propStr)
  return joiner.join(strList)