class Param:

  def __init__(self):
    self.processQ = []
    self.visits = set()
    self.solutionFound = False

  def removeInvalidParam(self, string):
    self.solutionFound = False
    self.enqueue(string)