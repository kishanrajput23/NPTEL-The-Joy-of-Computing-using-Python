d=[int(i) for i in input().split()]
s=sum(d)
result=0
if s%len(d)==0:
  for i in range(len(d)):
    if d[i]<(s//len(d)):
      result=result+((s//len(d))-d[i])
  print(result,end='')
else:
  print('-1',end='')