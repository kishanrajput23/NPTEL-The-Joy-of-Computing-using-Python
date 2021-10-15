for t in range(int(input())):
    n = int(input())
    a = [int(i1) for i1 in input().split()]
    mn,mnidx,mx,mxidx=a[0],0,a[0],0
    
    for i in range(0,n):
        if a[i]<mn:
            mn=a[i]
            mnidx=i
        if a[i]>mx:
            mx=a[i]
            mxidx=i
    
    val1 = max(mnidx,mxidx)
    val2 = min(mnidx,mxidx)
    print(min([val2-val1+1+n, val1+1,n-val2]))
