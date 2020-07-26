class Compiler:

  def __init__(self):
    self.array = []
    self.output = []
    self.precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}

  def getPostfix(self, exp):

    for element in exp:
      if self.isOperand(element):
        self.output.append(element)