vowel = "AEIOUaeiou "
for i in s:
  if i not in vowel:
    s = s.replace(i, "_")  
print(s)
