# Python3 implementation to  
# find first element  
# occurring k times 
  
# function to find the  
# first element occurring  
# k number of times 
def firstElement(arr, n, k): 
  
    # dictionary to count 
    # occurrences of  
    # each element 
    count_map = {}; 
    for i in range(0, n): 
        if(arr[i] in count_map.keys()): 
            count_map[arr[i]] += 1
        else: 
            count_map[arr[i]] = 1
        i += 1
      
    for i in range(0, n):  
          
        # if count of element == k , 
        # then it is the required 
        # first element  
        if (count_map[arr[i]] == k): 
            return arr[i] 
        i += 1
              
  
# Driver Code 
if __name__=="__main__": 
  
    arr = input().split(" ") 
    n = len(arr) 
    k = int(input())
    print(firstElement(arr, n, k)) 