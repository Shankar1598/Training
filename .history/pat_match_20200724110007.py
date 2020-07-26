d = 256
q = 101

def search(pat, txt, q):
  patLen = len(pat)
  txtLen = len(txt)

  patHash = 0
  texHash = 0

  h = 1