num = int(input())

factorial = 1

for i in range(1, num+1):
  
  factorial *= i
  
print(factorial, end="")