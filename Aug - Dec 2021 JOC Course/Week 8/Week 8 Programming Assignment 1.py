def isPalindrome(s):
    
    return new_string.lower() == new_string[::-1].lower()
  
# Driver code
s = input()
new_string = ''.join(char for char in s if char.isalnum())


ans = isPalindrome(s)
 
if ans:
    print("Yes", end="")
else:
    print("No", end="")