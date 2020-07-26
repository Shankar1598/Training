class Param:

  def __init__(self):
    self.processQ = []
    self.visits = set()
    self.solutionFound = False

  def enqueue(self, string):
    self.processQ.append(string)

  def pop(self):
    return self.processQ.pop(0)


  def isValidString(self, string):
    count = 0
    for char in string:
      if char == '(':
        count+=1
      elif char == ')':
        count-=1
      if count < 0:
        return False
      
    return (count == 0)

  def isParam(self, char):
    return (char == '(' or char == ')')

  def removeIndex(self, string, pos):
    part1 = 

  def removeInvalidParam(self, string):
    self.solutionFound = False
    self.enqueue(string)

    while (len(self.processQ) > 0):
      currentStr = self.pop()

      if self.isValidString(currentStr):
        print(currentStr)
        self.solutionFound = True
      elif self.solutionFound == False:
        for i in range(len(currentStr)):
          if not self.isParam(currentStr[i]):
            continue
          
          removedStr = self.removeIndex(currentStr, i)