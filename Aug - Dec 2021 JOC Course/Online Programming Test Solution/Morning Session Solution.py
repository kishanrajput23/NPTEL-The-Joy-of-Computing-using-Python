import textwrap
s = input()
w = int(input())


wrapper = textwrap.TextWrapper(width=w)
  
word_list = wrapper.wrap(text=s)
  
# Print each line.
for element in word_list:
    print(element)