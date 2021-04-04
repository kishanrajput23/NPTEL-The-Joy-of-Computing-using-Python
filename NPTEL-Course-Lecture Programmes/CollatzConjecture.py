

def collatz(n):
    count=1
    while(n!=1):
        if(n%2==0):
            n=int(n/2)
            count+=1
        else:
            n=(n*3)+1
            count+=1
        
    print(count)

number= int(input("Enter a number : "))

collatz(number)