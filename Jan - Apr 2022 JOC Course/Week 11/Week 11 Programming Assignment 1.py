a=int(input())
b=int(input())
c=int(input())
L=[a,b,c]
h=max(L)
L.remove(h)
if h**2==L[0]**2+L[1]**2:
  print("YES",end="")
else:
  print("NO",end="")
