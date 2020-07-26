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

  def isEmpty(self):
    return len(self.array) == 0

  def peak(self):
    return self.array[-1]

  def pop(self):
    if self.isEmpty():
      return "$"
    else:
      self.array.pop()

  def infixToPostfix(self, exp):
    for element in exp:
      if self.isOparand(element):
        self.output.append(element)
      elif element == '(':
        self.push(element)
      elif element == ')':
        while (not self.isEmpty() and self.peak() != '('):
          self.output.append(self.pop())
        if (not self.isEmpty() and self.peak() != '('):
          # error
          return -1
        else:
          self.pop()
      else:
        # operator
        while(not self.isEmpty() and not self.isGreater(element)):






compiler = Compiler()
compiler.infixToPostfix("123")