z=[]
a=[]
for i in L:
  if i!=0:
    a.append(i)
  else:
    z.append(0)
print(a+z,end="")