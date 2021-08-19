from math import factorial

num = input().split()

zeroes = factorial(num.count('0'))

ones = factorial(num.count('1'))

trails = factorial(len(num))

arrangements = trails // (zeroes * ones)

print(arrangements, end="")