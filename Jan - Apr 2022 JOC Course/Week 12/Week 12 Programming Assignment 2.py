L=input().split()
M=[]
for i in L:
  M.append("".join(list(i)[::-1]))
ans=[]
for i in sorted(M):
  ans.append("".join(list(i)[::-1]))
print(ans,end="")


   