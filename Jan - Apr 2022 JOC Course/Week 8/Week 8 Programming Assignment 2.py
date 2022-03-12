def replaceV(s):
  a=s
  v=list("aeiou"+"AEIOU")
  for i in range(len(s)-2):
    if s[i] in v and s[i+1] in v and s[i+2] in v:
        a=a.replace(s[i]+s[i+1]+s[i+2],'_')
  return(a)
    
    