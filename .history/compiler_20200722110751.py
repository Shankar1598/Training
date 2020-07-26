class Compiler:

  def __init__(self):
    self.array = []
    self.output = []
    self.precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}

  def isOperand(self, el):
    return el.isalpha()

  def push(self, el):
    self.array.append(el)

  def isEmpty(self):
    return (len(self.array) == 0)

  def peak(self):
    return self.array[-1]

  def pop(self):
    return self.array.pop()

  def notGreater(self, el):
    try:
      return self.precedence[el] < self.precedence[self.peak()]
    except KeyError:
      return False

  def clear(self):
    self.array = []
    self.output = []

  def getPostfix(self, exp):

    for element in exp:
      if self.isOperand(element):
        self.output.append(element)
      elif element == '(':
        self.push(element)
      elif element == ')':
        while (not self.isEmpty() and self.peak() != '('):
          self.output.append(self.pop())
        if self.isEmpty():
          print("error, ( not found")
        else:
          self.pop()
      else:
        # operator
        while (not self.isEmpty() and self.notGreater(element)):
          self.output.append(self.pop())
        self.push(element)

    while (not self.isEmpty()):
      self.output.append(self.pop())

    return "".join(self.output)

  def evaluate(self, exp):
    self.clear()
    for element in exp:
      if element.isdigit():
        self.push(element)
      else:
        # operator


exp = "a+b*(c*d-e)-f"
compiler = Compiler()
postfix = compiler.getPostfix(exp)

print(postfix)