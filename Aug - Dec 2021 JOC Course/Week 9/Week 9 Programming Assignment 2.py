s = input().split(',')
l = list(map(int,input().split(',')))
D = {}
count = 0
for i in s:
    t = i.split(':')
    D[int(t[0])] = int(t[1])
for val in l:
    count += val
    if count in D:
        count = D[count]
        
if count >= 100:
    print("Yes", end='')
else:
    print("No", end='')