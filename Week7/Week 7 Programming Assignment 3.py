r = input()

s = input()

a = r.split(",")

b = s.split(",")

count = 0

k = 0

for i in range(len(b)):
  
  count = count + int(b[k])
  
  k += 1
  
  for j in a:
    
    n = j.split(":")
    
    if count == int(n[0]):
      
      count = int(n[1])
      
if count>= 100:
  
  print("Yes", end="")
  
else:
  
  print("No", end="")
      