arr=input().split()

swap=0

for i in range(len(arr)):
  
  for j in range(i+1,len(arr)):
    
    if(int(arr[i])>int(arr[j])):
      
      temp=arr[i]
      
      arr[i]=arr[j]
      
      arr[j]=temp
      
      swap = swap+1

print(swap,end="")
      