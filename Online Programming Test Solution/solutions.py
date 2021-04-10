plain_text = input()
encrypted_text = input()

output = ''
for c in plain_text:
  output+=chr((ord(c)+5-ord('A'))%26 + ord('A'))
  

def removeSpaces(str): 
    str = str.replace(' ','') 
    str = str.replace(',','')
    return string.lower()
def check(output, encrypted_text):
     
    # the sorted strings are checked 
    if(sorted(output)== sorted(encrypted_text)):
        print("Yes",end='') 
    else:
        print("No",end='')         
         
check(output, encrypted_text)