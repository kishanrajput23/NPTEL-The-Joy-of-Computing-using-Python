import numpy as np    # importing numpy module

# taking endpoints from the user as point_1, point_2 & point_3

point_1 = list(map(float,input().split()))    
point_2 = list(map(float,input().split()))
point_3 = list(map(float,input().split()))

arr = np.array([point_1,point_2,point_3]) 

volume = abs(np.linalg.det(arr))

final = float("{0:.1f}". format(volume))

print(final,end="")