n=int(input())
l=[]
for i in range(n):
    for j in range(1):
        temp=[int(g) for g in input().split()]
        l.append(temp)
x=0
for i in range(n):
    for j in range(n):
        if l[i][j]!=l[j][i]:
           x=x+1
if x==0:
  print("Yes",end="")
else:
  print("No",end="")