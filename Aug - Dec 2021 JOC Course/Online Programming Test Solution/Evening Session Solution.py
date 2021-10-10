s=input()
j=0
for i in range(len(s)):
    if j>=len(s)-1:
        break
    n=s[j]
    while s[j]==s[j+1]:
        n = n+s[j]
        j+=1
        if j >= len(s)-1:
            break
    j+=1
    print("({},{})".format(len(n), n[0]),end="")
if(s[len(s)-1]!=s[len(s)-2]):
    print("(1,{})".format(s[len(s)-1]),end="")