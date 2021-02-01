a = [int(x) for x in input().split()]

a.sort() #this command sorts the list in ascending order

if a[-2]==a[-1]:
  print(a[-3]+a[1])
  
  
else:
  print(a[-2] + a[1])
