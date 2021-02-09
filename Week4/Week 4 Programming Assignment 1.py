def arrange_number(a, b):

   if a>b:

       s=b

   else:

       s=a

   for i in range(1, s+1):

       if a%i==0 and b%i==0:

           result=i

   return result

 

m=int(input())

n=int(input())

print(arrange_number(m,n))

