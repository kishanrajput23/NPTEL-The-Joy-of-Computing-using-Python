lst1 = [int(x) for x in input().split()]

lst2 = []

sum = 0

for i in lst1:
  sum += i
  lst2.append(sum)
  
print(*lst2,end="")
  
#str1 = ' '.join([str(elem) for elem in lst2])
  
#print(str1, end="")
  
