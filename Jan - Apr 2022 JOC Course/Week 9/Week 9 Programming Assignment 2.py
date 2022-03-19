def mergeDic(d1,d2):
  for k in d2:
    if k not in d1:
      d1[k]=d2[k]
  return(d1)
  