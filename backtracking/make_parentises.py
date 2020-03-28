def make(strs,open,close,n):
  if open==n and close==n:
    print(strs)
  else:
    if open<=close:
      make(strs+'{',open+1,close,n)
    if open>close:
      make(strs+'}',open,close+1,n)
  return
  
make('',0,0,3)