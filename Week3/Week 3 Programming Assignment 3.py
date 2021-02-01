a = [int(x) for x in input().split()]

res = []

for i in a: 
    if i not in res: 
        res.append(i) 
  
listToStr = ' '.join([str(elem) for elem in res])

print(listToStr)