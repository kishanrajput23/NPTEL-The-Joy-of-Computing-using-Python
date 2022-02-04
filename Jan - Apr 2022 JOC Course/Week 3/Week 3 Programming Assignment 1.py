L = [int(i) for i in input().split()]
n = len(L)
l = L[1:n:2]
for i in l:
  print(i)