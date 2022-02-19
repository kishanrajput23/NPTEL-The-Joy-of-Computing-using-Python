def uniqueE(L):
  ans=[]
  for a in L:
    if L.count(a)==1:
      ans.append(a)
  return(sorted(ans))
    