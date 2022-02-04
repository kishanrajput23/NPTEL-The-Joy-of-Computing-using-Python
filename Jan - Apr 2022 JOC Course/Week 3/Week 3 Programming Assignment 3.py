def all_even(L):
  for i in L:
    if i%2 == 0:
      print(i)
    
L = [int(i) for i in input().split()]
all_even(L)