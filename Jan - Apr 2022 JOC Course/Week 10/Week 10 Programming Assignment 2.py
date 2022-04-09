def closestSchool(x, y, L):
  min=99999
  distance=[]
  for i in L: 
    dis=((x-i[0])**2+(y-i[1])**2)**0.5
    distance.append(dis)
    if dis<min:
      min=dis 
  for i in range(len(distance)):
    if distance[i]==min:
        print(L[i])