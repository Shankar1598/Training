d = 256

def search(pat, txt, q):
  patLen = len(pat)
  txtLen = len(txt)

  patHash = 0
  txtHash = 0

  h = 1 # pow(d, patHash-1)

  for i in range(patLen-1):
    h = (h*d)%q

  for i in range(patLen):
    print(patHash, txtHash)
    patHash = (d * patHash + ord(pat[i]))%q
    txtHash = (d * texHash + ord(txt[i]))%q


  for i in range(txtLen - patLen + 1):
    if patHash == txtHash:
      matched = True
      for j in range(patLen):
        if pat[j] != txt[i+j]:
          matched = False

      if matched:
        print("Match found at: " + str(i))

    if i < txtLen - patLen:
      hashOfChar1 = ord(txt[i])*h
      texHash = (d * (txtHash - hashOfChar1) + ord(txt[i+patLen]))%q

      if txtHash < 0:
        texHash += q

txt = "THE RAT ATE THE CAT"
pat = "THE"
search(pat, txt, 101)