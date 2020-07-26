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
          print("error, ( ")




exp = "a+b*(c*d-e)-f"




stack = [1,5,6,13,2]

stack.peak -> 2

stack.pop -> 2

stack = [1,5,6]

stack.pop -> 13