Cap=list("ABCDEFGHIJKLMNOPQRSTUVMWXYZ")
Small=list('abcdefghijklmnopqrstuvwxyz')
ans=""
for a in S:
  if a=='a':
    ans+='y'
  elif a=='b':
    ans+='z'
  elif a=='A':
    ans+='X' 
  elif a=='B':
    ans+='Y'
  elif a=='C':
    ans+='Z'
  elif a=='W':
    ans+='T'
  else:
    if a in Cap:
      ans+=Cap[Cap.index(a)-3]
    elif a in Small:
      ans+=Small[Small.index(a)-2]
    else:
      ans+=a
print(ans,end="")