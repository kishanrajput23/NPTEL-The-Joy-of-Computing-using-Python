s = input().split(',')
D = {}
snake = 0
ladder = 0
for i in s:
    t = i.split(':')
    D[int(t[0])] = int(t[1])
for val in D:
    if D[val] > val:
        ladder += 1
    else:
        snake += 1
print(str(snake)+' '+str(ladder),end='')