n,m=map(int,input().split())
b=0

for i in range(n):
    for j in range(1):
        temp=[int(g) for g in input().split()]
        for k in temp:
            if k!=0 and k!=1:
                b=b+1
                break

if b==0:
    print("Yes",end="")
else:
    print("No",end="")