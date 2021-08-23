lst = input().split()

k = int(input())

for i in lst:
  if lst.count(i) == k:
    print(i, end="")
    break