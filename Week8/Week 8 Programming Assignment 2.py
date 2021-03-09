l =[]
for i in range(int(input())):
    l.append([int(j) for j in input().split()])
k=[list(i) for i in zip(*l)]
print("Yes",end="") if  (k==l) else print("No",end="")