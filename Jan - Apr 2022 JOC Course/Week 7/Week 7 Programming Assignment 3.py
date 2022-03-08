def snake(M):
  s=0
  sm=[]
  for r in M:
    m=[]
    s=s+1
    if s%2==0:
      m=r[::-1]
    else:
      m=r
    sm+=m
  return(sm)
      
      
