my_str = input()
no_punct = ""
for char in my_str:
    if char.isalnum() or char == ' ':
           no_punct = no_punct + char
print(no_punct, end="") 
