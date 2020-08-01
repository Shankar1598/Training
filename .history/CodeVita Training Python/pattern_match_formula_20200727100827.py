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

