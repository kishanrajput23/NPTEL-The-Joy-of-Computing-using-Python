SL=sorted(list(set(L)))
IL=[0]*(max(SL)+1)
for i in range(len(SL)):
  IL[SL[i]]=SL[i]
print(*IL,end="")  
    