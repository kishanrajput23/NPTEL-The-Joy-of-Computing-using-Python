def DiagCalc(L):
  L_sum=0
  R_sum=0
  m=L[::-1]
  for i in range(len(L)):
    for j in range(len(L)):
      if i==j:
        L_sum+=L[i][j]
        R_sum+=m[i][j] 
  print(L_sum)  
  print(R_sum,end="")
  
  
  
        
        