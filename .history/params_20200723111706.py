class Param:
  def removeInvalidParam(self, string):
    self.solutionFound = False
    self.enqueue(string)