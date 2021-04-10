x = [int(i) for i in input().split()]

moves = 0

temp = sum(x)



if temp % len(x) == 0:
  
  for j in range(len(x)):
    
    if x[j] < (temp // len(x)):
      
      moves = moves + ((temp // len(x))- x[j])
      
  print(moves,end='')
  
else:
  
  print('-1',end='')