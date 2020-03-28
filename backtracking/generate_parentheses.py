
def make(strp,n,open,close):
  if close==n:
    print(strp)
    return
  else:
    if open>close:
      make(strp+'}',n,open,close+1)
    if open<n:
      make(strp+'{',n,open+1,close)
  return
make('',2,0,0)