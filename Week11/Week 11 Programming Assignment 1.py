# PYTHON program to count ways to write
# number as sum of even integers
# Initialize mod variable as constant

MOD = 1e9 + 7
  
# Iterative Function to calculate 
# (x^y)%p in O(log y) 

def power(x, y, p) :
    res = 1      # Initialize result
   
    x = x % p  # Update x if it is more 
               # than or equal to p
   
    while (y > 0) :
          
        # If y is odd, multiply x
        # with result
        
        if (y & 1) :
            res = (1 * res * x) % p
          
        # y must be even now
        
        y = y >> 1  # y = y/2
        x = (1 * x * x) % p
          
          
    return res
  
   
# Return number of ways to write 'n'
# as sum of even integers

def countEvenWays(n) :
  
    return power(2, n//2 - 1, MOD)
  
# Driver code

n = int(input())

if n % 2==0:
  
  print(int(countEvenWays(n)))
  
else:
  
  print("invalid")
