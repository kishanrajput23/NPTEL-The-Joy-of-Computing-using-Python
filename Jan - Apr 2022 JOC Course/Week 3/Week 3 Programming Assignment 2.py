L = [int(i) for i in input().split()]
L.sort()
print(L[0:3])

new = L[-2:]
print(new[::-1])