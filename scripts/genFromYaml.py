import sys
import os.path
from genLib import clear
from genLib import getDict


#get all names
baseName=''
if len(sys.argv) > 1: baseName=sys.argv[1]
dataName=baseName

if len(sys.argv) > 2: dataName=sys.argv[2]
texName='scripts/output/'+dataName+'.tex'
yamlName1='content/'+dataName+'.yaml'
yamlName2='localContent/'+dataName+'.yaml'

form=''
if len(sys.argv) > 3: form=sys.argv[3]

#import generation algorythm
_temp = __import__(baseName, globals(), locals(), ['genEntity'], 0)
genEntity = _temp.genEntity

#import pure generation check
_temp = __import__(baseName, globals(), locals(), ['pureGen'], 0)
pureGen = _temp.pureGen

#import sorting key
_temp = __import__(baseName, globals(), locals(), ['sortKey'], 0)
sortKey = _temp.sortKey

#extract and sort data

def pickForm(myDict,myForm):
 if myForm=='':
  return myDict
 newDict={}
 for name in myDict:
  entity=myDict.get(name)
  curForm=entity.get('Форма','')
  if curForm=='':
   print(name,': err no form')
  if curForm==myForm:
   newDict[name]=entity
 return newDict

#main: read data and write generated string to .tex file
if not os.path.exists('scripts/output/'): os.makedirs('scripts/output/')
f=open(texName, "w", encoding="utf-8")
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
 finalDict=pickForm(finalDict,form)
f.write(genEntity(finalDict))
f.close()