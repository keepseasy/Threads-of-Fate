import os.path
import re
import yaml
from yaml.loader import SafeLoader


def getName(dict):
 return list(dict)[0]
def pureGen():
 return False
def sortDict(entityDict,curSortKey=getName):
 return dict(sorted(entityDict.items(),key=curSortKey))

def tryInt(val):
 if val=='\\tbd': return val
 if val.startswith('-') and val[1:].isdigit(): return val
 if val.isdigit(): return val
 return '\\err'

def genProps(props,eType=None):
 props.sort(key=getName)
 strList=[]
 joiner=', '
 for prop in props:
#  print(prop)
  cost=prop.get('стоимость',False)
  name=getName(prop)
  descr=prop.get(name,False)
  
  if eType is not None: name=makelink(prop,eType)
  if cost: name+='('+str(prop.get('стоимость'))+')'
  if descr:
   joiner=''
   name='\\newline\\textbullet\\ \\textbf{'+name+': }'+descr
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

def clear(entityDict,curSortKey=getName):
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
 if displayName is None: displayName=name
 return '\\hyperlink{'+eType+str(hash(name))+'}{'+displayName+'}'

def getDict(yamlName):
 if not os.path.isfile(yamlName): return {}
 with open(yamlName, 'r', encoding="utf-8") as jf:
  return yaml.load(jf, Loader=SafeLoader)
