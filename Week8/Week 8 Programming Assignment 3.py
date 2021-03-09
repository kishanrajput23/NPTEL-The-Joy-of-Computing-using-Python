R = int(input())

print('\n'.join(' '.join(str(R*row + col) for col in range(1, R+1)) for row in range(R)), end='')