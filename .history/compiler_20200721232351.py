class Compiler:

  def __init__(self):
    self.array = []
    self.output = []
    self.precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}

  # operand or not? (a,b,c)
  def isOparand(self, el):
    return el.isalpha()

  def infixToPostfix(self, exp):
    for element in exp:
      if self.isOparand(element):
        self.output.append(element)
      elif element == '(':
        




compiler = Compiler()
compiler.infixToPostfix("123")