import random
s = input()
t = input()
u = ''
for i in s:
    u += chr((ord(i) - ord('A') + 5)%26 + ord('A'))
l = list(t)
l.sort()
m = list(u)
m.sort()
if l == m:
    print('Yes',end='')
else:
    print('No',end='')