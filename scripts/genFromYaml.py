import sys
import yaml
from yaml.loader import SafeLoader
from genLib import checkKey
from genLib import clear

#get all names
baseName=''
if len(sys.argv) > 1:
 baseName=sys.argv[1]
dataName=baseName

if len(sys.argv) > 2:
 dataName=sys.argv[2]
texName='scripts/output/'+dataName+'.tex'
yamlName1='content/'+dataName+'.yaml'
yamlName2='localContent/'+dataName+'.yaml'

#import generation algorythm
_temp = __import__(baseName, globals(), locals(), ['genEntity'], 0)
genEntity = _temp.genEntity

#import pure generation check
_temp = __import__(baseName, globals(), locals(), ['genEntity'], 0)
pureGen = _temp.pureGen

#import sorting key
_temp = __import__(baseName, globals(), locals(), ['sortKey'], 0)
sortKey = _temp.sortKey

#extract and sort data
def getList(yamlName):
 with open(yamlName, 'r', encoding="utf-8") as jf:
  return yaml.load(jf, Loader=SafeLoader)

#main: read data and write generated string to .tex file
import os
if not os.path.exists('scripts/output/'):
 os.makedirs('scripts/output/')
f=open(texName, "w", encoding="utf-8")
finalList=None
if not pureGen():
 finalList=getList(yamlName2)
 finalList+=getList(yamlName1)
 finalList=clear(finalList,sortKey)
f.write(genEntity(finalList))
f.close()