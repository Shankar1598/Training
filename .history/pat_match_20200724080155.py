d=256

def search(pat, txt, q):
  patLen = len(pat)
  txtLen = len(txt)

  patHash = 0
  txtHash = 0

  h=1

  for i in range(patLen - 1):
    h = (h*d)%q

  for i in range(patLen):
    patHash = (d * patHash + ord(pat[i]))%q
    txtHash = (d * txtHash + ord(txt[i]))%q
    

  for i in range(txtLen - patLen + 1)