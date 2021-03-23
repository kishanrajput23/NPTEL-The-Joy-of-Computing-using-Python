a,b,c = int(input()),input().split(),0

key = [b[i-a:i] for i in range(1, len(b)+1)if i%a==0 and b.count("0")!=a*a]

for i in range(a):
  
  for j in range(a):
    
    if len(key) > 1 and key[i][j] == key[j][i]:
      
      c=c+1
      
if c == a*a:
  print("yes",end="")
  
else:
  print("no",end="")
    
    
    
    
       
    
