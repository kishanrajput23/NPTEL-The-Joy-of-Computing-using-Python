n=input()

k = input()

res = list()

lst1=list()

lst1 = k.split(" ")

for i in lst1:
  
  if i not in res:
    
    res.append(i)
    
for j in range(0,len(res)):
  
  if j!=len(res)-1:
    
    print(res[j],end=" ")
    
  else:
    
    print(res[j],end="")