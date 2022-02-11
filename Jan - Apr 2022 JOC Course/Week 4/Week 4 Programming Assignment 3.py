new  = [x for x in L if L.count(x) == 2]

res = []
[res.append(x) for x in new if x not in res]
  
for i in res:
  print(i)
