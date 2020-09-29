# list filtering

def filter_list(l):
  'return a new list with the strings filtered out'
  res=[]
  for x in l:
      if type(x)!=str:
          res.append(x)
  return res