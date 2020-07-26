d=256

def search(pat, txt, prime):
  patLen = len(pat)
  txtLen = len(txt)

  patHash = 0
  txtHash = 0

  h=1
  q = 101

  for i in xrange(patLen - 1):
    h = (h*d)%prime

  