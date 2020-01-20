def path(path):
  pathArray = path.split('/')
  result = []
  for item in pathArray:
    if item!='' and item!='.':
      if item=='..' and len(result)>0:
        result.pop()
      elif item!='..':
        result.append(item)

  if len(result)>0:
    final_path = '/'
    for item in result:
      final_path+=item+'/'
    return final_path[:-1]
  else:
    return '/' 



print(path("/../../../../a/"))