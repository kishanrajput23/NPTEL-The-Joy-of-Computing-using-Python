a,b,c = int(input()),input().split(),0

key = [b[i-a:i] for i in range(1,len(b)+1) if i % a == 0]

for i in range(len(key)):
  
  if key[i].count('1') == 2:
    c = i+1
    
if c!=0:
  print("yes",c,end="")
  
else:
  print("no",end="")
    
       
    
