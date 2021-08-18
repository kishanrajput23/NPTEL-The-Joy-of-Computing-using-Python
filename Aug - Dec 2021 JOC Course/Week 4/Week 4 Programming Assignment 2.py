num = map(int, input().split())

count = 0

for i in num:
  if i%3 == 0 or i%5 == 0:
    count += 1
    
print(count, end="")