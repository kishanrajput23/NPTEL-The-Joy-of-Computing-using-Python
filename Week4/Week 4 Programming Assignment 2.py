def fact(num):

 product=1

 while(num>1):

   product*=num

   num-=1

 return product

m=int(input())  #m=men

n=int(input())  #n=women

if  m+n>20 or m<=n:

 print('invalid',end="")

else:

  print(fact(m)*fact(n)*fact(m+1)//(fact(n)*fact(m+1-n)),end="")