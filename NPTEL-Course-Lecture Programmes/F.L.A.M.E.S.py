# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 22:23:29 2021

@author: Lakhan Kumawat
"""

def remove_matching_letter(list1,list2):
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i]==list2[j]:
                c=list1[i]
                list1.remove(c)
                list2.remove(c)
                l=list1+["*"]+list2
                #print(l)
                return [l,True]
    l=list1+["*"]+list2
    return [l,False]


boy=input("Enter boy's name:  ")
girl=input("Enter girl's name:  ")

boy=boy.lower()
girl=girl.lower()
boy=boy.replace(" ","")
girl=girl.replace(" ","")

l1=list(boy)
l2=list(girl)
proceed=True
while proceed:
    # Traverse and point matching letter if No loop will exit
    ret_list=remove_matching_letter(l1,l2)
    #conconated list is returned at 0 place and at 1 bool
    con_list=ret_list[0]
    proceed=ret_list[1]
    #find the position of start index
    star_index=con_list.index("*")
    #divide the lists 
    l1=con_list[:star_index]
    l2=con_list[star_index+1:]

#counter=l1.count()+l2.count()    
counter=len(l1)+len(l2)

result=["Friend","Loves","Affection","Marriage","Enemy","Sister"]

while len(result)>1:
    #modular way of representation
    split_index=(counter%len(result))-1
    if split_index>0:
        right=result[split_index+1:]
        left=result[:split_index]
        result=right+left
    else:
        result=result[:len(result)-1]
        
        
print(boy," ",result[0]," ",girl)











