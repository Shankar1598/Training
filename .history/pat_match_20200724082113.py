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
    

  for i in range(txtLen - patLen + 1):

    if patHash==txtHash:
      matched = True
      # str cmp
      for j in range(patLen):
        if pat[j]!=txt[i+j]:
          matched = False

      if matched:
        print("Match found at index: "+ str(i))

    if i < txtLen - patLen:
      hashOfChar1 = ord(txt[i])*h
      txtHash = (d * (txtHash -  hashOfChar1) + ord(txt[i+patLen]))%q

      if txtHash < 0:
        txtHash+=q

txt = "GEEKS FOR GEEKS"
pat = "GEEK"
q = 101 # A prime number 
search(pat,txt,q) 
