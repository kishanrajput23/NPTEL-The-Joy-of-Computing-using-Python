a,b,c,d = int(input()),input().split(),0,[]

key = [b[i-a:i] for i in range(1, len(b) + 1) if i % a == 0]

for i in range(a):
  l = []
  
  for j in range(a):
    l.append(key[j][i])
  d.append(l)
  
for m in range(a):
  if d[m].count('1') == 2:
    c = m + 1   
    
if c!=0:
  print("yes",c,end="")
  
else:
  print("no",end="")
    
       
    
