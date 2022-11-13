import sys
import json

#get all names
baseName=sys.argv[1]
jsonName='content/'+baseName+'.json'
texName='scripts/output/'+baseName+'.tex'

#import generation algorythm
_temp = __import__(baseName, globals(), locals(), ['genEntity'], 0)
genEntity = _temp.genEntity

#import sorting key
_temp = __import__(baseName, globals(), locals(), ['sortKey'], 0)
sortKey = _temp.sortKey

#extract and sort data
def getDict(jsonName):
 with open(jsonName, 'r', encoding="utf-8") as jf:
  entityList = json.load(jf)
  entityList.sort(key=sortKey)
  return entityList

#main: read data and write generated string to .tex file
f=open(texName, "w", encoding="utf-8")
f.write(genEntity(getDict(jsonName)))
f.close()