class Compiler:

  def __init__(self):
    self.array = []
    self.output = []
    self.precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}

  def isOperand(self, el):
    return el.isalpha()

  def push(self, el):
    self.array.append(el)

  def getPostfix(self, exp):

    for element in exp:
      if self.isOperand(element):
        self.output.append(element)
      elif element == '(':
        self.push(element)
      elif element == ')'



exp = "a+b*(c*d-e)-f"