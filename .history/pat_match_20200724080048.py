d=256

def search(pat, txt, prime):
  patLen = len(pat)
  txtLen = len(txt)

  patHash = 0
  txtHash = 0

  h=1

  for i in range(patLen - 1):
    h = (h*d)%prime

  for i in range(patLen):
    patHash = (d * patHash + ord(pat[i]))%prime
    txtHash = (d * txtHash + ord(txt[i]))%prime
    