d=256

def search(pat, txt):
  patLen = len(pat)
  txtLen = len(txt)

  patHash = 0
  txtHash = 0

  h=1

  for i in 