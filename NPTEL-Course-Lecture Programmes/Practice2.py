#to rotate a line in python

line= input().split(sep=",")
line2=input().split(sep=",")
dic={}
point=0
#to check fall or rise
def check(no):
    p=0
    if no in dic:
        p=dic[no]
    return p
        
        
for i in range(len(line)):
    spl=line[i].split(":")
    dic[spl[0]]=spl[1]
    

for i in range(len(line2)):
    roll=int(line2[i])
    point+=roll
    new_pt=check(point)
    if new_pt!=0:
        point=new_pt

print(point)    
if point>=100:
    print("Yes")
else:
    print('No')    