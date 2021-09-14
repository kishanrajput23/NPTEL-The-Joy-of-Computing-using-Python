str_1 = input()

str_2 = input()

sorted_str1 = []

sorted_str2 = []

k = sorted(str_1.upper())

l = sorted(str_2.upper())

for i in k:
  if i.isalnum():
    sorted_str1.append(i)
    
for j in l:
  if j.isalnum():
    sorted_str2.append(j)
    
if sorted_str1 == sorted_str2:
  print("Yes", end="")
else:
  print("No", end="")