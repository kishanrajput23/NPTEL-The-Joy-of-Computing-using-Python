def count_letters(string):
  d={}
  for s in string:
    if s not in d:
      d[s]=string.count(s)
  return(d)
  