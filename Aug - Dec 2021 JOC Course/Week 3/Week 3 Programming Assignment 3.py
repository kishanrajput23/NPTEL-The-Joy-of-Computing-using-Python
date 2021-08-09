int_num = list(map(int,input().split()))

x, y, z = sorted(int_num)

if x**2 + y**2 == z**2:
  
    print('YES', end="")

else:
    print('NO', end="")