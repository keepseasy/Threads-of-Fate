import sys
import yaml
from yaml.loader import SafeLoader
from genLib import checkKey

#get all names
baseName=''
if len(sys.argv) > 1:
 baseName=sys.argv[1]
dataName=baseName

if len(sys.argv) > 2:
 dataName=sys.argv[2]
texName='scripts/output/'+dataName+'.tex'
yamlName='content/'+dataName+'.yaml'

#import generation algorythm
_temp = __import__(baseName, globals(), locals(), ['genEntity'], 0)
genEntity = _temp.genEntity

#import pure generation check
_temp = __import__(baseName, globals(), locals(), ['genEntity'], 0)
pureGen = _temp.pureGen

#import sorting key
_temp = __import__(baseName, globals(), locals(), ['sortKey'], 0)
sortKey = _temp.sortKey

def removeInactive(entityList):
 for entity in entityList:
  if checkKey('Не используется',entity,keep=True):
   entityList.remove(entity)
 return entityList

#extract and sort data
def getList(yamlName):
 with open(yamlName, 'r', encoding="utf-8") as jf:
  entityList = yaml.load(jf, Loader=SafeLoader)
  entityList.sort(key=sortKey)
  return removeInactive(entityList)

#main: read data and write generated string to .tex file
import os
if not os.path.exists('scripts/output/'):
    os.makedirs('scripts/output/')
f=open(texName, "w", encoding="utf-8")
if pureGen():
 f.write(genEntity(None))
else:
 f.write(genEntity(getList(yamlName)))
f.close()