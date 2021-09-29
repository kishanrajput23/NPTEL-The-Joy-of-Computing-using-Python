large_string = input()
small_strings = input().split()
new_str = ""
for i in small_strings:
  new_str += i
if(set(large_string) == set(new_str) and len(large_string) == len(new_str)):
  print("Yes",end="")
else:
  print("No",end="")