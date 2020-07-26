class Param:

  def __init__(self):
    self.processQ = []
    self.visits = set()
    self.solutionFound = False

  def enqueue(self, string):
    self.processQ.append(string)

  def pop(self):
    self.processQ.pop(0)

  def removeInvalidParam(self, string):
    self.solutionFound = False
    self.enqueue(string)

    while (len(self.processQ) > 0):
      currentStr = self.pop()
      