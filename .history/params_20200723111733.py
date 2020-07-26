class Param:

  def __init__(self):
    self.processQ = []
    

  def removeInvalidParam(self, string):
    self.solutionFound = False
    self.enqueue(string)