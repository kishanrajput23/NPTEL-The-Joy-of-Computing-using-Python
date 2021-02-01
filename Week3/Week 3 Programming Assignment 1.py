arr = input().split(" ")

res = []

new = []

for i in range(len(arr)):
  
  if arr[i].endswith("4"):
    res.append(arr[i])
    
  else:
    new.append(arr[i])
    
    
listToStr = ' '.join([str(elem) for elem in new])

print(listToStr)
    
    