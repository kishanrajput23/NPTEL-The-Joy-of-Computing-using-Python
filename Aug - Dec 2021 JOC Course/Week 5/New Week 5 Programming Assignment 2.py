lst = [int(x) for x in input().split()]

k = int(input())

lst.sort()

print(lst[-k], end="")