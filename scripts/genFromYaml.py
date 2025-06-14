import os.path
from scripts.genLib import clear
from scripts.genLib import getDict
from scripts.genLib import try_to_get

def pickForm(myDict,myForm):
 if myForm=='':
  return myDict
 newDict={}
 for key in myDict:
  entity=myDict.get(key)
  curForm=try_to_get('Форма', entity, key)
  if curForm==myForm:
   newDict[key]=entity
 return newDict

def main(baseName,dataName,form=None):
  texName='scripts/output/'+dataName+'.tex'
  yamlName1='base_content/'+dataName+'.yaml'
  yamlName2='dlc/'+dataName+'.yaml'

#import generation algorythm
  _temp = __import__('scripts.'+baseName, globals(), locals(), ['genEntity'], 0)
  genEntity = _temp.genEntity

#import pure generation check
  _temp = __import__('scripts.'+baseName, globals(), locals(), ['pureGen'], 0)
  pureGen = _temp.pureGen

#import sorting key
  _temp = __import__('scripts.'+baseName, globals(), locals(), ['sortKey'], 0)
  sortKey = _temp.sortKey

#extract and sort data
#main: read data and write generated string to .tex file
  if not os.path.exists('scripts/output/'): os.makedirs('scripts/output/')
#  f=open(texName, "w", encoding="utf-8")
  finalDict=None
  if not pureGen():
    basicDict=getDict(yamlName1)
# print(basicDict)
    if not basicDict:
      print('missing generic Content file')
      exit()
    customDict=getDict(yamlName2)
# print(customDict)
    finalDict=clear(basicDict|customDict,sortKey)
    if not form is None:
      finalDict=pickForm(finalDict,form)
  return genEntity(finalDict,baseName,form)
#  f.write(genEntity(finalDict,baseName,form))
#  f.close()