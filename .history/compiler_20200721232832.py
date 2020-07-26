class Compiler:

  def __init__(self):
    self.array = []
    self.output = []
    self.precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}

  # operand or not? (a,b,c)
  def isOparand(self, el):
    return el.isalpha()

  def push(self, el):
    self.array.append(el)

  def infixToPostfix(self, exp):
    for element in exp:
      if self.isOparand(element):
        self.output.append(element)
      elif element == '(':
        self.push(element)
      elif element == ')':
        while (not self.isEmpty() and self.peak() == '(')




compiler = Compiler()
compiler.infixToPostfix("123")