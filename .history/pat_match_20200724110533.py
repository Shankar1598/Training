d = 256
q = 101

def search(pat, txt, q):
  patLen = len(pat)
  txtLen = len(txt)

  patHash = 0
  texHash = 0

  h = 1 # pow(d, patHash-1)

  for i in range(patLen-1):
    h = (h*d)%q

  for i in range(patLen):
    patHash = (d * patHash + ord(pat[i]))%q
    txtHash = (d * texHash + ord(txt[i]))%q

  for i in range(txtLen - patLen + 1):
    