num=input().split()

n =int(input())

l = []
for i in num:
  l.append(int(i))
  
max = sorted(l, reverse=True)

min = sorted(l)

max_num = []

min_num = []

for j in max:
  if j not in max_num:
    
    max_num.append(j)
    
for k in min:
  if k not in min_num:
    
    min_num.append(k)
    
result = max_num[n-1]+min_num[n-1]
print(result, end="")


  

