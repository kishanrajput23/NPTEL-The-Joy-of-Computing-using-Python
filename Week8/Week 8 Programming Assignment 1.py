import sys
m,n = input().split()
for i in range(int(m)):
    for k in [int(j) for j in input().split()]:
        if k!=0 and k!=1:
            print("No",end="")
            sys.exit()
        
else:
    print("Yes",end="")
