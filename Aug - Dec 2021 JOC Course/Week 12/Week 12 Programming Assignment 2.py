x = list(map(int, input().split()))
x.sort()
print(x[-1] + x[-2], end="")
