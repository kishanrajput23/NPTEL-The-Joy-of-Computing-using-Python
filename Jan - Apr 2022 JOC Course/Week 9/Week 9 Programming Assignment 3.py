N=list(str(n))
P=[]
for i in N:
  if i not in P:
    P.append(i)
ans=[]
for i in range(len(P)):
  a=[]
  for j in range(len(N)):
    if(P[i]==N[j]):
      a.append(j)
  ans.append(a)
#print(ans)

for i in range(len(P)):
  print(int(P[i]), "",end="")
  #print(len(ans[i]))
  for j in range(len(ans[i])):
               print(int(ans[i][j]),"",end="")
  print()
           
        
  
      
    
  
  