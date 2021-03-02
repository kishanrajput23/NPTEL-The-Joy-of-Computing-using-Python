num = input()

k = num.split(",")

m = 0

n = 0

for i in k:
  
  j= i.split(': ')
  
  if(int(j[0])> int(j[1])):
    
    m+=1
    
  if(int(j[1])> int(j[0])):
    
    n+=1
    
print(m, end="")

print(" ",end="")

print(n, end="")