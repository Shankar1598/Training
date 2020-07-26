def isShuffledSubStr(str1, str2):
  len1 = len(str1)
  len2 = len(str2)

  if len1 > len2:
    return False

  sorted1 = sorted(str1)

  for i in range(len2):
    if (i+len1 > len2):
      return False

    subStr = ""
    for j in range(len1):
      subStr += str2[i+j]

    subStr = sorted(subStr)

    if sorted1 == subStr:
      return True



# s1 -> goodbye
# s2 -> hellobyegoodworld
# sub -> byegood