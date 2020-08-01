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
    patHash = (d * patHash + ord(pat[i]))%q
    txtHash = (d * txtHash + ord(txt[i]))%q


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
      txtHash = (d * (txtHash - hashOfChar1) + ord(txt[i+patLen]))%q

      if txtHash < 0:
        txtHash += q


txt = "THE RAT ATE THE CAT"
pat = "THE"
search(pat, txt, 101)

# constants -> d, h, q
# d = 256
# h = d ^ ((length_of_pattern) - 1)
# q = a_prime_number

# initial hash.
# loop every charecter
  # nextHash = (d * previousHash + ord(currentCharecter)) % primeNumber

# normal hash -> subtract the  hash of 1st char, add the hash of the new last char.
# hashOfFirstChar = ord(firstChar)*h
# nextHash = (d * (previousHash - hashOfFirstChar) + ord(newLastCharecter)) % primeNumber

