  noSkipRef=checkKey('название',entity)
  entityName=entity.get('название')
  outStr+='\\subsection{'+entityName
  outStr+='}'
#  if noSkipRef:
#   outStr+='\\hypertarget{monster'+str(hash(entityName))+'}{}'
#  else:
#   outStr+='\\err не задано название Существа, ссылка не создана!'
